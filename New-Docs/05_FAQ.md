# FAQ ❓

Welcome to the Frequently Asked Questions section! Here you'll find answers to common questions about setting up, building, and deploying your Ursina mobile app. If you need further assistance, please check our [GitHub Issues](https://github.com/ShivamKR12/UrsinaForMobile/issues) page.

---

## General Questions

### **Q: Why do I need Python 3.13?**  
**A:** Python 3.13 is required for compatibility with the latest releases of Panda3D and other dependencies in this project. It ensures you have the most up-to-date features and bug fixes.  
*See [Getting Started](01_Getting_Started.md) for more details.*

---

### **Q: What if I encounter errors during the AAB build?**  
**A:**  
- **Check Configuration:** Ensure your **src/setup.py** has the correct settings (application name, version, application_id, etc.).  
- **Dependencies:** Verify that all required packages (e.g., Protobuf, Panda3D) are installed for Python 3.13.  
- **Python Version:** Run `python --version` or `python3.13 --version` to confirm you’re using the correct version.  
*For more troubleshooting, refer to [Troubleshooting](04_Troubleshooting.md).*

---

### **Q: How do I update or add new dependencies?**  
**A:**  
- Open the **src/requirements.txt** file.  
- Add any additional dependencies ensuring they are compatible with Python 3.13 and target `py3-none-any`.  
- Run:  
  ```bash
  python -m pip install -r src/requirements.txt
  ```  
*For more details, see [Getting Started](01_Getting_Started.md).*

---

## Build & Deployment

### **Q: What should I do if the APKS file already exists?**  
**A:**  
- Delete the existing file using:  
  ```bash
  rm ./dist/app.apks
  ```  
- Then re-run the BundleTool command in the [Build & Deployment](03_Build_and_Deployment.md) guide.

---

### **Q: Do I need to sign my AAB?**  
**A:**  
- **For Testing:** Signing is optional.  
- **For Distribution (Google Play):** Yes, you must sign your AAB using a valid keystore.  
*Refer to the [Build & Deployment](03_Build_and_Deployment.md) guide for instructions on signing your AAB.*

---

## Device & Installation

### **Q: My device isn’t recognized by ADB. What should I do?**  
**A:**  
- **Enable USB Debugging:** Follow [this guide](https://www.howtogeek.com/129728/how-to-enable-developer-options-menu-and-enable-usb-debugging-on-android/).  
- **Check Connections:** Verify that your USB cable works and that only one device is connected.  
- **Update Drivers:** (Windows users) Ensure that the appropriate drivers are installed.

---

### **Q: How can I view detailed logs to debug my app?**  
**A:**  
- Use **Logcat** with filtering options:  
  ```bash
  adb logcat -v brief -v color 'Panda3D:V' 'Python:V' 'threaded_app:V' 'AndroidRuntime:I' 'linker:W' '*:F'
  ```  
- Clear previous logs with:  
  ```bash
  adb logcat -c
  ```

---

## Miscellaneous

### **Q: Where can I get further help if my issue isn’t covered here?**  
**A:**  
- Visit our [GitHub Issues](https://github.com/ShivamKR12/UrsinaForMobile/issues) page to search for similar problems or to open a new issue.  
- Join community forums or chat groups related to Ursina and mobile game development.

---

If you have any more questions or need additional clarification, feel free to reach out through our GitHub or community channels. Happy coding and enjoy building your mobile game! 🎮📱✨
