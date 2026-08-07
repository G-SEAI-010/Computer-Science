# 1. Create a Book Class
class Book:
    def __init__(self, name, author, release_date):
        self.name = name
        self.author = author
        self.release_date = release_date
        self.read = False

    def __str__(self):
        status = "Gelesen" if self.read else "Nicht gelesen"
        return f"'{self.name}' von {self.author} ({self.release_date}) - {status}"


# 2. Create a BookCollection Class
# 3. Add Books to the Collection
# 4. Mark Books as Read
# 5. Display Collection Status
class BookCollection:
    def __init__(self, books=None):
        if books is None:
            self.books = []
        elif isinstance(books, list) and all(isinstance(book, Book) for book in books):
            self.books = books
        else:
            raise TypeError(
                "'books' muss eine Liste aus Buchinstanzen  oder 'None' sein."
            )

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
            print(f"Buch hinzugefügt: {book.name}")
        else:
            raise TypeError(
                "Nur Buchinstanzen können der Kollektion hinzugefügt werden."
            )

    def mark_as_read(self, book_name):
        for book in self.books:
            if book.name.lower() == book_name.lower():
                book.read = True
                print(f"'{book_name}' wurde als gelesen markiert.")
                return
        print(f"Es wurde kein Buch mit dem Namen '{book_name}' gefunden.")

    def list_books(self):
        if not self.books:
            print("Die Bücherkollektion ist leer.")
        else:
            print("Bücher in der Kollektion:")
            for book in self.books:
                print(book)


# --- Test ---

# Buchinstanzen erstellen
book1 = Book("1984", "George Orwell", 1949)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)

# Buchkollektioninstanz erstellen
my_collection = BookCollection()

# Bücher zur Kollektion hinzufügen
my_collection.add_book(book1)
my_collection.add_book(book2)
my_collection.add_book(book3)

print()

# Alle Bücher in der Bücherkollektion anzeigen
my_collection.list_books()

print()

# Ein Buch in der Bücherkollektion als 'gelesen' markieren
my_collection.mark_as_read("1984")

print()

# Nochmals anzeigen lassen, um die Änderung zu sehen
my_collection.list_books()

print()

# Feedback, wenn Buch nicht gefunden wurde
my_collection.mark_as_read("sdfdfgdfgf")
