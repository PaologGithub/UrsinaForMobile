[<- Back (Step 5 - Customizing your project)](/docs/step5/main.md)
# Ursina on Mobile - Customizing android app 

To customize your android app, all will be do in [setup.py](/src/setup.py).

I will go through all the available settings, and tell you how you can customize them.

* `setup/name :` Represent the name of the package. It won't do much to your application

* `setup/version :` Represent the version of your application. You can see the version by opening android settings, go to Application > Your Application, and you'll see `version THE_VERSION`

* `setup/build_apps/application_id :` Represent your application id. Normally, it is `com.company.application_name`. For me, I like to put `pao.paolog.android.my_ursina_game`. Make sure to change [setup_ursina_android at line 5](/src/game/setup_ursina_android.py) to make that the `app_id` is the same as your application_id

* `setup/build_apps/android_version_code :` This is the version code for google play store. Each time before uploading your game to the play store, you'll need to increment this variable by one.

* `setup/build_apps/gui_apps :` Represent your gui apps. The name of the apps (Example: mygame) are the ones that name the application in your android launcher. Make sure you **don't** put a space in the name. I didn't try for Maj, so please try it and tell me.

* `setup/build_apps/include_patters :` This is to add assets to your game. Please refer to [Customizing Assets](customizing-assets.md).

* `setup/build_apps/icons :` Is the icon that will be displayed as your app icon. Make sure that is a square, not rectangle (200x200 is good, 201x200 is bad)

And that's pretty much.