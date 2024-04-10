import time
from functions_for_text_file import store_in_text_file
from functions import scrape, extract

URL = "http://programmer100.pythonanywhere.com/tours/"


if __name__ == "__main__":
    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)

        if extracted != "No upcoming tours":
            # Work with data in text file
            store_in_text_file(extracted)

        time.sleep(5)
