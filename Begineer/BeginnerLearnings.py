## checking if the environment is working / not.
'''print("Hello World")
print("This will be marking all the practice scripts and learnings related to python");
resources = "https://www.udemy.com/share/103J8C3@5X4F98BK-9gGlp3buD_tyLnpMinHJvQmUdsLddBftMp9ESSx2lcl2JJoqULUzSZl/"
print(resources);'''
###########################################################################################################################################
## Day 1 :- Printing, Commenting, Debugging, String Manupiulation and Variable Names.######################################################
## print => used to print your onto the console. Pretty useful for debugging at timees
## String => set of characters or say an array of characters;
## Syntax error => its generally indicated with red. tells you that you have messed up 
## so check your code again. 
'''print(hello world)'''
## here you can see that we did not enclose HELLO WORLD in double quotes hence we are getting an error here
## resources to go to when we make errors 1) Stack OverFlow and 2) ChatGPT/Gemini
## This is Typically how print statements are used here
'''print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
print("2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes.")'''


## String Manipulations ##
## to print things multiple times we can either used multiple print statements/use 1 print statemrnt and write the contents with 
## an escape character => '\n' or use a Loop (which is what sane people do);

## Method1.
'''print("Hi")
print("Hi")
print("Hi")'''

## Method2 => in this method we are using string manupilation.
'''print("Hi\nHi\nHi");'''

## Method3.
'''for i in range(0,1,3):
    print("Hi\n")'''

## String Concatenation => taking separate strings and merging them into one.
## Example:-
'''firstName = "Mukund"
secondName = "Khamampati"
fullName = "Mukund"+" "+"Khamampati" ## here two strings are being concatenated.
print(fullName)'''
## In compiled langugaes like C,C++ and C# (These are the ones I have stidied earlier)
## '{}' indicate the start and end of a given block of code.
## in python indentation which is a 'TAB' space is something similar to that .
## been demonstrated in Method3


## Taking User Input
'''print("Please give me some input") ## this is for printing on the console
variable = input("Please provide a valid input:- ")## this is you input and storing it in varibale
print(variable)'''
## here we use variable ; think of it as a container or say a BOX
## in compiled languages the variable 's data type must be defined but here its
## not needed. Python is an interpretter based language meaning here 
## since I am on a linux system the BASH has an built "python3" interpretter which 
## runs script "Learnings.py" in my case.
## Naming can be done in the follwing conventions
## 1) Camel Case 2) Snake Case 3) Pascal Case and I will be following camel case 
## Variable Names must actually make sense and there must be a reason to call a variable
## a certain way 
## swaping to number/entities with a 'temp variable
'''glass1 = "milk"
glass2 = "juice"
print(glass1,glass2)
temp = glass1
glass1 = glass2
glass2 = temp
print(glass1,glass2)'''
## while declaring variable we do not use 'var' like we do while we declare dynamic type 
## variables in C#

### Small Project :- BAND NAME GENERATOR##
'''print("Welcome to a Band Name Generator")
City  = input("Enter the city that you have grown up in:- " )
Pet_Name = input("Enter a pet NAME :- ")
BandName = City+" "+Pet_Name
print(f"You band name is {BandName}") ## this is an fstring'''
######################################################################################
## Day 2 => Data Types, Numbers, Operators, Type Conversion , f-strings ##############
## using the len() method we can get the number of characters in a string 
## Example:- 
'''char_len = len(input("Enter a string:- "));
print(f"Total character count {char_len}")'''
## Data Types :- 
## 1) String, 2) Integers, 3) Floats 4) Booleans

##strings => collection of characters => 
'''String = "Khamampati"
print(String[0]) ## this will give is the first letter of a string 
## string / array indexing starts with 0 
print(String[0:3])## gives you the first 3 characters in the said string
print(String[0:5:2])## gives you 3 characters such that there is a gap of 1 
## character in between each
print(String[-1])## when we use negative indices we are getting the string from the 
## reverse order so here i will be the result
print(String[-5:-1])## from the last 5th index to the last index this is how it works 
## Print behaviour ##
print("123"+"124")## concatenating 2 strings
print(123+124)## adding 2 numbers
print("123"+123)## here you must get a type error because you are trying to add a
## string and an integer which is incorrect because of the way they are occupied in the 
## memory.
print(12345+123.5)## here you can see that the int is being converted into float 
## and the addition takes place this is what we call upcasting and this is done
## by the interpretter.
print(12345 + int(12345.123))''' ## This is called downcasting becausr we are 
## explicitely tellling the interpretter to convert the float number into integer 
## effectively ignoring the decimal part of the equation.

## FUNCTION / METHODS => pretty simple a re-usable piece of code 
## You have input arguements and output.
'''print(type("Error"))
print(type(12345))
print(type(12.334))
print(type(True))'''
## type() is used to determine the data type of a variable / constant
## Operators in Python 
## '+,-,*,/,%',// => these are the arithematic operators 
## 'and, or,!' => Logical operators
## '>,<,=,=>,<=,!=' => relational operators
## '==' => asignment operatoes
## '**' this is generally for indicating power off
## all of these have a certain priority order and PEMDAS is something we use
## for mathematic operators 
## A Example :- Calculating the body mass index of a person
'''
height = float(input("Enter your height in meters:- "))
weight = float(input("Enter you weight in kilograms:- "))
bmi =((weight)/(height*height))
isUnhealthy = False
print(f"Your BMI is => {bmi}")
if(bmi>25.0 and bmi<29.9):
    print("You are over-weight")
    isUnhealthy =True
elif(bmi>18.5 and bmi<24.9):
    print("You are having a healthy weight")
elif(bmi>30.0):
    print("You are obese")
elif(bmi<18.5):
    print("You are underweight")
    isUnhealthy = True
## This is a condition to see if the given person needs to see a doc
if(isUnhealthy == True):
    print("Please see a doctor");
'''
## Mini Project :- Creating a tip calculator 
'''
totalAmount = float(input("Please enter the total bill:- "));
isSplit = False;
toTip = bool(input("Do you want to tip the person? yes :- type 1 +Enter  no :- press Enter:- "))
if(toTip == True):
    tipPercentage = int(input("Please enter the tip percentage:- "))
    totalAmount = totalAmount*(tipPercentage/100) + totalAmount
    print(totalAmount);

toSplit = bool(input("Do you want to split the bill? yes :- type 1 +Enter  no :- press Enter:- "))
if(toSplit == True):
    split = int(input("How many people to split the bill:- "))
    isSplit = True
    totalAmount = totalAmount/split
    print(totalAmount)

if(isSplit == True):
    print(f"the amount per person amounts to  {totalAmount}");
else:
    print(f"Total amount to be paid is {totalAmount}")
'''
############################################################################################################
## Day 3 :- Control Statement and logical operators, Code blocks and Scope
## For conditional statements we use "if,else and elif"
## the program written above is a excellent example of how we write Control Statements
## example1:- getting a drivers licence 
'''
Age = int(input(" PLease enter age:- "))
IsInterested = bool(input("Are you interested to get your licence? 1+Enter=> Yes / Enter for No:- "))
if(IsInterested == True):
    if(Age>=18):
        print("You are eligible for your applying for your drivers licence")
    else:
        print(f"You are still a minor apply after {18-Age} year/years")
else:
    print("Thankyou for attending the survey")
'''
# Example 2:- digit related operations 
'''number = int(input("PLease enter a number"))
if(number%10 == 0):
    print("The number you have selecected is a single digit one")
else:
    count = 0
    sum = 0
    print(f"number specified {number} is even ")if number%2 == 0 else print(f"number specified {number} is odd")
    while number >0:
        sum = sum + number%10
        count = count+1
        number = number//10
    print(f"Number of digits present in the given number is {count}, sum of all digits is {sum}")
'''
## Nested if statements => an if statement present inside an if statement is what we call a nested of statement
## Example :- Fare Charges 
## Condition :- if the age of a person is 18 and able her can get on the fare
## and second contition is if he has luggage he will have to pay 2 dollars per Kg
'''
print("Welcome of Raw and Rustic Ferry services")
Age = int(input("Please enter your age:- "))
Price = 0
if(Age >18):
    Price = 12
    IsBaggage = bool(input("Is there any luggage?\n1+Enter=> Yes / Enter for No:- "))
    if(IsBaggage == True):
        weight = int(input("Please enter weight in Kg"))
        Price = Price + weight*2
    print(f"Total amount that has to be paid is {Price}");
else:
    print("You need to be accompanied with an adult")
'''
## if/else/elif Vs Multiple if's
## 1) In the first case we are veryfing all the conditions : the ladder is not further
## evaluated when one of the conditions is met
## 2) In the second case all the cases ARE VERIFIED irrespective of which condition is matched 
# Examole :- Ride fare 
# Condition : based on height/age and if they want photographs to be made
'''
print("Welcome to Wonderla")
height = float(input("Enter your height in cm:- "))
totalAmount = 0
if(height>=120):
    Age = int(input("Please Enter your age:- "))
    if(Age<12):
        print("Please pay $5")
        totalAmount +=5
    elif(Age>18 and not(Age>=45 and Age<=55)): ## here we have incorporated a condiion where we are giving out free tickects for 
        ## for people in a certain age group
        print("Please pay $15")
        totalAmount += 15
    elif(Age>=12 and Age<=18):
        print("Please pay $10")
        totalAmount +=10
    elif(Age>=45 and Age<=55):
        print("Your tickets are free enjoy your midlife crises")
        totalAmount = 0
    isPhotograph = input("Do you want to take a photograph? Y/N:- ")
    if(isPhotograph == "Y" or isPhotograph == "y"):
        print("Please pay 3 dollars per photograph")
        photoNumber = int(input("Enter number of Photographs:- "))
        totalAmount += photoNumber*3
    print(f"Your total cost has come to {totalAmount}")
else:
    print("You are too short to ride!!")
'''
## Pizza delivary Program
## Condtion :- 
## Small Pizza => $15
## Medium Pizza => $20
## Large Pizza => $25
## Extra toppings => $5
## Home Delivery/take away
'''
totalAmount = 0
print("Welcome to Jabba the Pizza!")
size = input("Please enter the pizza size?\n S,M or L:- ")
if(size =="M" or size == "m" ):
    totalAmount = 20
elif(size == "S" or size == "s"):
    totalAmount = 15
elif(size == "L" or size == "l"):
    totalAmount = 25
print(f"cost:- {totalAmount}")
isExtraToppings = input("Do you want extra toppings?\n Y/N :- ")
if(isExtraToppings == "Y" or isExtraToppings == "y"):
    totalAmount = totalAmount + 5
print(f"Cost = {totalAmount}")
isDelivery = input("Do you want it to be delivered\n Y/N:- ")
if(isDelivery == "Y" or isDelivery == 'y'):
    totalAmount = totalAmount + 10;
print(f"Total Cost amounts to {totalAmount}");
'''
## here we are cheching multiple conditions using logical operators
## they are based on something called truth tables but the just is
## and => both conditions need to be true
## or => one of the condition needs to be true 
## not => the negation of the condition needs to be true 

## Final project for DAY3 =>
## treasure Game 
'''
import time as t
print("Welcome to Treasure Island\nYour mission is to find the treasure!")
direction = input("Left(L)/Right(R):- ")
if(direction=="R" or direction == "r"):
    print("You have fallen in a hole.\nGame over")
elif(direction=="L" or direction=="l"):
    direction = input("But there is a lake.Swim(S)/Wait(W)")
    if(direction == "S" or direction == "s"):
        print("You have been attacked by a crocodile\nGame Over")
    elif(direction == "W" or direction == "w"):
        print("Your boat has arrived")
        direction = input("Please press enter to enter the boat")
        print("You have entered the boat, lets go")
        t.sleep(5)
        print("Your have reached the shore\n")
        direction = input("Left(L)/Right(R):- ")
        if(direction == "L" or direction == "l"):
            print("You have reached a forest and need to fight a tiger?")
            action = input("What will you do?\n Run(R)/Fight(F)")
            if(action == "F" or action == "f"):
                print("You have no wepons hence lost to the tiger\n Game Over")
            elif(action == "R" or action == "r"):
                print("Wrong choice! the tiger has followed you and killed you\n Game Over")
        elif(direction =="R" or direction == "r"):
            print("You have reached a cabin\n what will you do ??")
            action = input("Press Enter to open the cabin and get inside!")
            print("Entering the cabin")
            t.sleep(3)
            print("Entered the cabin\n You see a green, red, blue door. What should I select?")
            door = input("Red(R),Blue(B),Green(G):- ")
            if(door == "R" or door == "r"):
                print("The door leads to an inferno in which you have burned and died.\n GAME OVER")
            elif(door == "B" or door == "b"):
                print("The door leads to the treasure. Your win")
                name = input("Please enter your name")
                print(f"{name} is the proud owner of the treasure")
            elif(door == "G" or door == "g"):
                print("You have unleashed a deadly virus which has killed you instantly\n GAME OVER")
                '''
##########################################################################################################################
### Day 4:- Randomization and Python List
## Randomization :- to create a degree of unpredictablilty. 
## This is created via Random module in python 
## Computers are generally deterministic in nature meaning they work in a predictable manner
## Python uses something called "Mersenne Twister" for generating random numbers
## by running this code we can get the documentation
'''
import webbrowser as webb
url_random = "https://docs.python.org/3/library/random.html"
resources = "https://www.udemy.com/share/103J8C3@5X4F98BK-9gGlp3buD_tyLnpMinHJvQmUdsLddBftMp9ESSx2lcl2JJoqULUzSZl/"
print(f"{url_random}")
webb.open(url_random)
webb.open(resources)
'''
'''
import random as rand
random_number = rand.randint(1,9999999)## generates a number between 1 and 9999999 both inclusive
random_float = rand.random()## generates a number between 0 and 1
print(f"A random number {random_number} and {random_float}")
## Module => basically a function or a resuable piece of code.
'''
## Lists => is data structure  which is a collection of data
## Example :- fruits
''' 
fruits = ["Cherry","Apple","Pear","MuskMelon","WaterMelon","Mango","Blueberry"]
print(fruits[0:3])## prints 3 fruits form the list
print(fruits[2])## prints pear(index 2)
print(fruits[2][0])## Something like a 2D array in C but in this case we can have values with
## different data types
random_values = ["Mukund",3.14,24]
print(random_values[0:-1])
## This is how you basically use looping to travrse the loop
for i in random_values:
    print(i)
## Indexing starts from 0 because lists comes from a concept called arrays which are basically
## a list of contiguous memory locations =>  and the array starts from 0
## items in a list can be changed
random_values[0] = "Robert"
fruits[2]="Jackfruit"
print(random_values[0:-1])
print(fruits[0:-1])
import webbrowser as webb
webb.open("")
webb.open("https://docs.python.org/3/tutorial/datastructures.html")
## this is to get all the methods which can be used on a list
'''
## Example 
## Who is going to pay the bill
'''
import random as rand
import time as t
names = list()
number = int(input("Enter the number of people present in gathering:- "))
for i in range(number):
    temp = input("Please enter name:- ")
    names.append(temp)
print("The following names have been entered")
for i in names:
    print(f"{i}")
print("Please wait we are selecting a member\n")
t.sleep(1)
print(f"{names[rand.randint(0,number)]} please pay the bill")
'''
## Common issue / error :- Index out of range error. 
## say there are 10 elements in the list and you ask for the 11th element that is when you get this error
## this is what we call "INDEXX OUT OF RANGE" in C its something like segmentation fault
'''fruits  = ["Apples","Oranges","Mangoes","BlueBerries","Strawberries"]
vegetables=["Bringal","Potatoes","Spinach","Corriander","Cabbage","Cauliflower"]
animalProducts = ["Chicken", "Eggs", "Milk","Cheese"]
foodSuppliments = [fruits,vegetables,animalProducts]
print(foodSuppliments)## this contains 3 lists something like a 2 dimensional array but not exactly that '''
## Example :- Creating a Rock Paper Sissor game
## import random as rand
rock = '''    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''
paper = '''     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)'''
scissors = '''     _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''
'''
options = [rock,paper,scissors]
userInput = input("Rock(R)/Paper(P)/Scissors(S):- ")
computerInput = rand.randint(0,len(options)-1)
print(f"Computer chose {options[computerInput]}")
## Rock case
if((userInput == "R" or userInput == "r") and computerInput == 0):
    print("Its a draw")
elif((userInput == "R" or userInput == "r") and computerInput == 1):
    print("You Lose")
elif((userInput == "R" or userInput == "r") and computerInput == 2):
    print("You Win")
## Paper case
elif((userInput == "P" or userInput == "p") and computerInput == 1):
    print("Its a draw")
elif((userInput == "P" or userInput == "p") and computerInput == 2):
    print("You Lose")
elif((userInput == "P" or userInput == "p") and computerInput == 0):
    print("you win")
#Scissor case 
elif((userInput == "S" or userInput == "s") and computerInput == 2):
    print("Its a draw")
elif((userInput == "S" or userInput == "s") and computerInput == 0):
    print("You Lose")
elif((userInput == "S" or userInput == "s") and computerInput == 1):
    print("you win")'''
#######################################################################################################################
## Day 4 :- Looping.
## In coding in general we have 3 types/flavours of loops 
## 1) For loop => where the number of iterations is known
## 2) While loop => where the terminating contition is known but not sure about the number of iterations
## 3) Do While Loop => like while loop but work is first done before the terminating condition is checked
## Python has methods called sum() => which allow us to put in any iterable datatype and gives you the sum 
## of all the elements in the list all of which we can replicate using looping 
## Here we will have an exercise where we find the following
## 1) Maximum Value
## 2) Minimum Value
## 3) Sum of all elements
## 4) Average of all elements
## 5) Mean 
## 6) Median
## Input must be user defined with the number of elements and the elements present
## Note this has to be done without using the math functions and needs to be done using looping and conditionals and list
'''
elementCount = int(input("Enter the number of students present in a class: "))
marks = []
for i in range(elementCount):
    temp = float(input(f"Enter roll number{i+1} marks out or 100: "))
    marks.append(temp)
print(f"These are the marks that you have entered\n{marks}")
marks.sort()
## finding the maximim value
maxMarks = 0## students marks are out of 100
for i in marks:
    if(i>maxMarks):
        maxMarks = i
    else:
        continue
print(f"The Max marks is {maxMarks}")
## finding the least value
leastMarks = 100;
for i in marks :
    if(i<leastMarks):
        leastMarks = i
    else:
        continue
print(f"Least mark is {leastMarks}")
## calculating the average
sum = 0
for i in marks :
    sum = sum + i
print(f"Sum of all marks is {sum} and the average is {sum/elementCount}")
medianMarks =((marks[elementCount//2]+ marks[elementCount//2]-1)/2) if(elementCount%2 == 0)  else marks[elementCount//2]
print(f"Median mark is {medianMarks}")
## here "range()" used in conjecture with for is basically incrementing the local variable which we use to iterate through the list
## in c we write for(int i=0;i<max_number;i++) here this i++ is being done by the range function.
'''
### Next challange =>
## a number divisible by 3 must day "FIZZ" and the number divisible by 5 must say "BUZZ"
## Maximum number must be given by the user as userInput
'''
maximumValue = int(input("Please enter your maximum number: "))
for num in range(1,maximumValue+1):
    if(num%3 == 0 and not(num%5 == 0)):
        print("Fizz")
    elif(num%5 == 0 and not(num%3 == 0)):
        print("Buzz")
    elif(num%3 == 0 and num%5 == 0):
        print("FizzBuzz")
    else:
        print(num)
'''
## Next Chalange => Creating a Password generator 
'''
import random as rand
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','@','%','$','*']
alphabets = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]
print("Welcome to a random Password Generator")
number_count = int(input("Please enter number count needed in password: "))
symbol_count = int(input("Please enter symbols count needed in password: "))
alphabet_count = int(input("Please enter alphabet count needed in password: "))
## this is where we are taking the easy approach 
password = "";
## for number
for num in range(0,number_count):
    password += rand.choice(numbers)
## for letters
for char in range(0,alphabet_count):
    password += rand.choice(alphabets)
## for symbols
for symbol in range(0,symbol_count):
    password += rand.choice(symbols)
print(f"Your new password is :- {password}")  
'''
'''
## This is for the hard method
password = [];
## for number
for num in range(0,number_count):
    password += rand.choice(numbers)
## for letters
for char in range(0,alphabet_count):
    password += rand.choice(alphabets)
## for symbols
for symbol in range(0,symbol_count):
    password += rand.choice(symbols)
rand.shuffle(password)
newPassword = "".join(password) 
print(f"Your new password is :- {newPassword}")  
'''
######################################################################################
## Day6 :- Functions , while loop and an interesting project
'''import webbrowser as webb
webb.open("https://docs.python.org/3/library/functions.html")
'''
## This is the place where we can get the python documentation
## Example :- Something which finds he area and perimeter of a given shape.
## The dimensions must be user given.
## for area
'''
def area (shape):
    area = 0
    if(shape.upper() == "C"):
        radius = int(input("Please enter radius: "))
        area = 3.14 * radius * radius
    elif(shape.upper() == "R"):
        lenght = int(input("please enter lenght: "))
        breadth = int(input("please enter breadth: "))
        area = lenght*breadth
    elif(shape.upper() == "T"):
        base = int(input("Please enter base: "))
        height = int(input("Please enter height"))
        area = (base*height)/2
    elif(shape.upper() == "S"):
        side = int(input("please enter side"))
        area =side*side
    return area
## for type of triangle
def triangleNature(dimensions):
    if(len(set(dimensions)) == 1):
        print("Equilateral Triangle")
    elif(len(set(dimensions))<3):
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
## for the perimeter of dimensions 
def perimeter(shape,dimensions):
    if(shape.upper() == "C" and len(dimension)!=2):
        perimeter = 2* 3.14* dimensions[0]
        print(f"Circle Perimeter and area :{perimeter} and {area(shape)}")
    elif(shape.upper() == "S" and len(dimensions)!=2):
        perimeter = 4*dimensions[0]
        print(f"Square perimeter and area = {perimeter} and {area(shape)}")
    elif(shape.upper() == "R" and len(dimensions)==2):
        print(dimensions)
        perimeter = 2*(sum(dimensions))
        print(f"Perimeter and area of the rectangle = {perimeter} and {area(shape)}")
    elif(shape.upper() == "T" and len(dimensions)==3):
        print(dimensions)
        perimeter = sum(dimensions)
        ## here we are trying to check if the nature of triangle via dimensions 
        triangleNature(dimensions)
        print(f"Perimeter and area of the Triangle = {perimeter} and {area}")
## this is for area where I will be taking the dimensions in the function and will be returning it back to main function
dimension = []
## this is for square/circle
shape = input("Please enter shape\n Circle(C)/Square(S)/Rectangle(R)/Triangle(T): ")
if(shape.upper() == "C" or shape.upper() =="S" ):
    temp = int(input("Please enter radius/side: "))
    dimension.append(temp);
## this is for rectangle
elif(shape.upper() == "R"):
    for i in range(0,2):
        temp = int(input("Please enter lenght/breadth: "))
        dimension.append(temp);
elif(shape.upper() == "T"):
    for i in range(0,3):
        temp = int(input("Please enter lenght/breadth: "))
        dimension.append(temp);
perimeter(shape,dimension)
'''
## Guide for Python Code
''' 
import webbrowser as webb
webb.open("https://peps.python.org/pep-0008/")'''
##########################################################################################################################
## Day 7 :- HANGMAN
## With the skills we have learnt we will looking into how we can create this hangman game 
## That will be present in another file called Hangman.py so please look into it for further clarity
#################################################################################################################
## Day 8:- 
'''
import webbrowser as webb
webb.open("https://waitbutwhy.com/2014/05/life-weeks.html");
## This is what I need to replicate 
def life_in_weeks(Age):
    return Age*52

def life_in_days(Age):
    return Age*365

def life_in_hours(Age):
    return life_in_days(Age)*24

def life_in_min(Age):
    return life_in_hours(Age)*60

def life_in_seconds(Age):
    return life_in_min(Age)*60

Age = int(input("Please enter your age: "))
if(Age>0 and Age<90):
    print(f"You have lived for {life_in_weeks(Age)} weeks;{life_in_days(Age)} days;{life_in_min(Age)} minutes;{life_in_seconds(Age)} seconds.")

else:
    print("Entered Invalid Age!!")

'''
## Difference between Positional Argurment VS Keyword Arguement
## keyword arguements
'''import time as t
def greetings(name,location):
    print(f"Hey{name} and welcome to {location}")

name = input("Enter the name: ")
location = input("Enter the location: ")
## this is what you call keyword arguements ##
greetings(name=name,location=location)
t.sleep(2)
greetings(location= location,name=name)
t.sleep(2)
## This is what you call positional arguements
greetings(location,name)
t.sleep(2)
greetings(name,location)
'''
## Keyword arguement are more rebust as compared to positional arguements
## Example :- Love Calender 
#TO DO:- 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   
# TO DO:- 2. Then check for the number of times the letters in the word LOVE occurs.   
# TO DO :- 3. Then combine these numbers to make a 2 digit number and print it out. 
'''def calculate_love_score(name1,name2):
    ## must check the number of time letters in true occur
    word = ['t','r','u','e']
    True_totalCount = 0
    for char in word:
        count = 0
        count = name1.count(char)+name2.count(char)
        True_totalCount = count+True_totalCount
        #print(f"{char} occurs {count} times")
    word = ['l','o','v','e']
    Love_totalCount = 0
    for char in word:
        count = 0
        count = name1.count(char)+name2.count(char)
        Love_totalCount = count + Love_totalCount
        #print(f"{char} has been repeated{count} times")
    print(f"{True_totalCount}{Love_totalCount}")
 

name1 =input("Enter first name: ")
name2 = input("Enter Second name: ")
calculate_love_score(name1=name1,name2=name2)
'''
### Hangman Project ##
'''import random as rand
import webbrowser as webb
## the following are the rules of hangman 
##webb.open("https://en.wikipedia.org/wiki/Hangman_(game)")
## the above is the wikkipedia link to thenhangman game
# TODO 1 :-  Listing all the various words that make sense and putting it in a list 
# TODO 2:- Generating a random number 
# TODO 3:- Asking them to get a letter

animalList = ["camel","dog","cat","squirrel","tiger","wolf","lion","deer","mouse","pig","parrot"]
animal = rand.choice(animalList)
placeholders = ""
for position in range(0,len(animal)):
    placeholders += "_"
print(placeholders)
chances = len(animal)
status = False
print(f"you have {chances} lives")
correntLetters = []
while(chances>0):
    userGuess = input("Guess a letter: ").lower()
    display = ""
    ## here we need to check if the given letter is present /not 
    for char in animal:
        if(char == userGuess):
            display+=char
            correntLetters.append(userGuess)
        elif(char in correntLetters):
            display+= char
        else:
            display += "_"
    print(display)
    if(userGuess not in animal):
        chances = chances -1

    if(display.lower() == animal.lower()):
        status = True
        break
if(status == True):
    print("You Win") 
    print(f"{animal}")   
else:
    print(f"You lose. The word is {animal}")   
'''

#### Project Ceaser Cipher ###
## import webbrowser as webb
## webb.open_new("https://www.w3schools.com/python/ref_list_index.asp")
## this is going to the place you see what is needed 
## The solution will be broken into 3 parts 
## 1) The encription
## 2) The decription 
## once we have a working model/code => Restructure and code clean-up
'''alphabets = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]
def encript(original_message,shift):
    encripted_message = ""
    for char in original_message:
        shifted_position = alphabets.index(char)+shift
        shifted_position %= len(alphabets)## This is to prevent index out of range
        encripted_message+=alphabets[shifted_position]
    return encripted_message

def decript(original_message,shift):
    encripted_message = ""
    for char in original_message:
        shifted_position = alphabets.index(char)-shift
        shifted_position %= len(alphabets)
        encripted_message=encripted_message+alphabets[shifted_position]
    return encripted_message

status = True
while status==True:
    operation=input("Please enter E for encript or D for Decript: ").lower()
    if(operation!='e' and operation!='d'):
        break
    message = input("Please enter your message: ").lower()
    shift = int(input("How far do you want to shift it : "))
    if(operation == 'e'):
        print(f"Your Encripted message = {encript(original_message=message,shift=shift)}")
    elif(operation == 'd'):
        print(f"Your Decripted message = {decript(original_message=message,shift=shift)}")
    else:
        break
print("Exiting Program")
'''
## This marks the end of day 8 ######
#####################################
### Day 9 Dictionary and Nesting#####
## Dictionaries in Python => key value pairs 
## example :- 
'''programming_dictionaries = {404:"URL/Entry not found",500:"Internal Server error",200:"OK Response",401:"Authentication error"}
print(programming_dictionaries[404])
'''
## In the case above 404 => key and URL/Entry not found => value 
## "Key Error"=> exists when you are trying to searching for a key wihch doesnot exists 
# programming_dictionaries.clear() ## this clears the complete dictionary.
## looping through a dictionary 
'''
for keys in programming_dictionaries:
    print(f"{keys}:{programming_dictionaries[keys]}")

'''
## looping through a dictionary and getting the keys and values

## Example:-
'''
def grade(score):
    if(score >=91 and score<=100):
        return "OutStanding"
    elif(score>=81 and score<=90):
        return "Exceeds Expectations"
    elif(score>=71 and score<=80):
        return "Acceptable"
    else:
        return "Fail"
    
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
student_grade = {}
for student in student_scores:
    allocated_grade = grade(student_scores[student])
    student_grade[student] = allocated_grade
print(student_grade)
'''
## Nested Lists => basically a list inside a list.
## in dictionaries can be either premative data types or can be a list,dictionary,etc
'''
employee_dict = {1:["Mukund Khamampati",24,"Software","Jr Engineer"],2:["Raghava Khamampati",21,"Hardware","ASIC Designer"]}
print(employee_dict)
print(employee_dict[2])
print(employee_dict[1][2])# we are taking a key and the second value in the value which is a list 
places = {"Hyderabad":["TankBund","Financial District","Abids","Doctors Colony","Secunderabad","Gachibowli"],"Nagpur":["Ambazari","Seeta Buldi","Ram Nagar","Bajaj Nagar Chauk","Maate Chauk","Yeshwanth Nagar"]}
'''
## the above is another example:- City and the major places there.
## Instead of a list you can place a dictionary 
#Eg:-
'''
vehicles = {
    "Bike":{"Hero":"Impulse","Royal Emfield":"ThunderBird 350","Triumph":"Bonnevile","TVS":"Apache 310"},
    "Car":{"Maruthi":"Scross","Hyundai":"SantaFe","Honda":"Civic","Skoda":"Octavia","Tata":"Safari"}
}
print(vehicles["Bike"]["Hero"])## Works as Dictionary[Key][Key]
'''
## Silent Acution ## 
'''
import webbrowser
webbrowser.open("https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Blind%20Auction%20Flow%20Chart#R3VnbcpswEP0aPzYDCLB5tHNrZ9pMpu6kzaMMilEDiBHyLV%2FfFYirHMdp7JD4JUGrXV3Ont2V5AE6j9fXHKfhDxaQaGAZwXqALgaWZRqmAf%2BkZFNIHM8qBHNOA6VUC6b0iZSWSrqgAclaioKxSNC0LfRZkhBftGSYc7Zqqz2wqD1riudEE0x9HOnS3zQQoZK6jl13fCV0HpZTm65X9MS41FZbyUIcsFVDhC4H6JwzJoqveH1OIoleCUxhd%2FVMb7UyThKxj8Hs4R5fx%2BMlu%2F52dxPepdM7H31BxShLHC3UjtVixaaEgASAiGoyLkI2ZwmOLmvphLNFEhA5jQGtWuc7YykITRD%2BJUJslHvxQjAQhSKOVG8xp5zo2b0pUcYW3Cc7NlSSBPM5ETv0rMoDwF3CYiL4Buw4ibCgy%2FY6sCLRvNKrYYYPhfQrUDc11Ke%2Fxj9%2FadDXwEqUViEVZJrifP8riLdtIC4JF2S9G0Z928rAHimuqmi1VXNVU99TorBBemQcCSfn1Nhp7clOu092Wjo7Q0hclhEBcDKJchbn6VWcpZsPx1mvZ84OT42z9p6cdfvkrK2hPs4e84LP4e8NjokcIUkXon%2FCOk6LsKajM9a0t1DWPhZlvVOjrLsnZUd9UtbdSdkJ2FrGLaew0Y%2FG2OpI2xtjTf0E9ckp%2B1YqKtNbRmHmynOO1fYcGnU8UoSIsuo4pVrG%2F%2FtppHM8COqEjJOgojqsQB4usLwsUl9QcESOAKwUIjmU6o9kUxnlQ54NLBfHkvDJLEsrh%2FQZKmh41gmWLQcSc%2BjoweIcLVhGfcQGWVPxR5nL7%2FuG%2FGLd6LjYlI0EdpubAISqed%2Fsq83yVml3wCg00Z6VwxweIl7HnONNQyGVcZg9H872yGxxy%2B5e%2BTv6yHN26cNHsYKDxnwFdi90Mxt0Uzw6CcI1noz6eLDQ34mKwwp9KLIzz9N5%2FpfJ5kCu141gR5MZNNy5%2FFpkhMtsvgplpl%2FhnKp51p%2FJEtBN3SGLZ4usp7RdVcqX0na3oh4Oc%2F2AeE8yDSbYtGjjgSM6T%2BDbh82DJ9BEQkN9HI1VR0yDoIg6ktEnPMuHksRW%2BQfGdSYD50KOBYGWFTF3IKiRZ7dzkmFrQG87S1pHw9nrtTxWOeo1BbKVrerk9Q75arhnvnrrC9b2gmZ1HnvQcL%2Fz7GsLbbdwOvbuQttd12v1zeE7FGZTf5o6jwjm1fk68zkhiZ6I3%2FkMjZzOK%2FSWVLztSe9ot80y9TSAu6L5LaTALYQ1kEyUdQyuMlVX%2ByqT2wTEj4pKCSpx%2B4azokkii2fPHnCGL3vA9LYUQ%2FdoLrA0F9ywT18LXdTB2dBxRoephdCsf2osMkr9iy26%2FAc%3D#%7B%22pageId%22%3A%22_ZI8kH0kThzWXmJmaaEm%22%7D")
## This is how the diagram looks like.
import subprocess as sbp
import os
import time as t

## This is for clearing the terminal.
def clear_terminal():
    if os.name == 'nt': ## Meaning this is windows
        sbp.run(['cmd','/c','cls'])
    else:## Linux or any associated distro
        sbp.run(['clear'])

print("Welcome to the SILENT AUCTION")
item = input("Please enter the item to be auctioned off: ")
minimum_cost = int(input("Enter the minimum cost from which the bidding has to be started: "))
participant_list = {} ## dictionary
disqualified_list = []
status = True
lifes = 5
while status == True:
    op = input("Do you want to proceed? ")
    if op.upper() == "N":
        status = False
        continue
    name = input("Enter the participants name: ")
    cost = int(input(f"Please enter your bid, must be greater than {minimum_cost}: "))
    if cost > minimum_cost and name not in disqualified_list:
        participant_list[name] = cost
        minimum_cost = cost
        clear_terminal()

    else :
        if lifes ==0 and name in disqualified_list:
            print(f"{name} has been disqualified!")
            print(f"Will resume in 20 seconds after {name} has been ascorded out")
            t.sleep(20)
        lifes = lifes -1
        print(f"The bid amount{cost} is less than {minimum_cost}, Invalid bid,{name} has {lifes} left.")
        
## when the bidding is COMPLETE 
last_bid = next(reversed(participant_list))
if not participant_list:
    print(f"{item} has been removed from the auction")
print(f"{last_bid} wins the {item} for {participant_list[last_bid]}")
'''
################################################################################################################
## Day 9 => Functions with outputs
'''
def is_leap_year(year):
    if year%400 == 0 :
        return True
    elif year%100 == 0:
        return False
    elif year%4 == 0:
        return True
    else:
        return False
    
year = int(input("Please enter an year: "))
IsLeapYear = is_leap_year(year=year)
if IsLeapYear == True :
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
'''
## Calculator Project ##
'''def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2

print("Welcome to Calculator")
num1 = int(input("Enter first number: "))
status = True
while status !=False:
    operation = input("Enter Operation : +,-,*,/ : ")
    num2 = int(input("Enter second number: "))
    result = 0
    if(operation == "+"):
        result = add(num1=num1,num2=num2)
    elif(operation == "-"):
        result = sub(num1=num1,num2=num2)
    elif(operation == "*"):
        result = mul(num1=num1,num2=num2)
    elif(operation == "/"):
        result = div(num1=num1,num2=num2)
    print(f"Result = {result}")
    option = input("Do you want to proceed = N/Y: ")
    if(option.upper() == "N"):
        status = False
    elif(option.upper() == "Y"):
        num1 = result
print(f"Your total result = {result}")
'''
##############################################################################
## Day 11 :- Blackjack Capstone Project ##
## The Sum of all cards must be less then 21, if the sum exceeds 21 its called a bust
## all cards from 2 to 10 are the same as their face value
## J,K,Q => will be counted as 10
## Ace => 1/11 based which is specified by the user
## The Dealer's second hand is concelled => basically hidden 
## if our score == dealer score (DRAW)
## if my score > dealer score <21 (WIN)
## My score >21 ( BUST => you loose)
## if my score < dealer <21 then you loose 
## if sum total of dealer is <17 they can take a new card
'''import random as rand
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
def deal_card():
    return rand.choice(cards)

def calculate_score(cards):
    score = 0
    score = sum(cards)
    if score ==21 and len(cards) == 2:
        return 0
    if 11 in cards and  score >21:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score

def compare(user_score,comp_score):
    if(user_score == comp_score):
        return "Draw"
    elif(comp_score==0 or user_score>21):
        return "Computer Wins"
    elif(user_score==0 or comp_score>21):
        return "You Win"
    elif(user_score > comp_score):
        return "You Win"
    else:
        return "You lose"
    
player_status = False
player_card = []
comp_card = []
player_score = -1
computer_score = -1
for _ in range(2):
    player_card.append(deal_card())
    comp_card.append(deal_card())
## This is for the player
while player_status == False:
    player_score = calculate_score(player_card)
    computer_score = calculate_score(comp_card)
    print(f"Users Cards:- {player_card}")
    print(f"Computers Cards :- {comp_card[0]}")
    if player_score == 0 or computer_score == 0 or player_score>21:
        player_status = True
    else:
        should_redraw = input("Do you want to draw again: Y/N: ")
        if should_redraw.upper() == 'Y':
            player_card.append(deal_card())
        else:
            player_status = True
while computer_score !=0 and computer_score<17:
    comp_card.append(deal_card())
    computer_score = calculate_score(comp_card)
print(f"User Cards = {player_card}")
print(f"Computer Card = {comp_card}")
player_score = calculate_score(player_card)
computer_score = calculate_score(comp_card)
print(compare(user_score=player_score,comp_score=computer_score))'''
#######################################################################################
## Day 12 Number Guessing Game ##
## There will be 2 modes => easy and hard mode 
## easy mode will have 10 lives 
'''import random as rand
chance = 10
random_guess = rand.randint(0,100)
print("Welcome to the guessing game!")
choice = input("Enter the difficulty of the game. H/E: ")
if choice.Upper == "H" :
    chance = 5
else :
    chance = 10
while chance!= 0:
    userguess = int(input("Enter your guess: "))
    if userguess > random_guess:
        print("Too High")
        chance = chance-1
        print(f"Chances:{chance}")
    elif userguess < random_guess:
        print("Too Low")
        chance = chance-1
        print(f"Chances:{chance}")
    elif userguess == random_guess:
        print(f"You got it the answer is {random_guess}")
        break;
if chance == 0:
    print(f"The actual number is {random_guess}. Your missed it. run again ")'''
### BTW python does not have any block scope 
## Example :- Prime number checker
'''def prime_checker (number):
    factor_list = []
    if number == 1:
        return f"Given number {number} is neither prime nor composite"
    for i in range(1,number+1):
        if number%i == 0:
            factor_list.append(i)
            continue
    if(len(factor_list)==2):
        return "Prime Number"
    else:
        return "Composite Number"
number = int(input("Enter a number: "))
print(prime_checker(number=number))'''
############################################################################################################################################################