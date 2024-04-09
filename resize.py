
import os
import sys
from pathlib import Path
from PIL import Image

IMG_EXT = [".jpg", ".jpeg", ".png"]
WORKDIR = "/mnt/c/Users/bapti/Documents/Wordpress-img/"

MAX_SIZE = int(sys.argv[1]) #Max width or height dimension
QUALITY = int(sys.argv[2]) # % quality

def get_files():         
        target_dir = os.listdir(WORKDIR)
        for file in target_dir:
            if Path(file).suffix in IMG_EXT:                
                resize_picture(file, int(is_portrait(file)))
            elif Path(file).mkdir:
                pass
            else:
                print(f"img format: {Path(file)} not accepted")

def is_portrait(file) -> bool:
    im = Image.open(WORKDIR + file)
    return bool(im.size[0] <= im.size[1])

def resize_picture(file, format: int):
    im = Image.open(WORKDIR + file)
    ratio =  MAX_SIZE / im.size[format]    
    resized_im = im.resize((round(im.size[0]*ratio), round(im.size[1]*ratio)))
    resized_im.save(WORKDIR + f"{Path(file).stem}-resized{Path(file).suffix}")
    compress_image((WORKDIR + f"{Path(file).stem}-resized{Path(file).suffix}"), WORKDIR + "compressed-img/" + f"{Path(file).stem}-compress{Path(file).suffix}") 
    os.remove(WORKDIR + f"{Path(file).stem}-resized{Path(file).suffix}")
    os.rename(WORKDIR + file, WORKDIR + "original-img/" + file)


def compress_image(source_path, dest_path):
    with Image.open(source_path) as img:
        img.save(dest_path, optimize=True, quality=QUALITY)
        print(f"=== Fichier: {os.path.basename(dest_path)}\nSize: {img.size}   // Nouveau poid: {int((os.path.getsize(dest_path))/1000)} \n")

def main():
    get_files()

if __name__ == "__main__":
    main()