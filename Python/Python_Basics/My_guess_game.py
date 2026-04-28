import random

user_choice = ''
#int(input("Enter Your Choice : "))
computer_choice = random.randint(1, 3)

result = f'the user choice is : {user_choice}, and the computer choice is : {computer_choice}.'

while computer_choice != user_choice : 
        user_choice = int(input("Enter Your Choice : "))



if user_choice == computer_choice :
        print(result)
        print('you won')
        exit()


#        print('it is not correct \n try agian')