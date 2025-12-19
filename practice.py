'''Using following list of cities per country,
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
Write a program that asks user to enter a city name and it should tell which country the city belongs to



city=input('please enter your city name :')
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
if city in india:
    print('the given city exists in india ')
elif city in pakistan:
    print("city is in pakistan")
elif city in bangladesh:
    print('the given city is from bangladesh')
else :
    print('you have enteres a city that i dont know sorry ')
    '''
'''
Write a program that asks user to enter two cities and it tells you if they both are in same country or not. For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country"
city1=input('please enter your  1st city name :')
city2=input ('please enter your second city name :' )
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
if city1 and city2 in india:
    print ('both are from india')
elif city1 and city2 in pakistan:
    print('both cities are from paksitan')
elif city1 and city2 in bangladesh:
    print('both cites are from bangldaesh')
elif city1 or city2 not in india or pakistan or bangladesh:
    print ('the given city i dont know about that ')
else:
    print ('the cities are not from the same countries')'''

'''
Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
Ask user to enter his fasting sugar level
If it is below 80 to 100 range then print that sugar is low
If it is above 100 then print that it is high otherwise print that it is normal


level = int(input('please enter you sugar level  :'))
if level in range(80,101):
    print ('your sugar level is low bro')
elif level >100 :
    print('sugar level is high ')
else :
    print('your sugar is normal bro just chill and relax')    '''

    #FUNCTION PRACTICE SESSION
'''Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is,
area = (1/2)*base*height'''
'''def calculate_area(base,height):
    area=(1/2)*base*height
    return area

result = calculate_area(10,20)
print(result)'''
'''Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,
rectangle area=length*width'''

'''def calculate_area(base,height,shape):
    
    if shape =='triangle':
     area=(1/2)*base*height
     return area
    elif shape == 'rectengle':
     area =base*height
     return area
    else :
        print('please choose triangle or rectengle cz i have these two only')
    
base=int(input('please enter the base value  :'))
height=int(input('please enter the height value  :'))
shape=input('please enter the shape to perform calculation according to it  :')

result = calculate_area(base,height,shape)
print(result)'''

'''Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
*
**
***
if input is 4 then it should print

*
**
***
****
Basically number of lines it prints is equal to that number. (Hint: you need to use two for loops)

'''

'''def print_pattern(number):
    for i in range(number):
    
        s=''
        for j in range(i+1):
            s=s+'*'
            return s
        result=int(input('please enter input number for stars  '))
        print_pattern(result)
        print(result)'''

'''result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
count=0
for i in result:
    if i == 'heads':
        count=count+1
print(count)    '''

'''
for i in range(1,11):
    if i % 2==0:
        continue
    else:
       print(i*i)
   '''
'''month_list = ["January", "February", "March", "April", "May"]
expense_list = [2340, 2500, 2100, 3100, 2980] 
result=int(input('please input your expenses :'))
month =-1   
for i in range(len(expense_list)):
    
    if result==expense_list[i]:
        month=i
    print('the given expense has been found and it was of month  :',month)
    break
else :
    print('the expense wasent found there')'''


'''for i in range(5) :
 choice=input('are you tired :')
 if choice=='yes':
     print('you didnt finish the race')
     break
 elif choice=='no':
     continue

print ('congrates you have finished the race ')'''


'''info={'china':143,'india':136,'USA':32,'pakistan':21}

def query():
    qu=input('sk user for which country he or she wants to query').lower()
    if qu not in info:
        print('the country you entered does not exists in the dic')
        return
    else:
        print('the countryvinfo you looking for is ',info[qu])
        
    
def add():
     countinput=input('please add the country name :')
     if countinput in info:
         print('you have already entered a country that exists in the list')
         return
     
     else:
        popinput=input('please add the country population :')
        info[countinput]=popinput
        print('the new country has been added to the dictionary')
        print('the dict is ',info)
def deletee():
     countinput=input('please add the country name to delete:')
     if countinput not in info:
         print('the country you entered soes not exist in the dict so no need for the deletion')
         return
     
     elif  countinput in info:
        del info[countinput]
        print('the new country has been deletd from the dictionary')
        print('the dict is ',info)

def main():
    print('hey this is a country practice dictionary practice session')
    choice =input('please input your choice "add",  "delete" ,  "query" ')
    if choice=='add':
        add()
    elif choice =='delete':
        deletee()
    elif choice=='query':
        query()
        
if __name__ == "__main__":
    while True:
        should_restart = main()
        
        # Ask if user wants to restart
        restart = input("\nDo you want to restart the program? (yes/no): ").lower().strip()
        if restart in ['yes', 'y', 'yeah', 'yep']:
            print("\n" + "=" * 50)
            print("Restarting program...")
            print("=" * 50)
            continue  # Go back to start of while loop
        else:
            print("Program terminated. Have a nice day!")
            break  # Exit the outer lo'''
     
     