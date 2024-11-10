[<- Back (Step 5 - Customizing your project)](/docs/step5/main.md)
# Ursina on Mobile - Customizing assets

For the following tutorial, i imagine that your assets are under `game/assets` folder

You can add assets by doing that:
1) Change [setup.py](/src/setup.py)/setup/build_apps/include_patterns to add your folder. Example:
    ```python
    'include_patterns': [
        'game/assets/**',
        # Don't remove this, it is to include ursina assets
        'ursina_assets/**',
        '**/*.png',
        '**/*.jpg',
        '**/*.egg',
    ],
    ```
2) Get all your assets in a list by writing this in your terminal:
    ```bash
    # I imagine you are at the repo root
    cd src
    cd game
    cd assets
    python
    >>> import os
    >>> os.listdir()
    ['your_first_file.png', 'your_second_file.png']
    ```

    Then, just copy the tuple that os.listdir() returned

3) Modify [setup_ursina_android.py](/src/game/setup_ursina_android.py) like this:
    ```python
    import os
    from direct.stdpy.file import open, exists

    app_id = "your.company.app.name"
    assets = ['ursina_assets']
    my_assets = ['your_first_file.png', 'your_second_file.png']


    def setup_ursina_android():
        # Step 0: Change the path
        os.chdir(f"/data/data/{app_id}/files/")

        # Step 1: Check if there is ursina assets
        missing_assets = []
        for asset in assets:
            src_path = f"/android_asset/ursina_assets/{asset}"
            if not exists(src_path):
                missing_assets.append(asset)
        
        if missing_assets:
            return  # Stop setup if files are missing

        # Step 2: Copy the ursina assets
        for asset in assets:
            src_path = f"/android_asset/ursina_assets/{asset}"
            dest_path = os.path.join(os.getcwd(), os.path.basename(asset))

            with open(src_path, 'rb') as src_file, open(dest_path, 'wb') as dest_file:
                dest_file.write(src_file.read())

        # Step 3: Check if there is your game assets
        my_missing_assets = []
        for asset in my_assets:
            src_path = f"/android_asset/game/assets/{asset}"
            if not exists(src_path):
                my_missing_assets.append(asset)
        
        if my_missing_assets:
            return  # Stop setup if files are missing

        # Step 4: Copy the your game assets
        for asset in my_assets:
            src_path = f"/android_asset/game/assets/{asset}"
            dest_path = os.path.join(os.getcwd(), os.path.basename(asset))

            with open(src_path, 'rb') as src_file, open(dest_path, 'wb') as dest_file:
                dest_file.write(src_file.read())
    ```

And you can now import your assets (Do put `game/assets/your_first_file.png`, just put `your_first_file.png`)