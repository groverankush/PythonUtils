# Program to get matching keys of all the values

import os
import xml.etree.ElementTree as ET

path = "C:\\Users\\ankush.grover\\Desktop\\strings"
os.chdir(path)

tree = ET.parse("strings.xml")
root = tree.getroot()

keys = open("keys.txt", 'w')
values = open("keys.txt", 'r')


dic = {}

for string in root.findall('string'):
    name = string.get('name')
    value = string.text
    dic[value.strip()] = name

for line in values.readlines():

    key = dic.get(line.strip())
    if key is None:
        key = "********"

    values.write(key + '\n')


# for string in root.findall('string'):
#     name = string.get('name')
#     value = string.text
#     names.write(name + '\n')
#     values.write(value + '\n')

names.close()
values.close()
