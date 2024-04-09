import requests
import selectorlib
import os

URL = "http://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/39.0.2171.95 Safari/537.36'}
OUTPUT_PATH = "data.txt"

def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value


def store(extracted_value):
    with open(OUTPUT_PATH, "a") as file_to_store:
        file_to_store.write(extracted_value + "\n")


def read():
    with open(OUTPUT_PATH, "r") as file_to_read:
        return file_to_read.read()


if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    print(extracted)

    if not os.path.exists(OUTPUT_PATH):
        with open(OUTPUT_PATH, "w") as file:
            pass

    content = read()

    if extracted != "No upcoming tours":
        if extracted not in content:
            store(extracted)
