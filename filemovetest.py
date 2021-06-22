import os
import glob

file_list = glob.glob("*")
ext_set = set()

for file in file_list:
    ext = file.split(sep=".")
    try:
        ext_set.add(ext[1])
    except IndexError:
        continue


def create_dirs():
    for dir in ext_set:
        try:
            os.makedirs(dir + "_files")
        except FileExistsError:
            continue


def arrange_files():
    for file in file_list:
        fextension = file.split(sep=".")
        try:
            os.rename(file, fextension[1] + "_files/" + file)
        except (OSError, IndexError):
            continue


create_dirs()
arrange_files()
