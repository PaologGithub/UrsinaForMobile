# Ursina on Mobile - Step 2a: Generating the aab

AAB is an Android App Bundle. This is what will permit you to deploy your app to the [Google Play Store](https://developers.connectycube.com/guides/uploading-android-app-to-store/). First, make sure you're in the [src directory](/src/) in terminal.

Then, do 
```bash
python setup.py bdist_apps
```

If you want to have a signed with certificate .aab, go to [Step 2a_cert: Generating the aab with certificate](generating-the-aab-with-cert.md)

[Next -> (Step 2b - Converting your aab to apks)](/docs/step2/converting-your-aab-to-apks.md)
