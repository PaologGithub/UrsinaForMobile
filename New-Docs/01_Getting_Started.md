# Getting Started 🚀

This section will guide you through the initial steps to set up your development environment and prepare your project for mobile deployment.

---

## Prerequisites ✅

Before you begin, make sure you have the following installed on your computer:

- **Git:** Download and install from [git-scm.com](https://git-scm.com/downloads)  
- **Python 3.13:** Get the latest release from the [official Python downloads page](https://www.python.org/downloads/release/python-313/)  
- **OpenJDK 21:** Download from the [OpenJDK 21 page](https://jdk.java.net/21/)  
- **ADB:** Install ADB via [XDA Developers](https://www.xda-developers.com/install-adb-windows-macos-linux/)  
- **BundleTool:** Download the latest version from [BundleTool releases](https://github.com/google/bundletool/releases)

---

## Step 1: Clone the Repository 🔧

1. Open your terminal.
2. Run the following command to clone the repository:

   ```bash
   git clone https://github.com/ShivamKR12/UrsinaForMobile.git
   ```

3. Navigate to the project folder:

   ```bash
   cd UrsinaForMobile
   ```

---

## Step 2: Set Up Your Python Environment 🐍

1. **Install Python 3.13:**  
   Follow the installation instructions from the official Python website. Ensure Python 3.13 is in your PATH. You can verify it by running:

   ```bash
   python --version
   ```

   If it doesn’t show `Python 3.13.x`, use `python3.13` in subsequent commands.

2. **Install Required Python Packages:**

   - **Protobuf:**  
     ```bash
     python -m pip install protobuf
     ```
   
   - **Panda3D (for Android):**  
     Choose the correct wheel for your OS:
     
     - **Windows:**
       ```powershell
       python -m pip install https://buildbot.panda3d.org/downloads/latest/panda3d-cp313-cp313-win_amd64.whl
       ```
     
     - **macOS:**
       ```zsh
       python -m pip install https://buildbot.panda3d.org/downloads/latest/panda3d-cp313-cp313-macosx_10_9_x86_64.whl
       ```
     
     - **Linux:**
       ```bash
       python -m pip install https://buildbot.panda3d.org/downloads/latest/panda3d-cp313-cp313-manylinux2010_x86_64.whl
       ```

*Tip:* If you run into any issues, check the [GitHub Issues](https://github.com/ShivamKR12/UrsinaForMobile/issues) page for help.

---

## Step 3: Configure Your Project 🎮

1. **Create/Update `setup.py`:**  
   - Located in the **src/** folder.
   - Update the following key settings:
     - **Application Name and Version:**  
       ```python
       name='Your game name'
       version='Your game version'
       ```
     - **Application ID:**  
       ```python
       application_id='com.yourcompany.yourgame'
       ```
     - **Android Version Code:**  
       Increase this value before every release.
     - **Entry Point:**  
       Update the mapping for your game’s main file:
       ```python
       'yourappdisplayname': 'path/to/your/entry/python_file.py'
       ```

2. **Set Up Your Game Entry Point:**  
   - Open **src/game/__main__.py**.
   - Add these lines at the very top:
     ```python
     from setup_ursina_android import setup_ursina_android
     setup_ursina_android()
     ```

3. **Configure Android Setup:**  
   - Open **src/game/setup_ursina_android.py**.
   - Update the `app_id` to match the one in `setup.py`:
     ```python
     app_id = "com.yourcompany.yourgame"
     ```

4. **Additional Requirements:**  
   - If your project needs extra dependencies, add them to **src/requirements.txt** without removing existing entries.

---

## Step 4: Set Up Android Dependencies 🤖

1. **Enable Developer Options & USB Debugging on Your Device:**  
   Follow [this guide](https://www.howtogeek.com/129728/how-to-enable-developer-options-menu-and-enable-and-usb-debugging-on-android/).

2. **Install ADB:**  
   Follow the instructions from [XDA Developers](https://www.xda-developers.com/install-adb-windows-macos-linux/).

3. **Install OpenJDK 21:**  
   Ensure OpenJDK 21 is installed and set as your default Java runtime.

4. **Download BundleTool:**  
   Download from the [BundleTool releases page](https://github.com/google/bundletool/releases).

---

## Final Checklist ✅

- [ ] Git repository cloned.
- [ ] Python 3.13 installed and verified.
- [ ] Required Python packages (Protobuf, Panda3D) installed.
- [ ] `setup.py` configured in **src/**.
- [ ] Game entry point updated in **src/game/__main__.py**.
- [ ] Android setup file (`setup_ursina_android.py`) updated.
- [ ] Android dependencies (ADB, OpenJDK 21, BundleTool) installed.

---

You’re now ready to move on to building your app! Check out the next section, **Build Your App**, for instructions on generating your Android App Bundle and converting it to APKs.

Happy coding and enjoy your mobile development journey! 🎮📱✨
