import requests
import re

fileToWrite = open('scraped.txt', 'a+')

searchterm = input('Search term to scrape: ')
searchterm = searchterm.replace(' ', '+')
print('----')


fuckDups = list()
counter = 0

while True:
	if counter == 5:
		fileToWrite.close()
		print('----\nDone!')
		break

	htmlCode = requests.get(f'https://www.bing.com/search?q={searchterm}+site%3Arepl.it&first={counter}&FORM=PERE', headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.0.0 Safari/537.36'}).text
	regexedSource = re.findall(r'\<cite\>(http(s?)\:\/\/repl.it\/@\w+\/(\w+-?)+)<', htmlCode)

	for regex in regexedSource:
		link = regex[0]

		if link not in fuckDups:
			fuckDups.append(link)
			fileToWrite.write(f'{link}\n')
			print(link)

	counter+=10

# Jayceez X Chucky W | .gg/energy be here soon 
