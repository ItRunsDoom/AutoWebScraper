# Main function, makes program loop and handles input
# Libraries neccesary. bs4 and requests
# URL uses beautifulsoup4 to scrape and orginize the searched URL
def URL():
     from bs4 import BeautifulSoup
     import requests
     print("Please enter a URL you would like to read/scrape")
     userInput = input("cmd: ")
     # Uses requests to "request" a webpage. prettifys it, and prints it
     page = requests.get(userInput)
     soup = BeautifulSoup(page.content, 'html.parser')
     print(soup.prettify())
     return soup
     return page
#tagSearch searches tags in the body as per user input
def tagSearch():
    print("Please enter an HTML tag you would like to search for")
    userInput = input("cmd: ").lower
    for userInput in soup:
        print soup.findAll(userInput)
def main():
    print("Welcome to the small automated web scraper 1.0 \n If you need help type 'help'")
    # Program loop. The prompt is cmd:
    while (True):
        userInput = input("cmd: ").lower()
        if (userInput == "help"):
            print("Commands\n<help> brings this up\n<quit> quits the program\n<tag> lets you search for a specific HTML tag\n<url> lets you choose which URL to scrape, or input a 'URL Number'")
        if (userInput == "quit"):
            return False
        if (userInput == "url"):
            URL()
        if (userInput == "tag"):
            tagSearch()

main()
