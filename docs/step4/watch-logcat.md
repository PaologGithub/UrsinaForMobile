# Ursina on Mobile - Step 4a: Watch logcat

You can watch your application logs with logcat. First, make sure you have your android device connect to adb. Then, you can watch the logs of your application with this:
```bash
adb.exe logcat -v brief -v color 'Panda3D:V' 'Python:V' 'threaded_app:V' 'AndroidRuntime:I' 'linker:W' '*:F'
```
All your applications log will be there. You can, if you want, make your own log with:
```python
# Yeah, seriously, print works... What did you think?
# Did you really think it will be difficult to make logs?
# I don't even know what I put that here.
# I don't even know why I didn't put step4 in step3, because step4 has nothing to say.
# Seriously, I put a whole step just for 10 lines of instructions...

# But thanks for reading this :,)
# And thanks for trying my project !!!
print("This will be showed in logcat")
```

If your logcat is starting to be messy, clear it with:
```bash
adb logcat -c
```

[Next -> (Step 5 - Customizing your project)](/docs/step5/main.md)