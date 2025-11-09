from hashlib import sha256
import os
import json
from pathlib import Path
import zlib
import random

def setup_assets():
    game_assets_path: Path = Path("assets").absolute() / "game_assets"
    ursina_assets_path: Path = Path("assets").absolute() / "ursina_assets"


    generated: dict[str, dict[str, dict[str, str]]] = {
        "ursina_assets": process_dir(ursina_assets_path),
        "game_assets": process_dir(game_assets_path)
    }

    json_data = json.dumps(generated, indent=4, sort_keys=True).encode("utf-8")
    with open("assets/assets.gen", "wb") as file:
        compressed = zlib.compress(json_data)
        file.write(compressed)

    # DEBUG
    with open("assets/assets_DEBUG.json", "wb") as file:
        file.write(json_data)

def setup_asset(path: Path) -> dict[str, str]:
    h256 = sha256()
    with open(path, "rb") as f:
        h256.update(f.read())

    return {
        "dir": str(path.relative_to(Path("assets").absolute())).replace("\\", "/"),
        "sha": h256.hexdigest() 
    }

def process_dir(dir: Path, folder_data = None) -> dict[str, dict[str, str]]: # type: ignore
    if folder_data == None:
        folder_data: dict[str, dict[str, str]] = {}

    for str_path in os.listdir(dir):
        path: Path = (dir / Path(str_path)).absolute()
        if os.path.isfile(path):
            name = str_path.replace(".", "_") + "-" + str(random.randint(0, 100))
            folder_data[name] = setup_asset(Path(path))
        else:
            process_dir(path, folder_data)
    
    return folder_data