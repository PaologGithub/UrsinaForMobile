# Ursina on Mobile - Step 2a_cert: Generating the aab with cert

AAB is an Android App Bundle. This is what will permit you to deploy your app to the [Google Play Store](https://developers.connectycube.com/guides/uploading-android-app-to-store/). First, make sure you're in the [src directory](/src/) in terminal.

Then, generate a certificate with openssl:
```bash
openssl genpkey -algorithm RSA -aes256 -out private.pem
openssl req -new -x509 -sha256 -days 365 -key private.pem > cert.pem
```

Then, modify [setup.py](/src/setup.py) to include this option:
```python
from setuptools import setup

# Prc data

setup(
    # ...
    options={
        'build_apps': {
            # ...
        },
        'bdist_apps': {
            'signing_certificate': 'cert.pem',
            'signing_private_key': 'private.pem',
            # optional: Panda will otherwise ask passphrase on command-line
            #'signing_passphrase': 'panda3d_is_cool',
        },
    },
    # ...
)

```
```bash
python setup.py bdist_apps
```

[Next -> (Step 2b - Converting your aab to apks)](/docs/step2/converting-your-aab-to-apks.md)