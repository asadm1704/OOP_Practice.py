
'''   Create a Book class with:

__init__ method that takes title and author as parameters

A method get_info() that returns "Title: [title], Author: [author]"

A method is_long() that returns True if title has more than 10 characters, False otherwise

python
'''
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def get_info(self):
        return f"Title: {self.title}, Author: {self.author}"
    
    def is_long(self):
        return len(self.title) > 10


# Expected usage:
book1 = Book("Harry Potter", "J.K. Rowling")
print(book1.get_info())  # "Title: Harry Potter, Author: J.K. Rowling"
print(book1.is_long())   # True (13 characters)

'''Create a BankAccount class with:

__init__ method that takes account_holder (sets balance to 0)

deposit(amount) method that adds to balance

withdraw(amount) method that subtracts from balance (but not below 0)

check_balance() method that returns current balance

transfer(amount, other_account) method that transfers money to another BankAccount object'''
class BankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds!")
    
    def check_balance(self):
        return self.balance
    
    def transfer(self, amount, other_account):
        if amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount

# Expected usage:
alice_account = BankAccount("Alice")
bob_account = BankAccount("Bob")

alice_account.deposit(1000)
alice_account.withdraw(200)
alice_account.transfer(300, bob_account)

print(alice_account.check_balance())  # 500
print(bob_account.check_balance())    # 300


'''Create a Product class with:

__init__ method that takes name, price, and quantity

buy(quantity_to_buy) method that reduces quantity if available

restock(quantity_to_add) method that increases quantity

is_available() method that returns True if quantity > 0

get_total_value() method that returns price × quantity

A class variable total_products that counts how many Product objects exist

python
# Expected usage:
phone = Product("iPhone", 999.99, 10)
laptop = Product("MacBook", 1499.99, 5)

phone.buy(3)  # Buy 3 iPhones
laptop.restock(2)  # Add 2 more MacBooks

print(phone.quantity)  # 7
print(laptop.is_available())  # True
print(Product.total_products)  # 2 (should count all objects)'''
class Product:
    total_products = 0  # Class variable
    
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        Product.total_products += 1  # Increment counter
    
    def buy(self, quantity_to_buy):
        if quantity_to_buy <= self.quantity:
            self.quantity -= quantity_to_buy
        else:
            print(f"Only {self.quantity} available!")
    
    def restock(self, quantity_to_add):
        self.quantity += quantity_to_add
    
    def is_available(self):
        return self.quantity > 0
    
    def get_total_value(self):
        return self.price * self.quantity

phone = Product("iPhone", 999.99, 10)
laptop = Product("MacBook", 1499.99, 5)

phone.buy(3)  # Buy 3 iPhones
laptop.restock(2)  # Add 2 more MacBooks

print(phone.quantity)  # 7
print(laptop.is_available())  # True
print(Product.total_products)  # 2 (should count all objects
        