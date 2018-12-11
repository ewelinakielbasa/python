import os

path1 = 'D:/Python/dev'

def displayFolders(folder):
    print(folder)
    filesList = os.listdir(folder)

    for i in filesList:
        path2 = os.path.join(folder, i)
        if os.path.isdir(path2):
            displayFolders(path2)
        else:
            print(path2)

displayFolders(path1)