import random 


print("------Welcome to Guess Game --------")

#Functions
def randomNumber() :
    number = random.randint(1, 20)

    
def User_Guessed_Number() : # the number that the user entering
    guess = int(input("Enter your guess : "))
    return guess
    

    return number
"""
def If_Condition():
    if guess == number :
        print("it is not the correct guess")
        print("try again")
    elif guess != number :
        print("you won")
 """   
# ----Main Program----
guess = User_Guessed_Number()

number = randomNumber()

while guess != number :
    print("it is not the correct guess")
    print("try again")
    if guess == number :
        print("you won")
        break
   
