# Build & Deployment 🚀

Learn how to build your Android app, sign it if necessary, convert it to APKS, and deploy it.

---

### 1. Build Your Android App Bundle (AAB)

1. **Navigate to the Source Directory:**

   ```bash
   cd src
   ```

2. **Generate the AAB:**

   Run the build command:

   ```bash
   python setup.py bdist_apps
   ```

   *Your AAB will be located in the `./dist/` directory.*

---

### 2. (Optional) Sign Your AAB 🔐

If you plan to distribute your app through the Play Store, signing is necessary.

1. **Create a Keystore (if you don't have one):**

   ```bash
   keytool -genkey -v -keystore my-release-key.keystore -alias my_alias -keyalg RSA -keysize 2048 -validity 10000
   ```

2. **Sign the AAB:**

   Replace `your_app_bundle.aab` with your actual AAB filename:

   ```bash
   jarsigner -verbose -sigalg SHA256withRSA -digestalg SHA-256 -keystore my-release-key.keystore ./dist/your_app_bundle.aab my_alias
   ```

---

### 3. Convert AAB to APKS 🔄

Use BundleTool to convert your AAB into installable APKS.

1. **Run BundleTool:**

   ```bash
   java -jar /path/to/bundletool.jar build-apks --bundle ./dist/*.aab --output ./dist/app.apks --verbose
   ```

2. **Troubleshoot:**

   If an error indicates that `app.apks` already exists, remove it:

   ```bash
   rm ./dist/app.apks
   ```

   Then, re-run the BundleTool command.

---

### 4. Deploy the App (Overview)

After building and converting your app, you can then use the **Installation** guide (see **02_Installation.md**) to deploy the app to your device.

---

### 5. Troubleshooting & Tips 🔍

- **AAB Build Issues:**  
  Verify your `setup.py` configuration and that all dependencies are installed.
  
- **Signing Problems:**  
  Ensure your keystore and alias details match the signing command.
  
- **APKS Conversion:**  
  Confirm that the AAB is correctly built and there are no leftover APKS files in the `./dist/` directory.
  
- **Device Connectivity:**  
  Check that only one device is connected via ADB.

---

### Final Checklist ✅

- [ ] AAB generated using `python setup.py bdist_apps`.
- [ ] AAB signed (if necessary).
- [ ] APKS generated via BundleTool.
- [ ] Troubleshooting steps completed for any errors.
- [ ] Ready for installation using the separate Installation guide.

---

Congratulations! You’ve completed the build and deployment process. For installation details, please refer to the **02_Installation.md** guide.

Happy coding and deploying! 🎉🚀📱
