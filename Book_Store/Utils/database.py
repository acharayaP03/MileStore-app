
"""
Perform crud operation from here
"""


books =[] # store all books here

def add_book(name, author):
    books.append({"name":name, "author":author, "read": False})



def get_all_books():
    return books

def mark_books_as_read(name):
    for book in books:
        if book["name"] == name:
            book["read"] = True


def mark_books_as_not_read(name):
    for book in books:
        if book["name"] == name:
            book["read"] = False

def delete_book(name):
    global books
    books = [book for book in books if book["name"] != name]