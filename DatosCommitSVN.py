#!/usr/bin/env python
import os
import subprocess
import sys
import datetime
import os
import shutil
import fnmatch 
import string
import shutil
import zipfile
from pathlib import Path


# Carpeta de gemadesa
origen='D:\Yasmani\gemadesa\eclipse3.4-java\workspace'
nombreClase='UTD_Capter'
ext='.java'

path_list = [os.path.join(root, file) for root, _, files in os.walk(origen)
                                      for file in fnmatch.filter(files, nombreClase+ext)]
print(path_list)
rev_list=[]
reader= os.popen('svn log -v --limit 1 '+path_list[0])

for line in reader:
    print(line)
    if len(line.split('|'))== 4:
        rev_list.append(line.split('|'))
reader.close()
print(rev_list)