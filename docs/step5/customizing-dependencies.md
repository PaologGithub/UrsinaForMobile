[<- Back (Step 5 - Customizing your project)](/docs/step5/main.md)
# Ursina on Mobile - Customizing dependencies

If you need to add pypi dependencies, you can add them in [requirements.txt](/src/requirements.txt). **Do not remove anything already in it, or you'll break things.**

Sometimes, `python setup.py bdist_apps` can give you an error because of a dependencies. Make sure your dependency is for target `py3-none-any`, and is for python >=3.8.

If your dependency isn't for target `py3-none-any` (You can know this by going in the pypi page of your dependency, go to 'Download files' and watch if the .whl finishes by that), you're pretty f*cked up, so remove this dependency.

If your dependency isn't for python >=3.8 but for a greater version of python, you can try to extract your wheel like an zip archive, open `the_package-version.dist-info/METADATA` and change the Requires-Python attribute to be >=3.8, and then watch the logs to see any error, and patch it manually.
**This solution will take time, that's what I did to get ursina running on py3.8**