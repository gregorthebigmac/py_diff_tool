import os

root_dir = raw_input("What dir?")
dir_path, dirs, filenames = os.walk(root_dir)
print(dir_path)
print("contents:")
print("dirs:")
print(dirs)
print("files:")
print(filenames)


