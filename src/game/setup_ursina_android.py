import os
from direct.stdpy.file import open, exists

app_id = "your.company.app.name"
assets = ['arrow.ursinamesh', 'arrow_down.png', 'arrow_right.png', 'bag.png', 'Bitstream Vera License.txt', 'bow_arrow.png', 'brick.png', 'circle.blend', 'circle.png', 'circle.ursinamesh', 'circle_outlined.png', 'cog.png', 'cube.blend', 'cube.ursinamesh', 'cube_uv_top.blend', 'cube_uv_top.ursinamesh', 'cursor.png', 'diamond.ursinamesh', 'file_icon.png', 'folder.png', 'gem.png', 'grass.png', 'grass_tintable.png', 'heightmap_1.png', 'horizontal_gradient.png', 'icosphere.blend', 'icosphere.ursinamesh', 'items.psd', 'LICENSE.txt', 'line.ursinamesh', 'noise.png', 'noise.wav', 'OpenSans-Regular.ttf', 'orb.png', 'perlin_noise.png', 'plane.blend', 'plane.ursinamesh', 'quad.blend', 'quad.ursinamesh', 'radial_gradient.png', 'rainbow.png', 'reflection_map_3.jpg', 'scale_gizmo.ursinamesh', 'shore.jpg', 'sine.wav', 'sky_default.jpg', 'sky_dome.blend', 'sky_dome.ursinamesh', 'sky_sunset.jpg', 'sphere.blend', 'sphere.ursinamesh', 'square.wav', 'sword.png', 'test_tileset.png', 'tilemap_test_level.png', 'triangle.wav', 'untitled_scene[0,0].csv', 'untitled_scene[1,0].csv', 'untitled_scene[1,1].csv', 'untitled_scene[1,2].csv', 'untitled_scene[2,0].csv', 'untitled_scene[2,3].csv', 'ursina.ico', 'ursina.png','ursina_logo.png', 'ursina_wink_0000.png', 'ursina_wink_0001.png', 'VeraMono.ttf', 'vertical_gradient.png', 'vignette.png', 'white_cube.png', 'wireframe_cube.ursinamesh', 'wireframe_quad.ursinamesh', '_bat_to_exe.bat'] 


def setup_ursina_android():
    # Step 0: Change the path
    os.chdir(f"/data/data/{app_id}/files/")

    # Step 1: Check if there is ursina assets
    missing_assets = []
    for asset in assets:
        src_path = f"/android_asset/ursina_assets/{asset}"
        if not exists(src_path):
            missing_assets.append(asset)
    
    if missing_assets:
        return  # Stop setup if files are missing

    # Step 2: Copy the ursina assets
    for asset in assets:
        src_path = f"/android_asset/ursina_assets/{asset}"
        dest_path = os.path.join(os.getcwd(), os.path.basename(asset))

        with open(src_path, 'rb') as src_file, open(dest_path, 'wb') as dest_file:
            dest_file.write(src_file.read())
    