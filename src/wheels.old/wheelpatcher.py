import zipfile
import os
import shutil
import sys
import time

def rename_cpython_so_in_whl(whl_path, file_end):
    # Rename the original wheel file to .non_patched
    original_whl_path = whl_path
    non_patched_whl_path = original_whl_path + '.non_patched'

    print(f"Renaming original wheel {original_whl_path} -> {non_patched_whl_path}")
    os.rename(original_whl_path, non_patched_whl_path)

    # Temporary directory to extract the wheel
    temp_dir = "temp_whl"
    
    # Step 1: Extract the renamed wheel (now with .non_patched) to a temporary directory
    print(f"Extracting {non_patched_whl_path} to {temp_dir}...")
    with zipfile.ZipFile(non_patched_whl_path, 'r') as whl:
        whl.extractall(temp_dir)
    print("Extraction completed.")
    
    # Step 2: Traverse through the extracted files and rename *.cpython-38.so to *.so
    deploy_libs_dir = os.path.join(temp_dir, 'deploy_libs')
    
    if os.path.exists(deploy_libs_dir):
        print(f"Processing files in {deploy_libs_dir}...")
        for root, dirs, files in os.walk(deploy_libs_dir):
            for filename in files:
                if filename.endswith(file_end):
                    old_file = os.path.join(root, filename)
                    new_filename = filename.replace(file_end, '.so')
                    new_file = os.path.join(root, new_filename)
                    print(f"Renaming {old_file} -> {new_file}")

                    # Retry mechanism for renaming to handle possible race conditions
                    retry_count = 3
                    for attempt in range(retry_count):
                        try:
                            os.rename(old_file, new_file)
                            print(f"Renamed successfully: {new_file}")
                            break
                        except FileNotFoundError as e:
                            print(f"Error renaming {old_file}: {e}")
                            if attempt < retry_count - 1:
                                print(f"Retrying... ({attempt + 1}/{retry_count})")
                                time.sleep(1)
                            else:
                                raise

    else:
        print(f"Error: {deploy_libs_dir} does not exist.")
        return

    # Step 3: Create a new wheel archive with the original name
    new_whl_path = original_whl_path  # The patched wheel will have the original name

    print(f"Creating new wheel archive: {new_whl_path}")
    shutil.make_archive(new_whl_path.replace('.whl', ''), 'zip', temp_dir)

    # Rename the zip file back to .whl
    shutil.move(new_whl_path.replace('.whl', '.zip'), new_whl_path)

    # Step 4: Clean up the temporary directory
    shutil.rmtree(temp_dir)
    print(f"Patched wheel saved as: {new_whl_path}")

# Usage
if __name__ == "__main__":
    try:
        whl_path = sys.argv[1]
        file_end = sys.argv[2]
        rename_cpython_so_in_whl(whl_path, file_end)
    except IndexError:
        print("Usage: python3 wheelpatcher.py file_name file_end")
        print("Example: python3 wheelpatcher.py my_wheel.py .cpython-313.so")
        os._exit(1)