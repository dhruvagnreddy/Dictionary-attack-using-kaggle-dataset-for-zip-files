import glob
import os

files_path = 'bruteforce-database'
files = glob.glob(os.path.join(files_path,'*.txt'))


with open("result.txt", "wb") as outfile:
    for f in files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
