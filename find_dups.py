# Script to find java classes with the same name
# DnsLpt 19/06/23

import os
import glob

def get_final(strin):
    return (strin.split('\\')[-1])

def already_exists(name, lst):
    for el in lst:
        for el2 in el:
            lastEl = get_final(el2)
            basename = get_final(name)
            if(basename == lastEl):
                el.append(name)
                return
    lst2 = [name]
    lst.append(lst2)

directory = os.getcwd() + '/**'
file_extension = '*.java'

dups = []

files = glob.glob(os.path.join(directory, file_extension), recursive = True)

#print(files)

for file_path in files:
    already_exists(file_path, dups)
     
     
for element in dups:
    if len(element) > 1 :
        print("Duplicated files in : ")
        for eli in element:
            print(eli)