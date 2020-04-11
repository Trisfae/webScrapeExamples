from bs4 import BeautifulSoup
import requests
import time

counter = 1

for x in range(10):
    link = ('http://quotes.toscrape.com/page/' + str(counter) + '/')
    print ('Scraping: ' + link)
    source = requests.get(link).text
    soup = BeautifulSoup(source, 'lxml')

    for div in soup.find_all('div', class_='quote'):

        # empty print to line break for loop list
        print()

        # prints out the quote
        quote_text = div.span.text
        print(quote_text)

        # prints out the author of the quote
        quote_author = div.small.text
        print ('    ' + '- ' +  quote_author)

        # prints out the tags for the quote in csv format
        tags = div.find_all('a', class_='tag')
        print ('        ' +'TAGS')
        for text in tags:
            print('            ' + text.text)

    counter += 1
    time.sleep(1)
counter = 0







