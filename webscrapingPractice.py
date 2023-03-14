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
print(soup2.get_text())
