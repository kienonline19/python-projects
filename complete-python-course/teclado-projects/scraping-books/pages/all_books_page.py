import re
import logging

from bs4 import BeautifulSoup
from parsers.book_parser import BookParser
from locators.all_books_page import AllBooksPageLocators

logger = logging.getLogger('scraping.all_books_page')


class AllBooksPage:
    def __init__(self, page_content):
        logger.debug("Parsing page content with BeautifulSoup HTML parser.")
        self.soup = BeautifulSoup(page_content, 'html.parser')

    @property
    def books(self):
        logger.debug(f"Finding all books in the page using `{AllBooksPageLocators.BOOKS}`.")
        locator = AllBooksPageLocators.BOOKS
        book_tags = self.soup.select(locator)
        return [BookParser(e) for e in book_tags]

    @property
    def page_count(self):
        logger.debug(f"Finding all number of catalogue pages available...")
        content = self.soup.select_one(AllBooksPageLocators.PAGER).string

        logger.info(f"Found number of catalogue pages available: `{content}`.")
        matcher = re.search(r'Page \d+ of (\d+)', content)

        pages = int(matcher.group(1))
        logger.debug(f"Extracted number of pages as integer: `{pages}`")
        return pages
