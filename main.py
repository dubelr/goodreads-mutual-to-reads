# write a program to open a goodreads profile given a url and scrape the data from the to-read shelf
# and write it to a csv file

import requests
from bs4 import BeautifulSoup
import csv

# get the url from the user
url = input("Enter the url of the goodreads profile: ")

# get the html content of the page
page = requests.get(url)

# parse the html content
soup = BeautifulSoup(page.content, 'html.parser')

# get the list of books
books = soup.find_all('tr', class_='bookalike review')

# open a csv file to write the data
with open('books.csv', 'w', newline='') as csvfile:
    # create a csv writer object
    writer = csv.writer(csvfile)
    # write the header
    writer.writerow(['Title', 'Author', 'Rating', 'Date Read', 'Date Added'])
    # loop through the books
    for book in books:
        # get the title
        title = book.find('td', class_='field title').find('a').text.strip()
        # get the author
        author = book.find('td', class_='field author').find('a').text.strip()
        # get the rating
        rating = book.find('td', class_='field rating').find('span', class_='value').text.strip()
        # get the date read
        date_read = book.find('td', class_='field date_read').find('span', class_='value').text.strip()
        # get the date added
        date_added = book.find('td', class_='field date_added').find('span', class_='value').text.strip()
        # write the data to the csv file
        writer.writerow([title, author, rating, date_read, date_added])

# print a message
print("Data written to books.csv file")

# end of program
