from setuptools import setup

# Set renderer to pandagles2 (shaders) with pandagles (FFP) as fallback
PRC_DATA = '''
load-display pandagles2
aux-display pandagles

notify-level info
gl-debug true
'''

setup(
    # The name of the app
    name='My ursina game',
    # The version of the app
    version='0.0.0',
    options={
        'build_apps': {
            # Uniquely identifies the app
            'application_id': 'your.company.app.name',

            # Update this for every version uploaded to the Play Store
            'android_version_code': 0,
			
			'platforms': ['android'],

            # Tell here the entry py file. It will be executed at the launch of the app
            # In this file will be your ursina code
            'gui_apps': {
                'mygame': 'game/__main__.py',
            },
            'plugins': [
                # Note use of pandagles2/pandagles instead of pandagl
                'pandagles2',
                'pandagles',
                'p3openal_audio',
            ],
            # Here put all the resources you need
            'include_patterns': [
				'game/**',
                # Don't remove this, it is to include ursina assets
                'ursina_assets/**',
                '**/*.png',
                '**/*.jpg',
                '**/*.egg',
            ],
            'extra_prc_data': PRC_DATA,

            # Here, you can change the icon
            'icons': {'*': 'logo.png'},
        },
    },
    # Choosing a classifier in the Games category makes it marked a "Game"
    classifiers=['Topic :: Games/Entertainment'],
)
