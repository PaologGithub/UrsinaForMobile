import os
import sys
from direct.stdpy.file import open, exists
from panda3d.core import ConfigVariableString

app_id = ConfigVariableString("android-app-id", "").getValue()

def setup_ursina_android():
    if sys.platform == "android":
        base_path = f"/data/data/{app_id}/files"
        os.chdir(base_path)

        setup_assets()

        finish(base_path)

def setup_assets():
    import zlib
    import json

    if exists(os.path.join(os.getcwd(), "assets.gen")):
        return

    with open("/android_asset/assets/assets.gen", "rb") as file:
        decompressed = zlib.decompress(file.read()) # type: ignore
        data = json.loads(decompressed)
        open(os.path.join(os.getcwd(), "assets.gen"), "wb").write(file.read()) # type: ignore
    
    os.mkdir("ursina_assets")
    os.mkdir("game_assets")

    for root_folder in data:
        for file in data[root_folder]:
            file_data = data[root_folder][file]
            dir = file_data["dir"]

            src_path = f"/android_asset/assets/{dir}"
            dest_path = os.path.join(os.getcwd(), dir)

            os.makedirs(os.path.dirname(dir), exist_ok=True)

            with open(src_path, 'rb') as src_file, open(dest_path, 'wb') as dest_file:
                dest_file.write(src_file.read()) # type: ignore
                print("Writed file: " + dest_path)

def finish(base_path: str):
    os.chdir(os.path.join(base_path, "ursina_assets"))

    from ursina import application
    from pathlib import Path
    application.package_folder = Path(base_path) / "ursina_assets"
    application.asset_folder = Path(base_path) / "game_assets"

    # Reset the sub paths
    application.internal_models_folder = Path(base_path) / "ursina_assets" / 'models/'
    application.internal_models_compressed_folder = Path(base_path) / "ursina_assets" / 'models_compressed/'
    application.internal_scripts_folder = Path(base_path) / "ursina_assets" / 'scripts/'
    application.internal_textures_folder = Path(base_path) / "ursina_assets" / 'textures/'
    application.internal_fonts_folder = Path(base_path) / "ursina_assets" / 'fonts/'
    application.internal_audio_folder = Path(base_path) / "ursina_assets" / 'audio/'

    os.chdir(os.path.join(base_path, "game_assets"))