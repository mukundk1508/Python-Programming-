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
question_data = [
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
import webbrowser
webbrowser.open("https://opentdb.com/api_config.php")