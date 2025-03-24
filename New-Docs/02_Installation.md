 Installation 📲

This guide shows you how to install your already built app (APKS) on your Android device.

---

### 1. Connect Your Android Device

- **Enable Developer Options & USB Debugging:**  
  Follow [this guide](https://www.howtogeek.com/129728/how-to-enable-developer-options-menu-and-enable-and-usb-debugging-on-android/) if needed.
  
- **Connect via USB:**  
  Verify your device is connected:
  
  ```bash
  adb devices
  ```
  
  *Ensure only one device is connected to avoid conflicts.*

---

### 2. Install the App APKS

Use BundleTool to install your prebuilt APKS:

1. **Run BundleTool:**

   Replace `/path/to/bundletool.jar` with the actual path to BundleTool:

   ```bash
   java -jar /path/to/bundletool.jar install-apks --apks=./dist/app.apks
   ```

2. **Launch the App:**

   Once installation is complete, locate your app icon on your device and tap to launch.

---

### 3. Debugging (Optional)

- **View Logs:**  
  To troubleshoot any issues, run:

  ```bash
  adb logcat -v brief -v color 'Panda3D:V' 'Python:V' 'threaded_app:V' 'AndroidRuntime:I' 'linker:W' '*:F'
  ```

- **Clear Logs:**

  ```bash
  adb logcat -c
  ```

---

### Final Checklist ✅

- [ ] Device connected and recognized by ADB.
- [ ] APKS installed via BundleTool.
- [ ] App launches successfully.
- [ ] Debug logs verified (if needed).

---

Happy installing! 🎉📱
