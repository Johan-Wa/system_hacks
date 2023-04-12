from pathlib import Path
import os 

downloads_path = Path.home() / "Descargas"
images_path = Path.home() / "Images"
images_formats = ('jpg','png','jpeg')

files = [i.name for i in os.scandir(downloads_path) if i.is_dir() == False]

for i in files:
    name = i.split(".")[0]
    extension = i.split(".")[1]
    if extension in images_formats:
        os.system(f"mv {downloads_path / name}.{extension} {images_path}")
