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
    * Line 7: 
        ```python
        game_assets = ['your_first_file.png', 'your_second_file.png'] # The same as os.listdir() returned
        ```
    * Line 8:
        ```python
        game_assets_src_dir = "game/assets" # As said at the top, I imagine your assets are in game/assets directory
        ```
        Modifying this line is very important, because it tells the setup that you have assets, because None tells the setup that there isn't any assets, so it won't copy them

And you can now import your assets, like this: 
```python
from ursina import Entity

Entity(texture="your_first_file.png")
# Write texture="your_first_file.png", not texture="game/assets/your_first_file.png"
```