class Book:
    def __init__(self,unique_id,title,borrowing_status =False):
        self.unique_id=unique_id
        self.title=title
        self.borrowing_status =borrowing_status

class Member:
    def __init__(self,unique_id,register=True):
        self.unique_id =unique_id
        self.borrowed_books=[]
        self.register=register
class Library:
    def __init__(self):
        self.books=[]
        self.members=[]
    def add_book(self,book):
        self.books.append(book)
    def register_member(self,member):
        if member.register == True:
            self.members.append(member)
            return "registered"
    def borrow_book(self,book,member):
        if book.borrowing_status == False:
            if member.register ==True:
                if book not in member.borrowed_books:
                    if len(member.borrowed_books)<3:
                        member.borrowed_books.append(book)
                        print("book borrowed successfully")
                        book.borrowing_status=True
    def return_book(self,book,member):
        if book in member.borrowed_books:
            member.borrowed_books.remove(book)
            print ("book successfully returned")
            book.borrowing_status= False
    def display(self,member):
        for book in member.borrowed_books:
            print(book.title,book.unique_id,"the  book borrowed by",member.unique_id)
    def available_books(self):
        for book in self.books:
            if book.borrowing_status ==False:
                print(book.title,book.unique_id)

book1=Book("b-143","python basics")
book2=Book("b -555","java basics")
member1=Member("m-999")
member2=Member("m-777")
library=Library()
library.add_book(book1)
library.add_book(book2)
library.register_member(member1)
library.register_member(member2)
library.borrow_book(book1,member1)
library.borrow_book(book2,member2)
library.return_book(book1,member1)
library.display(member2)
library.available_books()







    
# Day8
