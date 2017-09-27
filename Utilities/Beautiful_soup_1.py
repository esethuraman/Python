import requests
from bs4 import BeautifulSoup

seed_url = "https://en.wikipedia.org/wiki/Tropical_cyclone"
r = requests.get(seed_url)
soup = BeautifulSoup(r.text, "html.parser")

href_set=set()
href_set.add(seed_url)

for link in soup.find_all('a'):
	url = str (link.get("href")) 
	url = url.strip()
	if( url != seed_url) :
		href_set.add(url)	
	
print(len(href_set))
