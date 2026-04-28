import random

computer = random.randint(1, 10)
att = 3

while True :
    guess =  int(input("Enter your guess : "))
    if guess == computer :
        print("You won")
        break
    else:
        att = att - 1
        print(f"Your attempts are [{att}]")
        print("try again !")
        if att == 0 :
            print("you lose")
            break
