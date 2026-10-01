class Book:
    def __init__(self, book_id, title, author):
        self.book_id=book_id
        self.title=title
        self.author=author
        self.is_available = True

    def display_info(self):
        print(f"\nBook Information")
        print(f"Book ID: {self.book_id}")
        print(f"Book Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Available: {self.is_available}")

book1 = Book(1, "The Hobbit", "J.R.R. Tolkien")

book1.display_info()