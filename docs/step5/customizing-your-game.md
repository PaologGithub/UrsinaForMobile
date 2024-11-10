[<- Back (Step 5 - Customizing your project)](/docs/step5/main.md)
# Ursina on Mobile - Customizing your game

You can put your ursina game into the [game folder](/src/game). Then, make sure you do this:

1) Change [setup.py](/src/setup.py), by changing setup/build_apps/gui_apps and do `mygame: game/entry_point_of_my_game.py`
2) Add in your entry point of your game these two lines:
    ```python
    from setup_ursina_android import setup_ursina_android
    setup_ursina_android()
    ```
    **This is very important**, because that's what get ursina running on android.

