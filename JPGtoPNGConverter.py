import sys
import os
from PIL import Image



# grab 1st & 2nd argument

starting_folder = f"{sys.argv[1]}/"
ending_folder = f"{sys.argv[2]}/"

# check if new folder exists, if not, create it.

if not os.path.exists(ending_folder):
    os.makedirs(ending_folder)

# loop through the starting folder
# convert images to png
# save images to the new folder

for filename in os.listdir(starting_folder):
    img = Image.open(f"{starting_folder}{filename}")
    img_root = os.path.splitext(filename)[0]
    img.save(f"{ending_folder}{img_root}.png", "PNG")
