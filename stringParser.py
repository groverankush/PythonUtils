# This is to parse all the strings in string file. This is created in this project
# to reduce the effort of creating new project

import os
import xml.etree.ElementTree as ET

path = "/home/emp272/Desktop"
os.chdir(path)

tree = ET.parse("strings.xml")
root = tree.getroot()

names = open("names.txt", 'w')
values = open("values.txt", 'w')

for string in root.findall('string'):
    name = string.get('name')
    value = string.text
    names.write(name+'\n')
    values.write(value+'\n')

names.close()
values.close()


