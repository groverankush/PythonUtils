import os
import xml.etree.ElementTree as ET

path = "/home/emp272/Desktop"
os.chdir(path)

tree = ET.parse("chinese.xml")
root = tree.getroot()

keys = open("keys.txt", 'r')
names = open("names.txt", 'w')
values = open("values.txt", 'w')

dic = {}

for string in root.findall('string'):
    dic[string.get('name')] = string.text

for line in keys.readlines():

    value = dic.get(line.strip())
    if value is None:
        value = "********"

    values.write(value + '\n')

names.close()
values.close()
