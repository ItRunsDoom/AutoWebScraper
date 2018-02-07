# Libraries necessary to run: bs4, requests, and get
from bs4 import BeautifulSoup
import requests

def main():
    print("Welcome to the small automated web scraper 1.0 \nIf you need help type <help>")

    while (True):
        userInput = input("cmd: ").lower()

        if (userInput == "help"):
            print("Commands\n<help> brings this up\n<quit> quits the program\n<tag> lets you search for a specific HTML tag\n<url> lets you choose which URL to scrape, or input a 'URL Number'")
        # Quits the program
        if (userInput == "quit"):
            print("Goodbye...")
            return False
        # Command scrapes URl and prettifies it
        if (userInput == "url"):
            # uses beautifulsoup4 to scrape and orginize the searched URL
            print("Please enter a URL you would like to read/scrape")
            userInput = input("cmd: ")
            # Uses requests to "request" a webpage. prettifys it, and prints it
            try:
                page = requests.get(userInput)
                soup = BeautifulSoup(page.content, 'html.parser')
                print(soup.prettify())
            except:
                print("That didn't work :( Try again or check your internet connection")
        # Command for finding a tag within the soup
        if (userInput == "tag"):
            #searches tags in the body as per user input
            print("Please enter an HTML tag you would like to search for")
            userInput = input("cmd: ").lower()
            searchedArray = soup.find_all(userInput)
            # If the searchedArray has no values then this tells the user why
            if (len(searchedArray) == 0):
                print("Sorry, it seems like this tag either does not occur in the HTML file, or does not exist")
            else:
                # Takes the searchedArray and prints it in an easier way to read for the user
                n = 1
                for i in searchedArray:
                    n += n
                    str(i)
                    str(n)
                    print(i + " this is link number " + n)

main()
