## Day 17 Start :- 
## creating a class
"""class Dog:
    ## This class must have the following 
    ## 1) Members/Attributes
    ## 2) Methods pertainating the User
    ## 3) a constructor class\
    def __init__(self,name,age,breed):
        self.name = name
        self.age = age
        self.breed = breed

    def introduction(self):
        print(f"{self.name} is a {self.breed} and is {self.age} years old")

    def eat(self):
        print(f"{self.name} is having food.")
    def sleep(self):
        print(f"{self.name} is currently sleeping!")

bruno = Dog("Bruno",2,"St Bernard")
bruno.introduction()
bruno.eat()
bruno.sleep()"""
## 18th August 2026 :- 
## name of a class in python must have all the names capatilized  which we call as pascal case 
## Snake casing will be used for everything almost everything but for class names we will be using camel casing
## Contructor => used to initialize the object.
#######################################################################################################################
##
## This is a class defination called Question 
"""question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]
class Question :
    def __init__(self,q_text,q_answer):
        self.q_text = q_text
        self.q_answer = q_answer


    
class QuizBrain:
    def __init__(self,q_list):
        self.q_number = 0
        self.score = 0
        self.q_list = q_list
        
    def stillHasQuestions(self):
        return  self.q_number<len(self.q_list)

    
    def nextQuestion(self):
        current_question = self.q_list[self.q_number]
        self.q_number +=1
        user_answer = input(f"{self.q_number}:{current_question.q_text}(True/False):")
        self.checkAnswer(user_answer,current_question.q_answer)
        #print(f"Your current score is {self.score}/{self.q_number}")

    def checkAnswer(self, user_answer,correct_answer):
        if(user_answer.lower()==correct_answer.lower()):
            print("Correct")
            self.score +=1
        else:
            print(f"Wrong Answer! Correct Answer = {correct_answer}")


question_bank = []
for question in question_data :
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)
quiz = QuizBrain(question_bank)
while quiz.stillHasQuestions(): 
    quiz.nextQuestion()
print("You have completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.q_number}")
## This is to change the questions or to get more questions 
import webbrowser
webbrowser.open("https://opentdb.com/api_config.php")"""
###########################################################################################
## Expresso Machine using lists and dictionaries
'''############################################################################################################
## TODO 1:- Print all the resourcess needed for coffee.                                                   ##
## TODO 2:- Printing the menue.                                                                           ##
## TODO 3:- Logic for the coins and their value.                                                          ##
## TODO 4:- Logic for depleting resources when something is ordered.                                      ##
## TODO 5:- Regarding the amount deducted every drink has some money assiciated with it.                  ##
## TODO 6:- ONce the drink is created we need to look into how to relete resources                        ##
## TODO 7:- This must be put in a loop till the resources are depleated                                   ##
############################################################################################################
import webbrowser as webb
from PIL import Image 

## Menu in the form of a dictionary
Menu = {
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":18,
        },
        "cost":1.5
    },
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24,
        },
        "cost":2.5
    },
    "cappuccino":{
        "ingredients":{
            "water":250,
            "milk":100,
            "coffee":24,
        },
        "cost":3.0
    }
}

## Resources in the form of a dictionary
resources = {
    "water":3000,
    "milk":2000,
    "coffee":1000,
}
## These are the variables needed for the program
profits = 0
status = True
## This is for the program requirement if anyone is interested 
## This is where you open some images 
def program_requirements():
    ## This is for the program requirements
    program_req_img = Image.open("/home/mk1508/Documents/Python_Learning/Intermediate/Images/Program Requirements.png")
    program_req_img.show()
    ##  This is for the coffee and their associated attributes 
    coffee_Members_img = Image.open("/home/mk1508/Documents/Python_Learning/Intermediate/Images/Coffee and their members.png")
    coffee_Members_img.show()
    ## Coins and their value 
    coin_and_value_img = Image.open("/home/mk1508/Documents/Python_Learning/Intermediate/Images/Coins and Their Values.png")
    coin_and_value_img.show()
    ## This indicated the initial Resources 
    initial_resources_img = Image.open("/home/mk1508/Documents/Python_Learning/Intermediate/Images/Initial Resources.png")
    initial_resources_img.show()
    ## These images speak about the program and what is needed 
    ## Instructions will be here
    webb.open_new("/home/mk1508/Documents/Python_Learning/Intermediate/PDF's/Coffee+Machine+Program+Requirements.pdf")
    ## Have decieded to open this in web 

## This is to check if the present resources are sufficient/not 
## If not sufficient will return false else will return true
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>=resources[item]:
            print(f"Insufficient Resources! {item} must be refilled")
            return False
    return True    

## Processing the total amount based on the number of coins inserted
## Returns total amount
def process_coins():
    print("Insert Coins: ")
    nickel_count = int(input("Enter number of nickels"))
    dime_count = int(input("Enter number of dimes"))
    penny_count = int(input("Enter number of pennies"))
    quater_count = int(input("Enter number of quaters"))
    total_amount = nickel_count*0.05 + dime_count*0.1 + penny_count*0.01 + quater_count*0.25
    return total_amount

## This is checking if the money recieved and the drink cost match
## -1 when drink_cost > money_recieved
## 0 when drink_cost == money_recieved
## change when drink_cost < money_recieved
def is_transaction_successful(money_recieved,drink_cost):
    global profits
    if money_recieved == drink_cost:
        #global profits
        profits += drink_cost
        print("Thankyou")
        return 0
    elif money_recieved>drink_cost:
        print(f"{money_recieved - drink_cost} is the change")
        #global profits
        profits += drink_cost
        return money_recieved - drink_cost
    elif money_recieved<drink_cost:
        print(f"Insuffient funds ! refunded {money_recieved}.")
        return -1

## Here you have to evaluate of the transcation has gone through
## If so deduct the resources
def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"There is your {drink_name}")

while status == True:
    option = input("What do you want? espresso/latte/cappuccino/Off(O)/report(R): ").lower()
    if option.lower() == "o" :
        print("Turining off the system")
        status = False
        continue
    elif option.lower() == "r":
        print(f"Water : {resources['water']}\nMilk : {resources['milk']}\nCoffee : {resources['coffee']}\nProfits : {profits}")
        continue
    else:
        drink = Menu[option]
        if is_resource_sufficient(drink["ingredients"]):
            ## Here we need to process coins
            payment = process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(option,drink["ingredients"])
## do you want to get the associated flowchart
choice = input("Do you want to know how the project works? N/Y: ").lower()
if choice == "n":
    program_requirements()
else:
    print("All right kool. Restart to run the coffee machine again ")'''
################################################################################################################################
## SO you can install python packages or search for varuious python packages 
## from the Pypi website also known as Python Package Index
import webbrowser as webb
#webb.open("https://pypi.org/")
## depending on what the package is , if present in PyPi you can go ahead and pip install 
## it in the terminal. once installed close VS code and open it again it should work
from prettytable import PrettyTable## Here we are importing the table 
table  = PrettyTable()## here we are creating an object of type PrettyTable
table.add_column("Employee_name",["Mukund","Samuel","Raghava","Lakshmi","Caleb"])
table.add_column("Occupations",["Backend Engineer","Data Engineer","RF Engineer","Lead Accountant","Youth Pastor"])
table.add_column("Age",[25,27,21,48,29])
table.align = 'r'
print(table)
table.align='l'
print(table)
## The Output is an ascii table with rows and columns