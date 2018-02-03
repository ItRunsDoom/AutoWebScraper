# Libraries necessary to run: bs4, requests
from bs4 import BeautifulSoup
import requests

def main():
    print("Welcome to the small automated web scraper 1.0 \nIf you need help type <help>")

    while (True):
        userInput = input("cmd: ").lower()
        # The help page
        if (userInput == "help"):
            print("Commands\n<help> brings this up\n<quit> quits the program\n<tag> lets you search for a specific HTML tag\n<url> lets you choose which URL to scrape, or input a 'URL Number'")
       
        # Quits the program
        if (userInput == "quit"):
            print("Goodbye...")
            return False
    
        # Command scrapes URL and prettifies it
        if (userInput == "url"):
            # uses beautifulsoup4 to scrape and orginize the searched URL
            print("Please enter a URL you would like to read/scrape")
            userInput = input("cmd: ")
            # Uses requests to "request" a webpage. prettifys it, and prints it
            print("Loading . . . \nType <url -p> to print out the HTML")
            try:
                page = requests.get(userInput)
                soup = BeautifulSoup(page.content, 'html.parser')
                pureHTML = soup.prettify()
            except:
                print("That didn't work :( Try again or check your internet connection")
       
        # Takes pureHTML and prints this, I added this because I liked how it gave the user more control over all the clutter
        if (userInput == "url -p"):
            print(pureHTML)
        
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
                print(searchedArray)

        # Takes all the links in soup and assignes them a number. It also prints the corrosponding href name
        if (userInput == "links"):
            links = soup.find_all("a")
            for i in links:
                print(links[i] + "/n")

main()
