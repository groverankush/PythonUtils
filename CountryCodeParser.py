import os

path = "/home/emp272/Desktop"
os.chdir(path)

keys = open('countryList.csv', 'r')

country = open('country.txt', 'w')
code = open('code.txt', 'w')
symbol = open('symbol.txt', 'w')



for key in keys.readlines():

    items = key.split(",")

    country.write('<item>{}</item>\n'.format(items[0].strip()))
    code.write('<item>+{}</item>\n'.format(items[2].strip()))
    symbol.write('<item>{}</item>\n '.format(items[1].strip()))


keys.close()
country.close()
symbol.close()