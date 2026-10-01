class Member:
    def __init__(self, member_id, name):
        self.member_id=member_id
        self.name=name
        self.borrowed_books = []

    def display_info(self):
        print("\n---Member Info---")
        print(f"Member ID: {self.member_id}")
        print(f"Name: {self.name}")
        print(f"Borrowed Books: ")
        for book in self.borrowed_books:
            print(book.title)

member1 = Member(1, "Ali")

member1.display_info()