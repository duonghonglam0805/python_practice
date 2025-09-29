import re
from datetime import datetime

class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth
        self.age = 0

    def __str__(self):
        return f"Name: {self.name}, Country: {self.country}, Date of birth: {self.date_of_birth}, Age: {self.age}."

    def calculate_age(self, date_of_birth):
        """Function for calculating age of person."""
        if not re.match(r"^\d{2}/\d{2}/\d{4}$", date_of_birth):
            raise ValueError("date_of_birth must be in format dd/mm/yyyy")
        year_of_birth = int(date_of_birth.split("/")[2])
        current_year = datetime.now().year
        self.age = current_year - year_of_birth
        return self.age
    
def main():
    person = Person("Lam","Viet Nam", "15/08/2000")
    person.calculate_age(person.date_of_birth)
    print(person) 

if __name__ == "__main__":
    main()