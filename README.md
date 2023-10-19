# WebP Batch Converter

This Python script converts a folder of images to WebP format. Supported formats as input are **.png**, **.jpg** and **.jpeg**. Note that the script itself recognises the correct suffix and will only create new copies of those files at a given directory. 

## Setup
Install [Python](https://www.python.org/downloads/), then run:
```
pip install Pillow
```
## How to run
```
python main.py -s [your source directory] -d [your destination directory]
```
You can also run the script with `-h` for help.
