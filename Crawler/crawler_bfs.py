import requests
from bs4 import BeautifulSoup
import re

def main():
	seed = "https://en.wikipedia.org/wiki/Tropical_cyclone"
	r = requests.get(seed) 
	soup = BeautifulSoup(r.text, "html.parser")

	crawled_set = []
	file = open('Results_crawler.txt', 'w')
	hashed_urls_file = open('HashedUrls.txt', 'w')
	same_page_urls_file = open('SampePageUrls.txt', 'w')

	hashed_urls_count = 0
	unhashed_urls_count = 0
	same_page_urls_count = 0
	
	for link in soup.find_all('a'):
		url = str (link.get("href"))
		
		if (url[:1] == '#'):
			hashed_urls_file.write(url+"\n")	
			hashed_urls_count = hashed_urls_count + 1 
		
		elif (is_same_page_link(url, seed)):
			same_page_urls_count +=1 
			same_page_urls_file.write(url + "\n")
		
		else:
			unhashed_urls_count = unhashed_urls_count + 1
			file.write(url+"\n")
			crawled_set.append(url)
		
	
	print("TOTAL URLS        : ", len(crawled_set))
	print("HASHED URLS       : ", hashed_urls_count)
	print("URLS WITHOUT HASH : ", unhashed_urls_count)
	print("SAME PAGE URLS    : ", same_page_urls_count)

def is_same_page_link(url, seed):
	duplicate_flag = True
	if('#' not in url):
		duplicate_flag = False

	return duplicate_flag

if __name__ == "__main__":
	main()

