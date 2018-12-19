import os
import xml.etree.ElementTree as ET

path = "C:\\Users\\ankush.grover\\Desktop\\strings\\default"
os.chdir(path)

tree = ET.parse("hindi.xml")
eTree = ET.parse("english.xml")

root = tree.getroot()
eRoot = eTree.getroot()

keys = open("keys.txt", 'w')
english = open("english.txt", 'wb')
hindi = open("hindi.txt", 'wb')

dic = {}

for string in root.findall('string'):
    dic[string.get('name')] = string.text

for string in eRoot.findall('string'):
    key = string.get('name')
    keys.write(key + "\n")
    eng = string.text + '\n'
    english.write(eng.encode("utf-8"))

    # soup.encode("utf-8")
    value = dic.get(key)
    if value is None:
        value = "********"

    value += "\n"
    hindi.write(value.encode("utf-8"))

keys.close()
english.close()
hindi.close()
