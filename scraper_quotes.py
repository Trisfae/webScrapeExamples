from bs4 import BeautifulSoup
import requests
import time
import csv

counter = 1
csv_file = open('scraped_quotes.csv', 'w')

csv_writer = csv.writer(csv_file)

csv_writer.writerow(['Quote', 'Author', 'Tags'])

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
        quote_tags = div.find_all('a', class_='tag')

        tag_list = []

        for text in quote_tags:
            tag = text.get_text()
            quote_tags_text = text.text
            tag_list.append(tag)

            print('            ' + text.text)



        csv_writer.writerow([quote_text, quote_author, tag_list])

    counter += 1
    time.sleep(1)

counter = 0
csv_file.close()