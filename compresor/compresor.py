from pathlib import Path
from PIL import Image
import os
import sys

images_formats = ['jpg', 'png', 'jpeg']

images_path = Path.home() / 'Images'

os.system(f"mkdir {images_path / 'compressed'}")

compressed_path = images_path / 'compressed'

print("Se utilizara el fichero ~/Images/compressed")

files = [i.name for i in os.scandir(images_path) if i.is_dir() == False]

for i in files:
    name = i.split('.')[0]
    extension = i.split('.')[1]
   
    if extension in images_formats:
        with Image.open(images_path / i) as img:
            img.save(compressed_path / f"{name}.{extension}", quallity=60, optimize=True)
        os.system(f"rm {images_path / name}.{extension}")



# Con el metodo save y la propiedad quallity se puede comprimir la imagen
# y se puede aun mas con el metodo optimize=True

#img.save("pexels.jpg", quallity=60, optimize=True)

#img.show()
# Combertir 
# img.save('pexels.png', 'png')
#con el metodo rotate(angulo) se puede rotar la imagen
# con la propiedad size se puede acceder a los valores de ancho y alto de la imagen
# con el metodo rezize puedes cambiar el anchon y el alto de la imagen
# y con el metodo thumnail se puede reescalar la imagen conservando las propiedades
