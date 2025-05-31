#Library Management System using python 

class Book:
    def __init__(self,book_id,title,author,image_url=None,available = True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.image_url = image_url
        self.available = available

    def __str__(self):
        return f'{self.book_id}:{self.title} by {self.author} - {'Available' if self.available else 'Issued'} '
    
class Member:
    def __init__(self,member_id,name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f'{self.member_id}:{self.name} | Borrowed:{[book.title for book in self.borrowed_books]}'
    
class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self,book):
        self.books.append(book)

    def remove_book(self,book_id):
        self.books = [b for b in self.books if b.book_id != book_id]

    def register_member(self,member):
        self.members.append(member)

    def issue_book(self,book_id,member_id):
        book = next((b for b in self.books if b.book_id == book_id),None)
        member = next((m for m in self.members if m.member_id == member_id),None)
        
        if not book:
            return {"success": False, "message": "Book not found"}
        if not member:
            return {"success": False, "message": "Member not found"}
        if not book.available:
            return {"success": False, "message": "Book is already issued"}
        
        book.available = False
        member.borrowed_books.append(book)
        return {"success": True, "message": f"Book {book.title} issued to {member.name}"}

    def return_book(self,book_id,member_id):
        member = next((m for m in self.members if m.member_id == member_id),None)
        if not member:
            return {"success": False, "message": "Member not found"}
            
        book = next((b for b in member.borrowed_books if b.book_id == book_id),None)
        if not book:
            return {"success": False, "message": "Book not found in member's borrowed list"}
            
        book.available = True
        member.borrowed_books.remove(book)
        return {"success": True, "message": f"Book {book.title} returned by {member.name}"}

    def get_available_books(self):
        return [book for book in self.books if book.available]

    def get_issued_books(self):
        return [book for book in self.books if not book.available]

    def get_member_books(self,member_id):
        member = next((m for m in self.members if m.member_id == member_id),None)
        if not member:
            return []
        return member.borrowed_books

# Create library
library = Library()

# Add sample books
library.add_book(Book(1, "1984", "George Orwell", "https://m.media-amazon.com/images/I/71kxa1-0mfL._AC_UF1000,1000_QL80_.jpg"))
library.add_book(Book(2, "The Great Gatsby", "F. Scott Fitzgerald", "https://m.media-amazon.com/images/I/71FTb9X6wsL._AC_UF1000,1000_QL80_.jpg"))
library.add_book(Book(3, "To Kill a Mockingbird", "Harper Lee", "https://m.media-amazon.com/images/I/71FxgtFKcQL._AC_UF1000,1000_QL80_.jpg"))

# Add sample members
library.register_member(Member(1, "John Doe"))
library.register_member(Member(2, "Jane Smith"))









    