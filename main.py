import pathlib
import argparse
from PIL import Image
from os import listdir
from os.path import isfile, join

def gatherFiles(path):
    fileFolder = []
    for f in listdir(path):
        if isfile(join(path, f)) == True:
            fileFolder.append(f)
    return fileFolder

def fileImgSorting(fileFolder):
    imgFiles = []
    for f in fileFolder:
        if pathlib.Path(f).suffix in [".png", ".jpg", ".jpeg"]:
            imgFiles.append(f)
    return imgFiles

def convertImg(newPath, imgFiles):
    convertedFiles = []
    for f in imgFiles:
        destination = pathlib.Path(f).with_suffix(".webp")
        image = Image.open(join(newPath, f))
        image.save(join(newPath, destination), format="webp")
        convertedFiles.append(destination)
    return convertedFiles

parser = argparse.ArgumentParser(description = "Convert copies of all .png, .jpg and .jpeg files to .webp. Use -s [source path] and -d [destination path].")

parser.add_argument("-s", "--source", help = "Source directory")
parser.add_argument("-d", "--destination", help = "Destination directory")

args = parser.parse_args()

if args.source != None and args.destination != None:
    convertImg(args.destination, fileImgSorting(gatherFiles(args.source)))
    print(f"Conversion complete, the new .webp images can be found at '{args.destination}'.")
else:
    print("Invalid source or/and destination.")