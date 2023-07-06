# Script to find specified file with given name
# DnsLpt 19/06/23

import os
import glob

directory = os.getcwd() + '/**'
file_extension = '*'
word = str(input("What is the file you're looking for?"))
counter = 0;

dups = []

files = glob.glob(os.path.join(directory, file_extension), recursive = True)

#print(files)

for file_path in files:
    if(os.path.basename(file_path) == word):
        counter +=1
        print(file_path)
        
print("found " + str(counter) + " files")