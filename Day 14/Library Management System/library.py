from book import Book
from member import Member

class Library:

    def __init__(self):
        self.books_list=[]
        self.members_list=[]

    def add_book(self, book):
        self.books_list.append(book)

    def view_books(self):
        for book in self.books_list:
            book.display_info()

    def add_member(self, member):
        self.members_list.append(member)

    def view_members(self):
        for member in self.members_list:
            member.display_info()

    def borrow_book(self, member_id, book_id):
        bk = None
        member_found = None
        for book in self.books_list:
            if book_id==book.book_id:
                bk=book

        for member in self.members_list:
            if member_id==member.member_id:
                member_found=member

        if bk is None:
            print("Book not found.")
            return
        if member_found is None:
            print("Member not found.")
            return
        
        if not bk.is_available:
            print("Book is already borrowed.")
            return
        
        bk.is_available = False
        member_found.borrowed_books.append(bk)
        print("Book borrowed successfully!")


    def return_book(self, member_id, book_id):

        bk = None
        member_found = None
        for book in self.books_list:
            if book_id==book.book_id:
                bk=book

        for member in self.members_list:
            if member_id==member.member_id:
                member_found=member

        if bk is None:
            print("Book not found.")
            return
        if member_found is None:
            print("Member not found.")
            return

        if bk.is_available:
            print("Book is already available.")
            return

        bk.is_available = True
        member_found.borrowed_books.remove(bk)
        
        print("Book returned successfully!")

    
library = Library()

book1 = Book(1, "The Hobbit", "J.R.R. Tolkien")

library.add_book(book1)
library.view_books()

member1=Member(1, "Fizza" )
library.add_member(member1)
library.view_members()

library.borrow_book(1,1)
library.view_books()
library.view_members()

library.return_book(1,1)
library.view_books()
library.view_members()

print(library.books_list)