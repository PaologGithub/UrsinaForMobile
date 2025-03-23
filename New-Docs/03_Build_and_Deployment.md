# Build and Deployment

Follow these steps to build your Ursina game for Android:

## Configuring Your Android Project

- Refer to the [Android SDK documentation](https://developer.android.com/studio) for detailed setup instructions.
- Update configuration files (e.g., `build.gradle`) as necessary.

## Packaging Your Game

1. Run the build script:
   ```bash
   python build_android.py
   ```
2. Locate the generated APK in the `build/` directory.
3. Install the APK on your Android device:
   ```bash
   adb install build/your_game.apk
   ```

## Troubleshooting Build Issues

- Ensure that your Android SDK path is correctly set.
- Verify that all dependencies are installed.
