# Ursina on Mobile - Step 2b: Converting your aab to apks

An APKS is some apk files, to help supporting multiple android architectures. To convert your aab to apks, check where you have installed BundleTool, as said in the [Step 1d - Installing android dependencies](/docs/step1/installing-android-dependencies.md). Then, do this:

```bash
java -jar Path\To\BundleTool\bundletool.jar build-apks --bundle .\dist\*.aab --output .\dist\app.apks --verbose
```
If you have already build once your app, BundleTool will give you this error:
`[BT:1.17.1] Error: File '.\dist\app.apks' already exists.`

To repair it, just delete `dist\app.apks`

And you finished building your application !!! 

[Next -> (Step 3a - Installing your apks)](/docs/step3/installing-your-apks.md)
