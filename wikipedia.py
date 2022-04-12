import wikipediaapi
import time

def wikiapi():
    wiki = wikipediaapi.Wikipedia('en')
    x = True
    while x == True:
        search = input("Search Something")
        target = wiki.page(search.replace(" ", "_"))
        time.sleep(1)
        print("Here is a summary for your search:\n " + target.summary)
        round2 = input("Would you like to search something else? (yes/no)")

        if(round2 == "no"):
            x = False

if __name__ == '__main__':
    wikiapi()
