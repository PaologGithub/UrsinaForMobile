import os
import sys
from direct.stdpy.file import open, exists

app_id = 'com.example.mygame'
assets = ['arrow.ursinamesh', 'arrow_down.png', 'arrow_right.png', 'bag.png', 'Bitstream Vera License.txt', 'bow_arrow.png', 'brick.png', 'circle.blend', 'circle.png', 'circle.ursinamesh', 'circle_outlined.png', 'cog.png', 'cube.blend', 'cube.ursinamesh', 'cube_uv_top.blend', 'cube_uv_top.ursinamesh', 'cursor.png', 'diamond.ursinamesh', 'file_icon.png', 'folder.png', 'gem.png', 'grass.png', 'grass_tintable.png', 'heightmap_1.png', 'horizontal_gradient.png', 'icosphere.blend', 'icosphere.ursinamesh', 'items.psd', 'LICENSE.txt', 'line.ursinamesh', 'noise.png', 'noise.wav', 'OpenSans-Regular.ttf', 'orb.png', 'perlin_noise.png', 'plane.blend', 'plane.ursinamesh', 'quad.blend', 'quad.ursinamesh', 'radial_gradient.png', 'rainbow.png', 'reflection_map_3.jpg', 'scale_gizmo.ursinamesh', 'shore.jpg', 'sine.wav', 'sky_default.jpg', 'sky_dome.blend', 'sky_dome.ursinamesh', 'sky_sunset.jpg', 'sphere.blend', 'sphere.ursinamesh', 'square.wav', 'sword.png', 'test_tileset.png', 'tilemap_test_level.png', 'triangle.wav', 'untitled_scene[0,0].csv', 'untitled_scene[1,0].csv', 'untitled_scene[1,1].csv', 'untitled_scene[1,2].csv', 'untitled_scene[2,0].csv', 'untitled_scene[2,3].csv', 'ursina.ico', 'ursina.png','ursina_logo.png', 'ursina_wink_0000.png', 'ursina_wink_0001.png', 'VeraMono.ttf', 'vertical_gradient.png', 'vignette.png', 'white_cube.png', 'wireframe_cube.ursinamesh', 'wireframe_quad.ursinamesh', '_bat_to_exe.bat'] 
game_assets = []
game_assets_src_dir = None

def setup_ursina_android():
    if sys.platform == 'android':
        # Step 0: Change the path
        os.chdir(f"/data/data/{app_id}/files/")

        copy_ursina_assets()

        copy_game_assets()

def copy_ursina_assets():
    # Step 1: Check if there is ursina assets
    missing_assets = []
    for asset in assets:
        src_path = f"/android_asset/ursina_assets/{asset}"
        dest_path = os.path.join(os.getcwd(), os.path.basename(asset))
        if not exists(dest_path):
            missing_assets.append(asset)
    
    if missing_assets:
        # Step 2: Copy the missing assets
        for asset in missing_assets:
            src_path = f"/android_asset/ursina_assets/{asset}"
            dest_path = os.path.join(os.getcwd(), os.path.basename(asset))

            with open(src_path, 'rb') as src_file, open(dest_path, 'wb') as dest_file:
                dest_file.write(src_file.read())

def copy_game_assets():
    if game_assets_src_dir:
        # Step 3: Check if there is your game assets
        my_missing_assets = []
        for asset in game_assets:
            src_path = f"/android_asset/{game_assets_src_dir}/{asset}"
            dest_path = os.path.join(os.getcwd(), os.path.basename(asset))
            if not exists(dest_path):
                my_missing_assets.append(asset)
        
        if my_missing_assets:
            # Step 4: Copy the your game assets
            for asset in game_assets:
                src_path = f"/android_asset/{game_assets_src_dir}/{asset}"
                dest_path = os.path.join(os.getcwd(), os.path.basename(asset))

                with open(src_path, 'rb') as src_file, open(dest_path, 'wb') as dest_file:
                    dest_file.write(src_file.read())