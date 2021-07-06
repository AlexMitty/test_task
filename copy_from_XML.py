# -*- coding: utf-8 -*-
import xml.dom.minidom as minidom
from shutil import copy2
from os import path, makedirs

def getFileXML(file_name):
    if len(file_name.getElementsByTagName('file')) !=0:
        return file_name.getElementsByTagName('file')
    else:
        print('There are not <file> tags in XML')
        return False
def copy_files(file):
        for attr in range(len(file)):
            dir = file[attr].getAttribute("source_path")
            fname = file[attr].getAttribute("file_name")
            destination = file[attr].getAttribute("destination_path")
            file_dir = path.normpath(path.join(dir,fname))
            try:
                if not path.exists(destination):
                    makedirs(destination)
                copy2(file_dir,destination)
                print(f'File {fname} successfully copied to {destination}')
            except FileNotFoundError:
                print(f'No such file {fname} in the directory {dir}')
            
with minidom.parse('testxml.xml') as dom:
    if getFileXML(dom)!= False:
        file = getFileXML(dom)
        copy_files(file)
