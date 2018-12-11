import os

files = os.listdir(os.curdir)
for file in files:
    if '.jpg' in file:
        newfile = file.replace('.jpg', '.png')
        os.rename(file, newfile)