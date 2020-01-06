import os

def getFilesFromFolder(dir):
    files = []
    count = 0
    for filename in os.listdir(dir):
        files.append([])
        for j in os.listdir(dir + '/' + filename):
            files[count].append(dir + '/' + filename + '/' + j)
        count += 1
    return files


def getFileNames(dir):
    files = []
    for filename in os.listdir(dir):
        files.append(filename)
    return files

