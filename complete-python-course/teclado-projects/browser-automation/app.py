from selenium import webdriver
from pages.quotes_page import QuotesPage, InvalidTagForAuthorError

# auto-install-chromedriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    author = input("Enter the author you'd like quotes from: ")
    tag = input("Enter your tag: ")

    # chrome = webdriver.Chrome()
    chrome.get('http://quotes.toscrape.com/search.aspx')

    page = QuotesPage(chrome)
    print(page.search_for_quotes(author, tag))
except InvalidTagForAuthorError as e:
    print(e)
except Exception as e:
    print(e)
    print("An unknown occurred. Please try again!")

# chrome.close()
