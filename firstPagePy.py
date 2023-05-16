#! usr/bin/python3
print("content/type:html")
from locationClass import Location
func = open("firstPage.html", 'w')


name = []
address = []
zip_code = []
language = []
locations = []

with open('soup1.txt') as f:
    counter = 0;
    for line in f:
        if(line.strip() != ""):
            if(counter%4 == 0):
                name.append(line.strip())
            elif(counter%4 == 1):
                address.append(line.strip())
            elif(counter%4 == 2):
                zip_code.append(line.strip())
            else:
                language.append(line.strip())
            counter += 1

i = 0;
while i < len(name):
    locations.append(Location(name[i], address[i], zip_code[i], language[i]))
    i+=1


f.close()

def wrap(arr):
    final = ""
    start = "<br><tr>"
    end = "</tr>"
    for x in arr:
        final += start + x.get_name() + end
    return final

names = wrap(locations)

func.write('''<html>
    <head>
    <link rel="stylesheet" href="firstPageCSS.css">
    <title>Names</title>
    <h1>Names</h1>
    </head>
    <body>
    <table> <tr>''' + names + '''</tr></table></body>
    </html>''')

func.close()
