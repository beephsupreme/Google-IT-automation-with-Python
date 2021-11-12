#!/usr/bin/env python3
import PIL.Image
import os, sys

path = "supplier-data/images/"
pictures = os.listdir(path)

for pic in pictures:
  if pic.endswith('tiff'):
    #grab the picture name without the .tiff extension
    file_name = os.path.splitext(pic)[0]
    outfile = "supplier-data/images/" + file_name + ".jpeg"
    try:
      PIL.Image.open(path + pic).convert("RGB").resize((600,400)).save(outfile,"JPEG")
    except IOError:
      print("cannot convert", pic)

