
from lib2to3.fixes.fix_methodattrs import MAP
import os
import sys
from pathlib import Path
from PIL import Image
from moviepy.editor import VideoFileClip

IMG_EXT = [".jpg", ".jpeg", ".png", ".avif"]
VIDEO_EXT = [".mp4", ".mov"]
WORKDIR = "/mnt/c/Users/bapti/Documents/Wordpress-img/"

    
def get_files(): 
        print("== Images ==")
        longueur = int(input("Quelle est la nouvelle longueur la plus grande ?"))
        quality = int(input("Images: Quelle qualité appliquer ? (%):"))  
        print("== Video ==")
        largeur = int(input("Quelle est la nouvelle width ?:"))    
        target_dir = os.listdir(WORKDIR)
        for file in target_dir:
            if Path(file).suffix in IMG_EXT:                
                resize_picture(file, int(is_portrait(file)), longueur, quality)
            elif Path(file).suffix in VIDEO_EXT:
                resize_movie(file, largeur)
            elif Path(file).mkdir:
                pass
            else:
                print(f"img format: {Path(file)} not accepted")

def is_portrait(file) -> bool:
    im = Image.open(WORKDIR + file)
    return bool(im.size[0] <= im.size[1])

def resize_picture(file, format, distance, quality):
    im = Image.open(WORKDIR + file)
    ratio =  distance / im.size[format]    
    resized_im = im.resize((round(im.size[0]*ratio), round(im.size[1]*ratio)))
    resized_im.save(WORKDIR + f"{Path(file).stem}-resized{Path(file).suffix}")
    compress_image((WORKDIR + f"{Path(file).stem}-resized{Path(file).suffix}"), WORKDIR + "compressed-img/" + f"{Path(file).stem}-compress{Path(file).suffix}", quality) 
    os.remove(WORKDIR + f"{Path(file).stem}-resized{Path(file).suffix}")
    os.rename(WORKDIR + file, WORKDIR + "original-img/" + file)

def resize_movie(file, largeur):
    hauteur = int(largeur / 1.777777777777778) #16:9 format
    video = VideoFileClip(WORKDIR + file)
    resized_video = video.resize((largeur, hauteur))
    output_file = f"{WORKDIR}resize-video/{Path(file).stem}-resized.mp4"
    resized_video.write_videofile(output_file, codec='libx264')
    os.rename(WORKDIR + file, WORKDIR + "original-video/" + file)

def compress_image(source_path, dest_path, quality):
    with Image.open(source_path) as img:
        img.save(dest_path, optimize=True, quality=quality)
        print(f"=== Fichier: {os.path.basename(dest_path)}\nSize: {img.size}   // Nouveau poid: {int((os.path.getsize(dest_path))/1000)} \n")

def main():
    get_files()

if __name__ == "__main__":
    main()