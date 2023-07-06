# Script to replace DEV env to PROD env nomenclature
# DnsLpt 19/06/23

import os
import glob

directory = os.getcwd() + '/**'
file_extension = '*.txt'

old_text = 'DEV '
new_text = 'PROD '

files = glob.glob(os.path.join(directory, file_extension), recursive = True)

print(files)

for file_path in files:
    with open(file_path, 'r') as file:
        file_contents = file.read()
    new_contents = file_contents.replace(old_text,new_text)
    
    with open(file_path, 'w') as file:
        file.write(new_contents)
        print('checked file: ' + file_path)
        

#Only the name -> os.path.basename(file_path)