

from Utils import database
# Create a book app.

USER_CHOICES = """
Enter: 
- 'a' to add a new book
- 'l' to list all books
- 'r' to remove a book
- 'd' to delete a book
- 'q' to quit
"""



def menu():

    user_input = input(USER_CHOICES)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_remove_book()
        else:
            print("Unknown command. Please try again.")

        user_input = input(USER_CHOICES)


def prompt_add_book():
    name = input("Enter book name: ")
    author = input("Enter book author: ")

    database.add_book(name, author)

def list_books():
    books = database.get_all_books()

    for index, book in enumerate(books):
        read = 'YES' if book['read'] else 'NO'
        print(f"{index + 1}. {book['name']} by {book['author']}, read: {read}")

def prompt_remove_book():
    remove = input("Enter book to remove: ")

    database.delete_book(remove)

def prompt_read_book():
    name = input("Enter book name: ")

    database.mark_books_as_read(name)

if __name__ == '__main__':
    menu()