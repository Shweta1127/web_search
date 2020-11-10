import requests
from bs4 import BeautifulSoup
	
def searchResult(ip):
	google_search = requests.get('https://www.google.com/search?q='+ip)
	soup = BeautifulSoup(google_search.text, 'lxml')
	
	link_container = soup.find_all('div', class_='kCrYT')
	urls = []
	headers = []

	for link in link_container:
		link = link.find('a')
		if link:
			header = link.find('div', class_='BNeawe vvjwJb AP7Wnd')
			if header:
				url = link.attrs['href']
				url = url.strip('/url?q=')
				url = url.split('&', 1)[0]
				urls.append(url)
				headers.append(header.string)
		
	return urls, headers
