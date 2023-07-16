# Run the program and enter the url of the profile when prompted. The program will scrape the data and write it to a csv file called books.csv.
import toReadByProfile
from getShelfByProfile import getShelfByProfile

# get the url from the user and parse it to get the username
# example url: https://www.goodreads.com/review/list/12345678
username = input("Enter the url of the goodreads profile: ").split('/')[-1]


if __name__ == '__main__':
    main()
