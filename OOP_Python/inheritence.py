'''Exercise 1: Basic Inheritance - Vehicles
Create a base class Vehicle with:

Attributes: brand, model, year

Method: start_engine() that prints "Engine started"

Method: get_info() that returns brand, model, and year

Then create two subclasses:

Car that adds:

Attribute: num_doors

Overrides start_engine() to print "Car engine started: Vroom!"

Motorcycle that adds:

Attribute: has_sidecar (boolean)

Overrides start_engine() to print "Motorcycle engine started: Brrrrm!"'''
class Vehicle:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year

    def start_engine(self):
       print('engine started')

    def get_info(self):
        return  f"{self.model}  {self.brand} {self.year}"

class Car(Vehicle):
    def __init__(self, brand, model, year,num_doors):
    
       super().__init__(brand,model,year)
       self.num_doors=num_doors
    def start_engine(self):
        print('car engine staretd vroon!')


class MotorCycle(Vehicle):
    def __init__(self, brand, model, year,has_sidecar):
        super().__init__(brand, model, year)
        self.has_sidecar=has_sidecar

    def start_engine(self):
        print('motorcycle engine started wroom ')

my_car =Car('toyota','GLI','2012','4')
print(my_car.year)
print(my_car.start_engine())
# Expected output:
car = Car("Toyota", "Camry", 2020, 4)
bike = MotorCycle("Harley", "Sportster", 2021, False)

car.start_engine() 
bike.start_engine() 
print(car.get_info()) 
print(f"Doors: {car.num_doors}") 


#EXAMPLE FOR MULTILEVEL

'''Create a class hierarchy for employees:

Base class Employee with:

Attributes: name, employee_id, salary

Method: work() that prints "[name] is working"

Method: get_details() returns basic info

Manager inherits from Employee and adds:

Attribute: team_size

Overrides work() to print "[name] is managing a team"

Method: conduct_meeting() prints "[name] is conducting a meeting"

Developer inherits from Employee and adds:

Attribute: programming_language

Overrides work() to print "[name] is writing code"

Method: debug() prints "[name] is debugging code"'''

class Employee:
     def __init__(self,name,employee_id,salary):
         self.name=name
         self.employee_id=employee_id
         self.salary=salary

     def work(self):
        return  f"{self.name} is working"

     def get_details (self):
         return  f"{self.name} {self.employee_id} {self.salary}"

class Manager(Employee):

    def __init__(self, name, employee_id, salary,team_size):
        super().__init__(name, employee_id, salary)
        self.team_size=team_size

    def work(self):
        return  f"{self.name}  is managing a team"

    def conduct_meeting(self):
        return  f"{self.name} is conducting a meeting"


class Developer(Employee):
    def __init__(self, name, employee_id, salary,programming_language ):
        super().__init__(name, employee_id, salary)
        self.programming_language =programming_language

    def  work(self):
        return  f"{self.name}  is writing code"

    def debug(self):
        return  f"{self.name} is debugging code"
# Expected usage:
# Expected output:
manager = Manager("Alice", "M001", 80000, 5)
dev = Developer("Bob", "D001", 70000, "Python")

print(manager.work())  # "Alice is managing a team"
print(dev.work())      # "Bob is writing code"
print(manager.conduct_meeting())  # "Alice is conducting a meeting"
print(dev.debug())     # "Bob is debugging code"



'''Create classes to represent smart devices:

Phone class with:

Attributes: phone_number, network

Method: call(number) prints "Calling [number]"

Method: send_sms(message, number)

Camera class with:

Attributes: megapixels, zoom_level

Method: take_photo() prints "Photo taken"

Method: record_video() prints "Recording video"

Smartphone class that inherits from both Phone and Camera:

Attribute: os (operating system)

Method: install_app(app_name) prints "Installing [app_name]"

Should be able to use all methods from both parent classes'''

class Phone:
    def __init__(self,phone_number,network):
        self.phone_number=phone_number
        self.network=network

    def call(self,number):
        print(f"calling {number}")

    def send_sms(self,message,number):
        print(f"sending sms to {number} with message {message}")

class Camera:
    def __init__(self,megapixels,zoom_level):
        self.megapixels=megapixels
        self.zoom_level=zoom_level

    def take_photo(self):
        print("Photo taken")

    def record_video(self):
        print("Recording video")

class Smartphone(Phone,Camera):
    def __init__(self,phone_number,network,megapixels,zoom_level,os):
        Phone.__init__(self,phone_number,network)
        Camera.__init__(self,megapixels,zoom_level)
        self.os=os

    def install_app(self,app_name):
        print(f"Installing {app_name}")

# Expected output:
phone = Smartphone("123-456-7890", "5G", 12, 3.0, "Android")
phone.call("987-654-3210")  # "Calling 987-654-3210"
phone.take_photo()          # "Photo taken"
phone.install_app("WhatsApp") # "Installing WhatsApp"
print(f"OS: {phone.os}")    # "OS: Android"
        
        
       
         




    
        
        
    
    
    
       