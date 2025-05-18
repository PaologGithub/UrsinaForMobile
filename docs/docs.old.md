# Ursina on Mobile

Steps:
* [Step 1 - Setting up the environment](#step-1-setting-up-the-environment)
* [Step 2 - Compiling the project](#step-2-compiling-the-project)
* [Step 3 - Installing the app](#step-3-installing-the-app)
* [Step 4 - Viewing logs](#step-4-optional-viewing-your-app-logs)

## Step 1: Setting up the environment

* [Step 1.a - Clone the repo and install Python](#step-1a-clone-the-repo-and-install-python)
* [Step 1.b - Installing Panda3D](#step-1b-installing-panda3d)
* [Step 1.c - Setting up your game](#step-1c-setting-up-your-game)

### Step 1.a: Clone the repo and install Python
First, clone this repository with:
```bash
git clone https://github.com/PaologGithub/UrsinaForMobile
```

Then, install [Python 3.13](https://www.python.org/downloads/release/python-313/)
This step is really important, because Panda3D for Android requires Python 3.13.

### Step 1.b: Installing Panda3D
Then, you'll need to install Panda3D 1.11. For this step, please run this command:

For Windows - 64 BIT:
```bash
python3.13 -m pip install https://buildbot.panda3d.org/downloads/55fa0e9912633d0406f56033ec166b853e482717/panda3d-1.11.0.dev3596-cp313-cp313-win_amd64.whl
```
For macOS - Universal:
```bash
python3.13 -m pip install https://buildbot.panda3d.org/downloads/5b6318e77f3cb1fea519bbd3cd637ad9b0be1606/panda3d-1.11.0.dev3585-cp313-cp313-macosx_11_0_universal2.whl
```
For macOS - 64 BIT:
```bash
python3.13 -m pip install https://buildbot.panda3d.org/downloads/5b6318e77f3cb1fea519bbd3cd637ad9b0be1606/panda3d-1.11.0.dev3585-cp313-cp313-macosx_10_13_x86_64.whl
```
For Linux - 64 BIT:
```bash
python3.13 -m pip install https://buildbot.panda3d.org/downloads/5b6318e77f3cb1fea519bbd3cd637ad9b0be1606/panda3d-1.11.0.dev3585-cp313-cp313-manylinux2014_x86_64.whl
```

If pip shows an error about the wheel not existing, please [make an issue](https://github.com/PaologGithub/UrsinaForMobile/issues), so I can remake the links.

### Step 1.c: Setting up your game
Now, you'll need to create the setup.py file. You can use the existing [setup.py template](/src/setup.py) to help you out, but make sure to change the data, to match your application.
**Do not remove** in 'include_patterns' the 'ursina_assets/**', because it is required to make ursina engine running.

When you have finished creating your setup.py, you'll need to put your Ursina Game into the [game folder](/src/game).
Into the first 2 lines of your main script (Default: `src/game/__main__.py`), add these python lines:
```python
from setup_ursina_android import setup_ursina_android
setup_ursina_android()
```
**It needs to be here**, because it is required to get ursina working on Android. So, you need to put them at the **2 first lines**, not after, and if there is a bug/error inside the `setup_ursina_android()` function, please [make an issue](https://github.com/PaologGithub/UrsinaForMobile/issues).
Then, at the 5th line of [game/setup_ursina_android.py](/src/game/setup_ursina_android.py), edit the app_id variable.
If your application id in `setup.py` is 'com.mycompany.ursina.android', edit the 5th line to be
```
app_id = "com.mycompany.ursina.android"
```


Then, you'll need to edit [requirements.txt](/src/requirements.txt). **Do not delete anything.** Add the dependencies needed for your project, but keep the base requirements to run Ursina.

As you'll see, there is a [wheels folder](/src/wheels). This is where panda3d and ursina code is stored. As you'll see, there is some .non_patched file. This is because base panda3d wheels filenames are `something.cpython-38.so`, which won't be found by the app, making the app crash.
This is why I made a little tool, [wheelpatcher](/src/wheels/wheelpatcher.py). To use it, just do:
```bash
python wheelpatcher.py wheel_name.whl
```
Pre-included wheels are automatically patched.

There is also the [Ursina wheel](/src/wheels/ursina-7.0.0-py3-none-any.whl). I made some changes to patch it for Python 3.8, such as removing the `deprecated` decorator, and set the minimum version to 3.8, and removed pyperclip from the dependencies.
And that's it! You're done.

## Step 2: Compiling the project
First, you'll need to compile the panda3d mobile into an aab.
To do that, first change the directory to [src](/src/)
```bash
cd src/
```
Then, actually build the aab
```bash
python3.13 setup.py bdist_apps
```
Then, convert the .AAB to an .APKs. To do that, install [BundleTool](https://github.com/google/bundletool/releases), and [Java](https://www.oracle.com/java/technologies/downloads/).

Then, do:
```bash
java -jar Path\To\BundleTool\bundletool.jar build-apks --bundle .\dist\*.aab --output .\dist\app.apks --verbose
```

## Step 3: Installing the app
To install your app, first enable Developer Options on your Android phone. Then enable USB Debugging, and plug your phone into your PC with MTP. Make sure you have ADB installed.

Then, do this:
```bash
java -jar Path\To\BundleTool\bundletool.jar install-apks --apks .\dist\*.apks
```

## Step 4 (Optional): Viewing your app logs
If your application crashes, or if you want to view the logs, you run the following command:
```bash
adb logcat -v brief -v color 'Panda3D:V' 'Python:V' 'threaded_app:V' 'AndroidRuntime:I' 'linker:W' '*:F'
```