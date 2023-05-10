#! usr/bin/python3
print("content/type:html")

func = open("firstPage.html", 'w')


name = []
address = []
zip_code = []
language = []

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

f.close()

def wrap(arr):
    final = ""
    start = "<br><tr>"
    end = "</tr>"
    for x in arr:
        final += start + x + end
    return final

names = wrap(name)

func.write('''<html>
    <head>
    <title>Names</title>
    <h1>Names</h1>
    </head>
    <table> <tr>''' + names + '''</tr></table>
    </html>''')

func.close()
