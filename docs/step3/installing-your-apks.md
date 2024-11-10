# Ursina on Mobile - Step 3a: Installing your apks

First, make sure your android device is [connected to adb](https://www.guru99.com/adb-connect.html), with:
```bash
adb devices
```
Make sure you have only **one** connected device, or BundleTool will give you an error.

Then, do: 
```bash
java -jar Path\To\BundleTool\bundletool.jar install-apks --apks=.\dist\*.apks
```

And you have your app installed !!!

Welcome to the new era of ursina, the mobile era !!!

[Next -> (Step 4a - Watch logcat)](/docs/step4/watch-logcat.md)
