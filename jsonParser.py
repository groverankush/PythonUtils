import json
import os

path = "/home/emp272/Desktop"
os.chdir(path)

file = open("coordinates.json", 'r')

data = json.load(file)

file.close()

for co in data:
    print('temp.add(new LocationModel({},{},"{}"));'.format(co['lat'], co['long'], "2017-07-24"))
