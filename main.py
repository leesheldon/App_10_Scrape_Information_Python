import time
from functions_for_text_file import store_in_text_file
from functions_for_database import store_in_database
from functions import scrape, extract
import sqlite3

URL = "http://programmer100.pythonanywhere.com/tours/"


if __name__ == "__main__":
    connection = sqlite3.connect("data.db")

    while True:
        try:
            scraped = scrape(URL)
            extracted = extract(scraped)
            print(extracted)

            if extracted != "No upcoming tours":
                # Work with data in text file
                # store_in_text_file(extracted)

                # Work with data in database
                store_in_database(connection, extracted)

            time.sleep(5)
        except KeyboardInterrupt:
            break

    connection.close()
