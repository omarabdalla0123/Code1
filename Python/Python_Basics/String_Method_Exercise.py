
user_first_input = ""


def upper():
    print(f"Upper : {user_first_input.upper()}")


def Lower():
    print(f"Lower : {user_first_input.lower()}")



def split():
    user_first_input.strip()
    print(f"word count : {len(user_first_input.split())}")


def len1():
    print(f"ch count : {len(user_first_input)}")

def replace():

    old_word = input("what is the word that you want to change : ")
    if old_word in user_first_input :
        new_word = input("what is the word you want to put : ")

        new_sentence = user_first_input.replace(old_word,new_word) 
        print(f"this is the sentence : {new_sentence}")
    else: 
        print("the word is not exist")    




while True :

    user_first_input = input("Enter a sentence : ")
    sen = user_first_input
    res = upper()
    res = Lower()
    res = split()
    res = len1()
    sentence_check = input("Enter a Word to search : ")
    
    if  sentence_check in user_first_input :
        print(f"{sentence_check} exist on the sentence ")
    else:
        print(f"{sentence_check}is not exist on the sentence ")    
    
    replace_check = input("if you want to replace any word click on (r) : ")
    if replace_check == "r" :
        res =  replace()
        
    else:
        print("that mean you don't want to change ")
        print(f"this is your sentense : {user_first_input}")

    break
