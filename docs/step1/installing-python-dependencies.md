# Ursina on Mobile - Step 1b: Installing python dependencies

Install [python 3.13](https://www.python.org/downloads/release/python-313/). This step is really important, because Panda3D for android requires python3.13.

Make sure python3.13 is in your path, and it is the default python installation.
If `python --version` return other things than 'Python 3.13.X', continue this tutorial by replacing all `python` to `python3.13`

Then, you'll need to install [protobuf](https://pypi.org/project/protobuf/). To do that, enter the following command in your terminal:
```bash
python -m pip install protobuf===3.20.0
```

Then, you'll need to install panda3d. To do that, enter the following command for your operating system:

### For Windows - 64 BIT:
```bash
python3 -m pip install https://buildbot.panda3d.org/downloads/55fa0e9912633d0406f56033ec166b853e482717/panda3d-1.11.0.dev3596-cp313-cp313-win_amd64.whl
```
### For macOS - Universal:
```bash
python3 -m pip install https://buildbot.panda3d.org/downloads/5b6318e77f3cb1fea519bbd3cd637ad9b0be1606/panda3d-1.11.0.dev3585-cp313-cp313-macosx_11_0_universal2.whl
```
### For macOS - 64 BIT:
```bash
python3 -m pip install https://buildbot.panda3d.org/downloads/5b6318e77f3cb1fea519bbd3cd637ad9b0be1606/panda3d-1.11.0.dev3585-cp313-cp313-macosx_10_13_x86_64.whl
```
### For Linux - 64 BIT:
```bash
python3 -m pip install https://buildbot.panda3d.org/downloads/5b6318e77f3cb1fea519bbd3cd637ad9b0be1606/panda3d-1.11.0.dev3585-cp313-cp313-manylinux2014_x86_64.whl
```

If pip shows an error about the wheel not existing, please [make an issue](https://github.com/PaologGithub/UrsinaForMobile/issues), so I can remake the links.

[Next -> (Step 1c - Setting up your game)](/docs/step1/setting-up-your-game.md)