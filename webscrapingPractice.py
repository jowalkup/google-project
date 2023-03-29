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

y = list()
i = 1
for x in r:
    if (i % 5 == 4):
        y.append(x)
    i += 1
print(y)
