# Library Management System
# Coded By Mr Sabaz Ali Khan

class Book:
    def __init__(self, book_id, title, author, total_copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies

    def __str__(self):
        return f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Available: {self.available_copies}/{self.total_copies}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"ID: {self.member_id}, Name: {self.name}, Borrowed Books: {[book.book_id for book in self.borrowed_books]}"

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book_id, title, author, total_copies):
        book = Book(book_id, title, author, total_copies)
        self.books.append(book)
        print(f"Book '{title}' added successfully.")

    def register_member(self, member_id, name):
        member = Member(member_id, name)
        self.members.append(member)
        print(f"Member '{name}' registered successfully.")

    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def borrow_book(self, member_id, book_id):
        book = self.find_book(book_id)
        member = self.find_member(member_id)
        
        if not book:
            print("Book not found.")
            return
        if not member:
            print("Member not found.")
            return
        if book.available_copies == 0:
            print("No copies available.")
            return
        if book in member.borrowed_books:
            print("Book already borrowed by this member.")
            return

        book.available_copies -= 1
        member.borrowed_books.append(book)
        print(f"Book '{book.title}' borrowed by {member.name}.")

    def return_book(self, member_id, book_id):
        book = self.find_book(book_id)
        member = self.find_member(member_id)
        
        if not book:
            print("Book not found.")
            return
        if not member:
            print("Member not found.")
            return
        if book not in member.borrowed_books:
            print("This book was not borrowed by this member.")
            return

        book.available_copies += 1
        member.borrowed_books.remove(book)
        print(f"Book '{book.title}' returned by {member.name}.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("\nBooks in Library:")
            for book in self.books:
                print(book)

    def display_members(self):
        if not self.members:
            print("No members registered.")
        else:
            print("\nRegistered Members:")
            for member in self.members:
                print(member)

def main():
    library = Library()
    
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Display All Books")
        print("6. Display All Members")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            book_id = input("Enter Book ID: ")
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            try:
                total_copies = int(input("Enter Total Copies: "))
                library.add_book(book_id, title, author, total_copies)
            except ValueError:
                print("Invalid input for total copies. Please enter a number.")
                
        elif choice == '2':
            member_id = input("Enter Member ID: ")
            name = input("Enter Member Name: ")
            library.register_member(member_id, name)
            
        elif choice == '3':
            member_id = input("Enter Member ID: ")
            book_id = input("Enter Book ID: ")
            library.borrow_book(member_id, book_id)
            
        elif choice == '4':
            member_id = input("Enter Member ID: ")
            book_id = input("Enter Book ID: ")
            library.return_book(member_id, book_id)
            
        elif choice == '5':
            library.display_books()
            
        elif choice == '6':
            library.display_members()
            
        elif choice == '7':
            print("Exiting Library Management System. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()