class Book:
    def __init__(self, book_id, title, author, quantity):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__quantity = quantity

    def __str__(self):
        return f"Book Id: {self.__book_id}, Book Title: {self.__title}, Author: {self.__author}, Quantity: {self.__quantity}"

    @property
    def title(self):
        """Function get title of book."""
        return self.__title
    
    @property
    def author(self):
        """Function get title of book."""
        return self.__author
    
    @property
    def quantity(self):
        """Function get quantity of book."""
        return self.__quantity
    
    @property
    def book_id(self):
        """Function get book id of book."""
        return self.__book_id

    @book_id.setter
    def book_id(self, book_id):
        self.__book_id = book_id

    @title.setter
    def title(self, title):
        self.__title = title
    
    @author.setter
    def author(self, author ):
        self.__author = author
    
    @quantity.setter
    def quantity(self, quantity):
        self.__quantity = quantity

    def check_availability(self):
        """Function check if book quatity is avaliable."""
        return self.quantity > 0
    
    def update_quantity(self, quantity):
        """Function update book quantity"""
        self.quantity += quantity