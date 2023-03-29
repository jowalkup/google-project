#install beautiful soup, requests, and html5lib first! any url should work
from bs4 import BeautifulSoup
import requests
URL = "https://konstantinnovation.github.io/apcsSpring.html"
req = requests.get(URL)
#print(req.content)
soup = BeautifulSoup(req.text, "html.parser")
#for link in soup.find_all('a'):
    #print(link.get('href')) # gets the links
#print(soup.get_text()) # gets the text

URL2 = "https://www.nyc.gov/site/civicengagement/voting/poll-site-service-list.page"
req2 = requests.get(URL2)
soup2 = BeautifulSoup(req2.text, "html.parser")
#print(soup2.get_text())

#f = open("soup4.txt", "x")
#f.write("Hello There\n")

f = open("soup2.txt", "w")
f.write(soup2.get_text())

d = open("soup.txt", "w")
d.write(soup.get_text())

r = open("soup1.txt", "r")
# print(r.read())
#for x in r:
    #if x.strip():
        #print(x)
zips = list()
j = 1
for k in r:
    if (j % 5 == 3):
        zips.append(k[:len(k) - 1])
    j += 1
print("zip codes ")
print(zips)
print("\n")
r.close()

s = open("soup1.txt", "r")
languages = list()
i = 1
for x in s:
    if (i % 5 == 4):
        languages.append(x[:len(x) - 1])
    i += 1
print("languages ")
print(languages)
print("\n")
s.close()

t = open("soup1.txt", "r")
adds = list()
l = 1
for x in t:
    if (l % 5 == 2):
        adds.append(x[:len(x) - 1])
    l += 1
print("addresses ")
print(adds)
print("\n")
t.close()

u = open("soup1.txt", "r")
names = list()
o = 1
for x in u:
    if (o % 5 == 1):
        names.append(x[:len(x) - 1])
    o += 1
print("names ")
print(names)
print("\n")

# zips = list()
# j = 1
# for k in r:
#     if (j % 5 == 4):
#         zips.append(k[:len(k) - 1])
#     j += 1
# print(zips)
