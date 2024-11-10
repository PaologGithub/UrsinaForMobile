# Ursina on Mobile - Step 1c: Setting up your game

Now, you'll need to create the setup.py file. You can use the existing [setup.py template](/src/setup.py), but you'll need to change a few lines:
* Line 14: Change `name='My ursina game'` &rarr; `name='Your game name'`

* Line 16: Change `version='0.0.0'` &rarr; `version='Your game version'`

* Line 20: Change `application_id` &rarr; `application_id: 'com.yourcompany.yourgame'`

* Line 23: If you plan to publish your game into the playstore, you'll need to increment the `android_version_code` by one each time before uploading it

* Line 30: Change `'mygame': 'game/__main__.py'` &rarr; `'yourappdisplayname': 'path\to\your\entry\python_file.py'`

* Line 50 (Optional): Change `'icons'` &rarr; `'icons': {'*': 'mylogo.png'}`

Make sure to **not** remove `ursina_assets` folder or `ursina_assets/**` at line 42 in setup.py, because it is needed to run ursina.

Then, you can put your ursina game inside the [game folder](/src/game). Into the first 2 lines of your main script, add these lines:
```python
from setup_ursina_android import setup_ursina_android
setup_ursina_android()
```
**It is required to run ursina**, because it set's up ursina assets. Make sure you put them at the 2 first lines, not after.

Then, you'll need to modify the Line 5 of [game/setup_ursina_android.py](/src/game/setup_ursina_android.py), like this:
`app_id = "The same as application_id in setup.py (Line 20)"`

If your game needs some requirements, add them in [requirements.txt](/src/requirements.txt). **Do not remove anything, just add**.

[Next -> (Step 1d - Installing android dependencies)](/docs/step1/installing-android-dependencies.md)