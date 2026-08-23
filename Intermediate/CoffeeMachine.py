
############################################################################################################
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
    print("All right kool. Restart to run the coffee machine again ")