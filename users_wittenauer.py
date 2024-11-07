class User: 
    def __init__(self, first_name, last_name, age, city):
        #Initialize first name, last name, age, and city attributes
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city

    def describe_user(self): 
        #prints a summary of the user's information
        print(f"{self.first_name} {self.last_name} is {self.age} years old and is from {self.city}.")

    def greet_user(self):
        #prints a personalized greeting to the user
        print(f"Hello {self.first_name} {self.last_name}. How are you?")

user = User('Will','Wittenauer',16,'Smithton')
user.describe_user()
user.greet_user()

user = User('John','Smith', 52,'Boston')
user.describe_user()
user.greet_user()

user = User('Albert','Einstein', 68,'New York')
user.describe_user()
user.greet_user()
print()