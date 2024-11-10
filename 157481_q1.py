class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def mark_as_borrowed(self):
        self.is_borrowed = True

    def mark_as_returned(self):
        self.is_borrowed = False

class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.mark_as_borrowed()
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print(f"'{book.title}' is already borrowed.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.mark_as_returned()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'")
        else:
            print(f"{self.name} does not have '{book.title}' borrowed.")

    def list_borrowed_books(self):
        
        print("Borrowed books:")
        for book in self.borrowed_books:
            print(f"- {book.title} by {book.author}")

if __name__ == "__main__":
    
    mwangi = LibraryMember("Mwangi", "M001")
    book1 = Book("Siku Njema", "Ken Walibora")
    book2 = Book("Petals of Blood", "Ngugi wa Thiong'o")

    mwangi.borrow_book(book1)
    mwangi.list_borrowed_books()
    mwangi.return_book(book1)
    mwangi.list_borrowed_books()