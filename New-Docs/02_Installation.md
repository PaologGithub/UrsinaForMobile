# Installation & Deployment 📦📲

In this section, you'll learn how to build your Ursina mobile app, convert it into APKs, and install it on your device. Follow these step-by-step instructions.

---

## Step 1: Build Your App Bundle (AAB) 📦

1. **Navigate to the Source Directory:**

   Open your terminal, then change to the **src/** directory:

   ```bash
   cd src
   ```

2. **Generate the AAB:**

   Run the following command to build your Android App Bundle:

   ```bash
   python setup.py bdist_apps
   ```

   *Tip:* If you plan to sign your AAB with a certificate, see the [certificate signing guide](docs/generating-the-aab-with-cert.md).

---

## Step 2: Convert AAB to APKS 🔄

Use BundleTool to convert your AAB into APKS, a set of APK files that support multiple architectures.

1. **Run BundleTool:**

   Replace `/path/to/bundletool.jar` with the actual path where you downloaded BundleTool:

   ```bash
   java -jar /path/to/bundletool.jar build-apks --bundle ./dist/*.aab --output ./dist/app.apks --verbose
   ```

2. **Handling Existing APKS:**

   If you encounter an error like:
   
   ```
   [BT:1.17.1] Error: File './dist/app.apks' already exists.
   ```
   
   Simply delete the existing `app.apks` file:

   ```bash
   rm ./dist/app.apks
   ```
   
   Then run the command again.

---

## Step 3: Install the APKS on Your Device 📲

1. **Connect Your Android Device:**

   Ensure your Android device is connected via USB and has USB Debugging enabled. Verify the connection by running:

   ```bash
   adb devices
   ```

   *Note:* Only one device should be connected to avoid installation conflicts.

2. **Install the APKs:**

   Use BundleTool to install the generated APKS:

   ```bash
   java -jar /path/to/bundletool.jar install-apks --apks=./dist/*.apks
   ```

   This command installs the necessary APK files on your device.

---

## Step 4: Verify Installation & Launch Your App 🚀

1. **Launch the App:**

   Once installed, find your app icon on your Android device and tap it to launch.

2. **Check Logs for Debugging (Optional):**

   If you need to view logs to troubleshoot issues, run:

   ```bash
   adb logcat -v brief -v color 'Panda3D:V' 'Python:V' 'threaded_app:V' 'AndroidRuntime:I' 'linker:W' '*:F'
   ```

   To clear the log, execute:

   ```bash
   adb logcat -c
   ```

---

## Final Checklist ✅

- [ ] **AAB Generation:** Successfully built using `python setup.py bdist_apps`.
- [ ] **APKS Conversion:** Converted using BundleTool.
- [ ] **Device Connection:** Only one Android device connected with USB Debugging enabled.
- [ ] **Installation:** App installed on your device via BundleTool.
- [ ] **Testing:** App launched and logs checked (if necessary).

---

Congratulations! You have successfully built and installed your Ursina mobile app. If you run into any issues, refer to the [FAQ & Troubleshooting](../FAQ.md) section or open an issue on [GitHub](https://github.com/ShivamKR12/UrsinaForMobile/issues).

Happy coding and enjoy your new mobile app! 🎉📱✨
