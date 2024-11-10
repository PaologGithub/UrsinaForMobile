# Ursina on Mobile - Step 1b: Installing python dependencies

Install [python 3.8](https://www.python.org/downloads/release/python-380/). This step is really important, because Panda3D for android requires python3.8.

Make sure python3.8 is in your path, and it is the default python installation.
If `python --version` return other things than 'Python 3.8.X', continue this tutorial by replacing all `python` to `python3.8`

Then, you'll need to install [protobuf](https://pypi.org/project/protobuf/). To do that, enter the following command in your terminal:
```bash
python -m pip install protobuf===3.20.0
```

Then, you'll need to install panda3d. To do that, enter the following command for your operating system:
### For windows:
```powershell
python -m pip install https://buildbot.panda3d.org/downloads/68f0931f43284345893a90d5bba9ba5df8aa53bb/panda3d-1.11.0.dev2480-cp38-cp38-win_amd64.whl
```
### For macOS X (Not sure if this works with macOS 11+):
```zsh
python -m pip install https://buildbot.panda3d.org/downloads/68f0931f43284345893a90d5bba9ba5df8aa53bb/panda3d-1.11.0.dev2480-cp38-cp38-macosx_10_9_x86_64.whl
```
### For Linux:
```bash
python -m pip install https://buildbot.panda3d.org/downloads/68f0931f43284345893a90d5bba9ba5df8aa53bb/panda3d-1.11.0.dev2480-cp38-cp38-manylinux2010_x86_64.whl
```

If pip shows an error about the wheel not existing, please [make an issue](https://github.com/PaologGithub/UrsinaForMobile/issues), so I can remake the links.

[Next -> (Step 1c - Setting up your game)](/docs/step1/setting-up-your-game.md)