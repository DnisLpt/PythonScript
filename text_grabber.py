# Script to find specified text in files
# DnsLpt 19/06/23

import os
import glob

directory = os.getcwd() + '/**'
file_extension = '*.java'
word = str(input("What is the word you're looking for?"))

dups = []

files = glob.glob(os.path.join(directory, file_extension), recursive = True)

#print(files)

for file_path in files:
    with open(file_path, 'r') as file:
        file_contents = file.read()
        linenum = 1;
        for line in file_contents.splitlines():
            if(word in line):
                print("Document: " + file_path)
                print("Line: " + line + " line number: ")
                print(linenum)
            linenum +=1
        
        
#Check only if exists, its faster but doesnt tell you the line
        #if("product" in file_contents):
        #    print(file_path)
    