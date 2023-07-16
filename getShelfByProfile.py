import requests
from bs4 import BeautifulSoup
import csv
import book


def getShelfByProfile(profileURLId, shelf):
    baseURL = 'https://www.goodreads.com/review/list'
    
    # iterate through the pages of the to-read shelf and scrape the data until the last page is reached
    endReached = False
    pageCt = 1
    while(not endReached):
        # get the html content of the page
        page = requests.get('{}/{}?page={}&shelf={}'.format(baseURL, profileURLId, pageCt, shelf))

        # parse the html content and get the list of books
        soup = BeautifulSoup(page.content, 'html.parser')
        booksResultSet = soup.find_all('tr', class_='bookalike review')

        # if there are no books on the page, then the last page has been reached
        if(len(booksResultSet) == 0):
            endReached = True
            break

        # convert the result set to a list of book objects
        booksList = []
        for bookItem in booksResultSet:
            title = bookItem.find('td', class_='field title').find('a').text.strip()
            author = bookItem.find('td', class_='field author').find('a').text.strip()
            rating = bookItem.find('td', class_='field avg_rating').find('div', class_='value').text.strip()
            booksList += book(title, author, rating)

        # increment the page number
        pageCt += 1