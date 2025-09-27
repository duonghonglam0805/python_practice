class User:
    def __init__(self, user_id, name, email):
        self.__user_id = user_id
        self.__name = name
        self.__email = email
        self.__borrowed_books = []

    def __str__(self):
        return f"Name: {self.__name}, email: {self.__email}"
    
    @property
    def user_id(self):
        """Function get user id of user."""
        return self.__user_id

    @user_id.setter
    def user_id(self, user_id):
        self.__user_id = user_id

    @property
    def name(self):
        """Function reture name of user."""
        return self.__name
    
    @name.setter
    def name(self, name):
        """Function set name of user."""
        self.__name = name

    @property
    def email(self):
        """Function reture email of user."""
        return self.__email
    
    @email.setter
    def email(self, email):
        """Function set email of user."""
        self.__email = email

    @property
    def borrowed_books(self):
        return self.__borrowed_books

    @borrowed_books.setter
    def borrowed_books(self, borrewed_books):
        self.__borrowed_books = borrewed_books
    
    def borrow_book(self, book):
        """Function borrow book."""
        if book.check_availability():
            self.borrowed_books.append(book)
            book.update_quantity(-1) 
            print(f"{self.name} has borrowed '{book.title}'")
        else:
            print(f"Sorry, '{book.title}' is not available for borrowing.")
    
    def return_book(self, book):
        """Function return book."""
        if book in self.__borrowed_books:
            self.__borrowed_books.remove(book)
            book.update_quantity(1)
            print(f"{self.name} has returned '{book.title}'")
        else:
            print(f"{self.name} does not have '{book.title}' borrowed.")

    def view_borrowed_books(self):
        """Function view borrowed book"""
        if self.__borrowed_books:
            print(f"{self.name}'s Borrowed Books:")
            for book in self.__borrowed_books:
                print(f" - Book id: {book.book_id}, Book title: {book.title}, Author: {book.author}")
        else:
            print(f"{self.name} has not borrowed any books.")

    

