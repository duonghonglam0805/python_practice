from book import Book 
from user import User

class Library:
    def __init__(self):
        self.__list_books = []  
        self.__list_users = []  

    @property
    def list_books(self):
        """Function get list books in Library."""
        return self.__list_books
    
    @list_books.setter
    def list_books(self, books):
        self.__list_books = books
    
    @property
    def list_users(self):
        """Function get list users in Library."""
        return self.__list_users
    
    @list_users.setter
    def list_users(self, users):
        self.__list_users = users
    
    def add_new_user(self, use):
        """Function add new user to the list of user."""
        self.__list_users.append(use)

    def add_new_book(self):
        """Function add new book to the list of book."""
        while True:
            try:
                book_id = int(input("Enter book Id: "))
                break
            except ValueError:
                print("Invalid book id:(((. Please enter number!")
        while True:
            if any (book.book_id == book_id for book in self.list_books):
                print("Book with the same id already exists, Please enter another ID")
                book_id = int(input("Enter book Id: "))
            else:
                break  

        title = input("Enter book title: ")
        author = input("Enter author name: ")
        while True:
            try:
                quantity = int(input("Enter the quatity of books: "))
                break
            except ValueError:
                print("Invalid quantity:(((. Please enter number!")
        new_book = Book(book_id, title, author, quantity)
        self.__list_books.append(new_book)

    def finding_book(self, title):
        """Function search book from library"""
        return[book for book in self.__list_books if title.lower() in book.title.lower()]  
    
    def display_book_list(self, list_books):
        """Function show book lists"""
        for i, b in enumerate(list_books):
                print(i+1,b)

def main():
    library = Library()

    book1 = Book(1, "Mua Do", "Ta", 5)
    book2 = Book(2, "Mai", "Tran Thanh", 3)
    book3 = Book(3, "Viet Tiep Cau Chuyen Hoa Binh", "Ha Tram", 2)
    book4 = Book(4, "Viet Tiep Cau Chuyen Hoa Binh1", "Ha Tram1", 3)

    user1 = User(1, "Nguyen Van A", "nguyenvana@gmail.com")
    user2 = User(2, "Duong Thi B", "duongthib@gmail.com")
    user3 = User(3, "Nguyen Duc C", "nguyenducc@gmail.com")
    user4 = User(4, "Ho Thi D", "hothid@gmail")

    library.list_books = [book1, book2, book3, book4]
    library.list_users = [user1, user2, user3, user4]

    list_books = library.list_books

    print("Welcome HL library: \n 1: View List of books in my library \n 2: Add new book \n 3: Search a book \n 4: Borrow a book \n 5: Return a book \n 6: View list of borrowed book \n 6: Exits")
    while True:
        try:
            number = int(input("Please choose your service: "))
            match number: 
                case 1:
                    print("_________________________________________________________________________")
                    print("List of books:")
                    library.display_book_list(list_books)
                    # library.display_book_list(list_users)
                case 2:
                    print("______________________________________________________________________________________________________")
                    print("Please enter book information:")
                    library.add_new_book()
                    print("List of books after adding new book:")
                    library.display_book_list(list_books)
                case 3:
                    print("______________________________________________________________________________________________________")
                    print("Do you search a book? Please enter your book that you want to search.")
                    search_word = input()
                    list_result = []
                    result = library.finding_book(search_word)
                    if result:
                        print("This is the list of book use might need:")
                        list_result.extend(result)
                        library.display_book_list(list_result)
                    else:
                        print("Ohhh ohh :(((.No books were found!")
                case 4:
                    print("______________________________________________________________________________________________________")
                    print("Hello:)). Do you want to borrow a book?")
                    user_id = int(input("Enter your user ID: "))
                    book_id = int(input("Enter the book ID to borrow: "))
                    user = next((u for u in library.list_users if u.user_id == user_id), None)
                    book = next((b for b in library.list_books if b.book_id == book_id), None)
                    if user and book:
                        user.borrow_book(book)
                        print("List of remaining book:")
                        library.display_book_list(list_books)
                    else:
                        print("Ohh:((.Invalid user or book ID!")

                case 5:
                    while True:
                        print("______________________________________________________________________________________________________")
                        print("Hello!, Do you want to return the book?")
                        try:
                            user_id = int(input("Enter your user ID: "))
                            book_id = int(input("Enter the book ID to return: "))

                            user = next((u for u in library.list_users if u.user_id == user_id), None)
                            book = next((b for b in library.list_books if b.book_id == book_id), None)
                            if user and book:
                                user.return_book(book)
                                break
                            else:
                                print("Ohh:((.User id or book id dose not exists!")
                        except ValueError:
                            print("Invalid user id or book id:(((! Please enter number!")
                case 6:
                    while True:
                        print("______________________________________________________________________________________________________")
                        print("Hello!, Do you want to view list of borrowed book?")
                        try:
                            user_id = int(input("Enter your user ID: "))
                            user = next((u for u in library.list_users if u.user_id == user_id), None)
                            if user:
                                user.view_borrowed_books()
                                break
                            else:
                                print("Ohh:((.User id dose not exists!")
                        except ValueError:
                            print("Invalid user id:(((! Please enter number!")
                case 7:
                    print("______________________________________________________________________________________________________")
                    print("Thank you!")
                    break
        except ValueError:
            print("Invalid number:(((! Please enter number!")

if __name__ == "__main__":
    main()

