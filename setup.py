from setuptools import setup
import tomllib

from project.builder.commands import BuildAssetsCommand, BDistApps

content: dict = dict()
with open("project/settings.toml", "rb") as file:
    content = tomllib.load(file)

# [android] part
app_id: str            = content["android"]["id"]
app_version: str       = content["android"]["version"]
app_name_set: str      = content["android"]["name"]
app_icon: str          = content["android"]["icon"]
app_classifiers: list  = content["android"]["classifiers"]
# [application] part
app_name: str          = content["application"]["name"]
app_pyfile: str        = content["application"]["startfile"]
# [build] part
app_vercode: str       = content["build"]["vercode"]
app_platforms: list    = content["build"]["platforms"]
app_includes: list     = content["build"]["includes"]

# PRC Data
PRC_DATA = f'''
load-display pandagles2
aux-display pandagles

notify-level info
gl-debug true

android-app-id {app_id}
'''

# Main part
setup(
    name=app_name_set,
    version=app_version,

    options={
        'build_apps': {
            'application_id': app_id,

            'android_version_code': app_vercode,
			
			'platforms': app_platforms,

            'gui_apps': {
                app_name: app_pyfile,
            },
            'plugins': [
                # Use of pandagles2/pandagles instead of pandagl
                'pandagles2',
                'pandagles',
                'p3openal_audio',
            ],
            'include_patterns': app_includes,
            'extra_prc_data': PRC_DATA,

            'icons': {'*': app_icon},
        },
    },
    classifiers=app_classifiers,
    cmdclass={
        'build_assets': BuildAssetsCommand,
        'bdist_apps': BDistApps
    }
)
