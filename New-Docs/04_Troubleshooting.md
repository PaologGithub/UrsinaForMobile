# Troubleshooting ❓🛠️

This guide is designed to help you diagnose and resolve common issues when building, deploying, and running your Ursina mobile app.

---

## 1. General Issues

### **AAB Build Failures**
- **Problem:**  
  Errors during `python setup.py bdist_apps` execution.
- **Possible Causes & Solutions:**  
  - **Configuration Errors:**  
    Verify that all entries in your **src/setup.py** are correct (application name, version, application_id, etc.).
  - **Missing Dependencies:**  
    Ensure you have installed all required packages such as Protobuf and the correct version of Panda3D for Python 3.13.
  - **Python Version:**  
    Make sure you're using Python 3.13. Run `python --version` or `python3.13 --version` to confirm.

---

## 2. Signing & Keystore Issues 🔐

### **Keystore Not Found / Invalid Alias**
- **Problem:**  
  When signing your AAB, you encounter errors related to the keystore or alias.
- **Possible Causes & Solutions:**  
  - **Incorrect Path or Filename:**  
    Double-check the path and filename of your keystore.
  - **Alias Mismatch:**  
    Ensure that the alias provided in the signing command exactly matches the one in your keystore.
  - **Permissions:**  
    Verify that you have the necessary permissions to read the keystore file.

---

## 3. BundleTool & APKS Conversion Problems 🔄

### **APKS File Already Exists**
- **Problem:**  
  You receive an error message like:  
  ```
  [BT:1.17.1] Error: File './dist/app.apks' already exists.
  ```
- **Solution:**  
  Delete the existing `app.apks` file before running the command again:
  ```bash
  rm ./dist/app.apks
  ```

### **General BundleTool Errors**
- **Problem:**  
  BundleTool fails during conversion.
- **Possible Causes & Solutions:**  
  - **Incorrect AAB File:**  
    Verify that your AAB is properly built and located in the `./dist/` directory.
  - **Jar Path Issue:**  
    Make sure you are using the correct path to BundleTool’s jar file.
  - **Verbose Logs:**  
    Run BundleTool with `--verbose` to get more detailed error messages that can help in debugging.

---

## 4. Device & ADB Issues 📲

### **Device Not Recognized**
- **Problem:**  
  Your Android device is not listed when you run `adb devices`.
- **Possible Causes & Solutions:**  
  - **USB Debugging Disabled:**  
    Ensure that USB Debugging is enabled on your device. Follow [this guide](https://www.howtogeek.com/129728/how-to-enable-developer-options-menu-and-enable-usb-debugging-on-android/).
  - **Driver Issues (Windows):**  
    Install or update the necessary USB drivers.
  - **Cable/Connection:**  
    Verify your USB cable and try reconnecting the device.

### **Multiple Devices Connected**
- **Problem:**  
  ADB shows more than one connected device, which can cause installation conflicts.
- **Solution:**  
  Disconnect any extra devices or specify the device using ADB’s serial number:
  ```bash
  adb -s <device_serial> install <apk_file>
  ```

---

## 5. Logcat & Runtime Errors 🔍

### **No Log Output / Incomplete Logs**
- **Problem:**  
  Logcat does not show expected output or is cluttered.
- **Possible Solutions:**  
  - **Filtering Logs:**  
    Use filters to isolate logs for your app. For example:
    ```bash
    adb logcat -v brief -v color 'Panda3D:V' 'Python:V' 'threaded_app:V' 'AndroidRuntime:I' 'linker:W' '*:F'
    ```
  - **Clearing Logs:**  
    Clear old logs with:
    ```bash
    adb logcat -c
    ```

### **Runtime Crashes**
- **Problem:**  
  The app crashes immediately after launching.
- **Possible Causes & Solutions:**  
  - **Asset Issues:**  
    Ensure that all asset paths are correctly configured in **setup.py** and **setup_ursina_android.py**.
  - **Code Errors:**  
    Check the logcat output for Python errors or stack traces that indicate which part of the code is failing.
  - **Resource Optimization:**  
    Mobile devices have different performance characteristics. Review and optimize resource usage in your game.

---

## 6. Additional Tips & Resources

- **Documentation:**  
  Revisit the [Getting Started](01_Getting_Started.md) and [Build & Deployment](03_Build_and_Deployment.md) guides for detailed instructions.
- **GitHub Issues:**  
  If you’re still stuck, search for your issue or open a new issue on our [GitHub Issues page](https://github.com/ShivamKR12/UrsinaForMobile/issues).
- **Community Help:**  
  Consider asking for help in relevant developer communities or forums.

---

## Final Checklist ✅

- [ ] Verify Python and dependency installations.
- [ ] Confirm configuration in **setup.py** and **setup_ursina_android.py**.
- [ ] Ensure proper keystore and signing details (if signing is required).
- [ ] Check for a single connected device via ADB.
- [ ] Use verbose logging for detailed error information.
- [ ] Review logs with logcat for runtime issues.

---

By following this guide, you should be able to troubleshoot and resolve most common issues during your development and deployment process. If problems persist, please refer to our [GitHub Issues](https://github.com/ShivamKR12/UrsinaForMobile/issues) page for further assistance.

Happy troubleshooting! 🚀🔧📱
