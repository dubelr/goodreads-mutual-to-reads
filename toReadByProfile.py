import requests
from bs4 import BeautifulSoup
import csv

baseURL = 'https://www.goodreads.com/review/list'

def getShelfByProfile(profileURLId, shelf):
    # iterate through the pages of the to-read shelf and scrape the data until the last page is reached
    endReached = False
    pageCt = 1
    while(not endReached):
        # get the html content of the page
        page = requests.get('{}/{}?page={}&shelf={}'.format(baseURL, profileURLId, pageCt, shelf))

        # parse the html content and get the list of books
        soup = BeautifulSoup(page.content, 'html.parser')
        books = soup.find_all('tr', class_='bookalike review')

        # if there are no books on the page, then the last page has been reached
        if(len(books) == 0):
            endReached = True
            break

        # open the csv file to write the data to
        with open('books.csv', 'a', newline='') as csvfile:
            bookwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            # if this is the first page, write the header row
            if(pageCt == 1):
                bookwriter.writerow(['Title', 'Author', 'Rating'])

            # write the data to the csv file
            for book in books:
                title = book.find('td', class_='field title').find('a').text.strip()
                author = book.find('td', class_='field author').find('a').text.strip()
                rating = book.find('td', class_='field avg_rating').find('div', class_='value').text.strip()
                bookwriter.writerow([title, author, rating])

        # increment the page number
        pageCt += 1