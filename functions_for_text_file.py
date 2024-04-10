import os
from functions import send_email

OUTPUT_PATH = "data.txt"


def store(extracted_value):
    with open(OUTPUT_PATH, "a") as file_to_store:
        file_to_store.write(extracted_value + "\n")


def read():
    with open(OUTPUT_PATH, "r") as file_to_read:
        return file_to_read.read()


def store_in_text_file(extracted):
    if not os.path.exists(OUTPUT_PATH):
        with open(OUTPUT_PATH, "w") as file:
            pass

    content = read()

    if extracted not in content:
        store(extracted)
        send_email(raw_message="Hey, new event was found.\n\n" + extracted)
