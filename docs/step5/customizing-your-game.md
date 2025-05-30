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

## Testing your game
As you'll see, building the game takes time. So, if you want to test your game without building you app each time, you can install ursina 7.0.0 for python3.13 by doing this:

```bash
# I assume that you're in the project root
python3.13 -m pip install src/wheels/ursina-7.0.0-py3-none-any.whl
```

Then, you can test your game by doing this:
```bash
# I assume that you're in the project root, and that your main game file is game/__main__.py
python3.13 src/game/__main__.py
```

## Tips for porting your ursina game for mobile :
Do you remember what you learn about ursina? Forget, now !!!

And by saying that, I want to say that a lot of things in your project is desktop-related. By exemple, you can have a `def input(key)` function, but it doesn't work on Android.
You need to thing that all your project need to be ported for a device that doesn't have mouse, keyboard, windowing system, a lot of performance like gaming PC or an OS integration.

You need to think different (Not by making your game 1200$) to port your app. For exemple, if you have a simple WASD controls, you'll need to make a virtual button/joystick to handle the WASD. 

So don't just put your ursina game into the game folder, port it