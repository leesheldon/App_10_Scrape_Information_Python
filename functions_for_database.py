from functions import send_email


def store(connection, extracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]

    cursor = connection.cursor()
    cursor.execute("INSERT INTO events VALUES(?,?,?)", row)
    connection.commit()
    cursor.close()


def read(connection, extracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]
    band, city, date = row

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM events WHERE band=? AND city=? AND date=?", (band, city, date))
    rows = cursor.fetchall()
    cursor.close()
    return rows


def store_in_database(connection, extracted):
    row = read(connection, extracted)

    if not row:
        store(connection, extracted)
        send_email(raw_message="Hey, new event was found.\n\n" + extracted)
