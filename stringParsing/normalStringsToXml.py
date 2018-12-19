import os

# path = "/home/emp272/Desktop"
path = "C:\\Users\\ankush.grover\\Desktop"
os.chdir(path)

keys = open('keys.txt', 'r')
values = open('values.txt', 'r', encoding="utf8")

result = open('result.txt', 'w')

#    <string name="mileage_km">Mileage (km)</string>


for key in keys.readlines():
    val = '<string name="{}">{}</string>'.format(key.strip(), values.readline().strip())
    result.write(val+'\n')

keys.close()
values.close()
result.close()
