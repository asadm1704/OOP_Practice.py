'''Create a SecureBankAccount class that:

Has private attributes: _account_number, _balance, _pin
(use single underscore convention for protected, double for truly private if needed)

Provides public methods to:

deposit(amount) - add to balance

withdraw(amount, pin) - subtract if pin matches

check_balance(pin) - return balance if pin matches

change_pin(old_pin, new_pin) - change PIN

Add validation:

Balance can't go negative

PIN must be 4 digits

Deposit/withdrawal amounts must be positive'''
class SecureBankAccount:


    
    def __init__(self,account_number,balance,pin):
        self.__account_number=account_number
        self.__balance=balance
        self.__pin=pin


    
    def set_pin(self, pin):
        """Validate and set PIN"""
        if isinstance(pin, str) and pin.isdigit() and len(pin) == 4:
            self.__pin = pin
        else:
            raise ValueError("PIN must be 4 digits")

    def deposit(self,amount):
        if amount>0:
          self.__balance=amount +self.__balance
        else:
            print("Deposit amount must be positive")

    def __verifypin(self,pin):
      if self.__pin==pin:
          return True
      else:
          return False


    def withdraw(self, amount, pin):
        """Withdraw only if the PIN matches and funds are sufficient."""
        if not self.__verifypin(pin):
            print("Invalid PIN")
            return

        if amount > 0:
            if amount <= self.__balance:
                self.__balance = self.__balance - amount
            else:
                print("Insufficient balance")
        else:
            print("Withdrawal amount must be positive")

    def check_balance(self, pin):
        """Return balance only if the PIN matches."""
        if self.__verifypin(pin):
            return self.__balance
        else:
            print("Invalid PIN")
            return None
    def change_pin(self, old_pin, new_pin):
        """Change PIN if old PIN matches and new PIN is valid."""
        if not self.__verifypin(old_pin):
            print("Invalid old PIN")
            return

        if isinstance(new_pin, str) and new_pin.isdigit() and len(new_pin) == 4:
            self.__pin = new_pin
        else:
            print("New PIN must be 4 digits")



# Expected usage:
acc = SecureBankAccount("123456", 1000, "1234")
print(acc.check_balance("1234"))  # 1000
acc.deposit(500)
acc.withdraw(200, "1234")
print(acc.check_balance("1234"))  
acc.withdraw(1500, "1234")  
acc.check_balance("9999")  



'''Create a Temperature class that:

Stores temperature privately in Celsius

Provides getter/setter methods with validation:

set_celsius(temp) - can't be below absolute zero (-273.15°C)

set_fahrenheit(temp) - converts to Celsius

set_kelvin(temp) - converts to Celsius

get_celsius(), get_fahrenheit(), get_kelvin()

Add property decorators for Pythonic encapsulation

Temperature should always be valid (no invalid states possible)'''

class Temperature:
    def __init__(self, celsius=0):
        self.set_celsius(celsius)

    def set_celsius(self, temp):
        if temp < -273.15:
            raise ValueError("Temperature cannot be below absolute zero (-273.15°C)")
        self.__celsius = temp

    def set_fahrenheit(self, temp):
        celsius = (temp - 32) * 5.0 / 9.0
        self.set_celsius(celsius)

    def set_kelvin(self, temp):
        celsius = temp - 273.15
        self.set_celsius(celsius)

    def get_celsius(self):
        return self.__celsius

    def get_fahrenheit(self):
        return (self.__celsius * 9.0 / 5.0) + 32

    def get_kelvin(self):
        return self.__celsius + 273.15

    celsius = property(get_celsius, set_celsius)
    fahrenheit = property(get_fahrenheit, set_fahrenheit)
    kelvin = property(get_kelvin, set_kelvin)

temp = Temperature(25)  
print(temp.celsius)     
print(temp.fahrenheit)  
print(temp.kelvin)      

temp.fahrenheit = 100   
print(temp.celsius)     

temp.celsius = -250    


'''Exercise 3: Student Record with GPA Calculation
Create a Student class that:

Has private attributes: _name, _id, _grades (list of grades)

Provides controlled access through methods:

add_grade(grade) - adds grade (0-100), automatically updates GPA

remove_grade(index) - removes grade at index

get_gpa() - returns calculated GPA (A=4.0, B=3.0, etc.)

get_transcript() - returns formatted transcript

GPA should be calculated on demand, not stored

Grades should be validated (0-100 range)

Name and ID should be immutable after creation'''
class Student:
    def __init__(self, name, student_id):
        self.__name = name
        self.__id = student_id
        self.__grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grades.append(grade)   #append grade to the list
        else:
            print("Grade must be between 0 and 100")

    def remove_grade(self, index):
        if 0 <= index < len(self.__grades):
            self.__grades.pop(index)
        else:
            print("Invalid index")

    def get_gpa(self):
        if not self.__grades:
            return 0.0
        total_points = 0
        for grade in self.__grades:
            if grade >= 90:
                total_points += 4.0
            elif grade >= 80:
                total_points += 3.0
            elif grade >= 70:
                total_points += 2.0
            elif grade >= 60:
                total_points += 1.0
        return total_points / len(self.__grades)

    def get_transcript(self):
        transcript = f"Transcript for {self.__name} (ID: {self.__id}):\n"
        for i, grade in enumerate(self.__grades):
            transcript += f"  Grade {i + 1}: {grade}\n"
        transcript += f"GPA: {self.get_gpa():.2f}"
        return transcript


# Expected usage:
student = Student("Alice Johnson", "S12345")
student.add_grade(95)
student.add_grade(87)
student.add_grade(92)
student.add_grade(78)

print(f"GPA: {student.get_gpa():.2f}")  # GPA: 3.25
print(student.get_transcript())

# Try invalid grade
student.add_grade(105)  # "Grade must be between 0 and 100"

# Remove a grade
student.remove_grade(3)  # Removes 78
print(f"GPA after removal: {student.get_gpa():.2f}")  # GPA: 3.67
