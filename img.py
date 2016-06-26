#!/usr/bin/env python3.5

import os
import pprint
import PIL.Image
import sys

pre_dir = ""
post_dir = ""
print(str(sys.argv))

if (len(sys.argv) == 3):
  pre_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), sys.argv[1])
  post_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), sys.argv[2])

print("pre_dir: " + pre_dir)
print("post_dir: " + post_dir)
print()

for file in os.listdir(pre_dir):
    path = os.path.join(pre_dir, file)
    print(path)
    img = PIL.Image.open(path)
    exif_data = img._getexif()
    name_list = exif_data[36867].split()
    print(name_list)
    new_name = name_list[0].replace(':', '-') + ' ' + name_list[1].replace(':', '.') + '.jpg'
    print(new_name + "\n")
