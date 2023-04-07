from utils.database_connection import DatabaseConnection


HOST = "books.db"
TABLE = "book"

SQL_CREATE_TABLE_COMMAND = f"""
CREATE TABLE IF NOT EXISTS {TABLE} (
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER NOT NULL
);
"""

SQL_INSERT_COMMAND = f"INSERT INTO {TABLE} VALUES (?, ?, ?);"

SQL_SELECT_COMMAND = f"SELECT * FROM {TABLE};"

SQL_DELETE_COMMAND = f"DELETE FROM {TABLE} WHERE title=?;"

SQL_UPDATE_COMMAND = f"""
UPDATE {TABLE}
SET author=?, year=?
WHERE title=?;
"""


def create_book_table():
    with DatabaseConnection(HOST) as conn:
        cur = conn.cursor()
        cur.execute(SQL_CREATE_TABLE_COMMAND)


def input_book():
    title = input("Enter the book title\t: ").title()
    author = input("Enter the book author\t: ").capitalize()
    year = int(input("Enter the release year\t: "))
    return (title, author, year)


def insert_book_table():
    with DatabaseConnection(HOST) as conn:
        cur = conn.cursor()
        cur.execute(SQL_INSERT_COMMAND, input_book())


def get_all_books():
    with DatabaseConnection(HOST) as conn:
        cur = conn.cursor()
        cur.execute(SQL_SELECT_COMMAND)

        for title, author, year in cur.fetchall():
            print(f"{title} ({year}) - {author}")


def delete_book():
    title = input("Enter the book title\t: ").title()

    with DatabaseConnection(HOST) as conn:
        cur = conn.cursor()
        cur.execute(SQL_DELETE_COMMAND, (title,))


def update_book():
    title, author, year = input_book()
    with DatabaseConnection(HOST) as conn:
        cur = conn.cursor()
        cur.execute(SQL_UPDATE_COMMAND, (author, year, title))
