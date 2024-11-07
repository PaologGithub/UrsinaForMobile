# Ursina on Mobile

* [Step 1 - Setting up the environnment](#step-1-setting-up-the-environnment)
* [Step 2 - Compiling the project](#step-2-compiling-the-project)
* [Step 3 - Installing the app](#step-3-installing-the-app)

# Step 1: Setting up the environnment
First, clone this repository with:
```bash
git clone https://github.com/PaologGithub/UrsinaForMobile
```

Then, install [Python 3.8](https://www.python.org/downloads/release/python-380/)
This step is really important, because Panda3D for android requires python3.8

Then, you'll need to install Panda3D 1.11. To do this, you'll need to do this:

### For Windows:
```bash
python3.8 -m pip install https://buildbot.panda3d.org/downloads/68f0931f43284345893a90d5bba9ba5df8aa53bb/panda3d-1.11.0.dev2480-cp38-cp38-win_amd64.whl
```
### For macosX:
```bash
python3.8 -m pip install https://buildbot.panda3d.org/downloads/68f0931f43284345893a90d5bba9ba5df8aa53bb/panda3d-1.11.0.dev2480-cp38-cp38-macosx_10_9_x86_64.whl
```
### For Linux:
```bash
python3.8 -m pip install https://buildbot.panda3d.org/downloads/68f0931f43284345893a90d5bba9ba5df8aa53bb/panda3d-1.11.0.dev2480-cp38-cp38-manylinux2010_x86_64.whl
```

If pip gives you error about wheel not existing, please [make an issue](https://github.com/PaologGithub/UrsinaForMobile/issues), so I can fix it.

Now, you'll need to create the setup.py file. You can use the existing [setup.py template](/src/setup.py) to help you out, but make sure to change the data, for your current application.

When you finished creating your setup.py, you'll need to put your ursina game into the [game folder](/src/game)

Then, you'll need to edit [requirements.txt](/src/requirements.txt). **Do not delete anything.** Just add the dependencies needed for your project, but the base requirements are needed to run ursina

As you'll see, there is a [wheels folder](/src/wheels). This is where panda3d and ursina code is stored. As you'll see, there is some .non_patched file. This is because base panda3d wheels filenames are `something.cpython-38.so`, which won't be finded by the app, making the app crash.
This is why I made a little tool, [wheelpatcher](/src/wheels/wheelpatcher.py). To use it, just do:
```bash
python wheelpatcher.py wheel_name.whl
```
Pre-included wheels are automatically patched.

There is too the [ursina wheel](/src/wheels/ursina-7.0.0-py3-none-any.whl). I did some works to patch it for python3.8, like removed the `deprecated` decorator, and set the minimum version to 3.8, and removed pyperclip from the dependencies.
And there you finished.

# Step 2: Compiling the project
First, you'll need to compile the panda3d mobile into an aab.
To do that, first change the directory to [src](/src/)
```bash
cd src/
```
Then, actually build the aab
```bash
python3.8 setup.py bdist_apps
```
Then, convert the aab to an apks. To do that, install [BundleTool](https://github.com/google/bundletool/releases), and [Java](https://www.oracle.com/java/technologies/downloads/).

Then, do:
```bash
java -jar Path\To\BundleTool\bundletool.jar build-apks --bundle .\dist\*.aab --output .\dist\app.apks --verbose
```

# Step 3: Installing the app
To install your app, enable Developer Options on your Android phone. Then enable USB Debugging, and plug your phone into your pc with MTP. Make sure you have ADB installed.

Then, do this:
```bash
java -jar Path\To\BundleTool\bundletool.jar install-apks --apks .\dist\*.apks
```