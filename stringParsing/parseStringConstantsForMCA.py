import os

# path = "/home/emp272/Desktop"
path = "C:\\Users\\ankush.grover\\Desktop"

os.chdir(path)

keys = open("parse.txt", 'r')
strings = open("strings.txt", 'w')

categories = set()
actions = set()


def print_strings(typeof, value):
    return 'String {}_{} = "{}";\n'.format(typeof.upper(), value.upper().strip(), value.strip())


for line in keys.readlines():
    words = line.split(".")[1].split(":")
    if len(words) == 1:
        strings.write(print_strings("SCREEN", words[0]))
        # strings.write('String SCREEN_{} = "{}"\n;'.format(words[0].upper().strip(), words[0].strip()))
    else:
        categories.add(words[0].strip())

        subtypes = words[1].strip().split("*")
        actions.add(subtypes[0].strip().rstrip("_"))

for category in categories:
    strings.write(print_strings("CATEGORY", category))

for action in actions:
    strings.write(print_strings("ACTION", action))
