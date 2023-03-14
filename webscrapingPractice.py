#install beautiful soup, requests, and html5lib first! any url should work
from bs4 import BeautifulSoup
import requests
URL = "https://konstantinnovation.github.io/apcsSpring.html"
req = requests.get(URL)
print(req.content)
soup = BeautifulSoup(req.text, "html.parser")
for link in soup.find_all('a'):
    print(link.get('href'))
