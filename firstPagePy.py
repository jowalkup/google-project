#! /usr/bin/python3
print("content/type:html")
print()
import cgi
allData = cgi.FieldStorage(  keep_blank_values=True)
preferredLanguage = allData['preferredLanguage'].value
#preferredLanguage = "Polish"
from location import Location
func = open("result.html", 'w')
func.write('''<html><head><link rel="stylesheet" href="firstPageCSS.css"><title>Voter Information Page: Language Search Results</title>''')

name = []
address = []
zip_code = []
language = []
locations = []

with open('soup1.txt') as f:
    counter = 0
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

i = 0
while i < len(name):
    if(language[i] == preferredLanguage):
        locations.append(Location(name[i], address[i], zip_code[i], language[i]))
    i+=1


# f.close()

def wrap(arr):
    final = ""
    start = "<br><tr>"
    end = "</tr>"
    for x in arr:
        final += start + x.get_name() + end
    return final

names = wrap(locations)

func.write('''
     <body>
     <table> <tr>''' + names + '''</tr></table></body></html>
    ''')

#func.close()
print(func.read())

# print('''<html>
# <head>
# <link rel="stylesheet" href="firstPageCSS.css">
# <title>Voter Information Page: Language Search Results</title>
#     <body>
#     <table> <tr>''' + names + '''</tr></table></body></html>
#     ''')
