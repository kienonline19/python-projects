import utils.database as db


MENU = """Enter
'a' - add a book
'l' - list books
'd' - delete book
'u' - update book
'q' - quit
your choice: """

operations = {
    'a': db.insert_book_table,
    'l': db.get_all_books,
    'd': db.delete_book,
    'u': db.update_book
}

db.create_book_table()
user_choice = input(MENU).lower()

while user_choice != 'q':

    if user_choice in operations:
        operations[user_choice]()
    else:
        print("Invalid command, please try again!")

    user_choice = input(MENU).lower()
