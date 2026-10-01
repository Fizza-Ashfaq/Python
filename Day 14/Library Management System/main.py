from book import Book
from member import Member
from library import Library


library = Library()


while True:

    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Add Member")
    print("4. View Members")
    print("5. Borrow Book")
    print("6. Return Book")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        book_id = int(input("Enter book ID: "))
        title = input("Enter book title: ")
        author = input("Enter author name: ")

        book = Book(book_id, title, author)
        library.add_book(book)

        print("Book added successfully!")

    elif choice == "2":

        library.view_books()

    elif choice == "3":

        member_id = int(input("Enter member ID: "))
        name = input("Enter member name: ")

        member = Member(member_id, name)
        library.add_member(member)

        print("Member added successfully!")

    elif choice == "4":

        library.view_members()

    elif choice == "5":

        member_id = int(input("Enter member ID: "))
        book_id = int(input("Enter book ID: "))

        library.borrow_book(member_id, book_id)

    elif choice == "6":

        member_id = int(input("Enter member ID: "))
        book_id = int(input("Enter book ID: "))

        library.return_book(member_id, book_id)

    elif choice == "0":

        print("Goodbye!")
        break

    else:

        print("Invalid choice. Please try again.")