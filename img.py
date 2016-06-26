#!/usr/bin/env python3.5
import os, pprint, PIL.Image, sys, shutil

pre_dir = "."
post_dir = "./post"
print(str(sys.argv))

if (len(sys.argv) == 3):
  pre_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), sys.argv[1])
  post_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), sys.argv[2])

if (not os.path.isdir(pre_dir)):
  exit("import directory doesn't exist")

if (not os.path.isdir(post_dir)):
  print("Creating export directory.")
  os.mkdir(post_dir)

print("pre_dir: " + pre_dir + ", post_dir: " + post_dir + "\n")

for file in os.listdir(pre_dir):
  if (file.lower().endswith('jpg') or file.lower().endswith('jpeg')):
    original_file = os.path.join(pre_dir, file)
    print(original_file)
    img = PIL.Image.open(original_file)
    exif_data = img._getexif()
    name_list = exif_data[36867].split()
    new_name = name_list[0].replace(':', '-') + ' ' + name_list[1].replace(':', '.') + '.jpg'
    new_file = os.path.join(post_dir, new_name)
    print(new_file + "\n")
    shutil.copy(original_file, new_file)
