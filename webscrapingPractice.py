#install beautiful soup, requests, and html5lib first! any url should work
import requests
URL = "https://konstantinnovation.github.io/apcsSpring.html"
r = requests.get(URL)
print(r.content)
