name = []
address = []
zip_code = []
language = []

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

f.close()

queens = list(zip(name, address, zip_code, language))
for i in queens:
    if "Russian" in i[3]:
        pyscript.write(i)
'''
print()
for i in range(0, len(name)):
    print(name[i])
    print(address[i])
    print(zip_code[i])
    print(language[i])
    print()
'''
