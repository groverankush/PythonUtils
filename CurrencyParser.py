import os

path = "/home/emp272/Desktop"
os.chdir(path)

currency = open("currency.txt", 'r')
countries = open("countries.txt", 'w')
symbols = open("symbols.txt", 'w')

for line in currency.readlines():
    words = line.strip().split(",")
    countries.write("<item>{}</item>".format(words[1].replace("'", '').strip()) + "\n")
    symbols.write("<item>{}</item>".format(words[4].replace("'", '').strip()) + "\n")

countries.close()
symbols.close()
currency.close()
