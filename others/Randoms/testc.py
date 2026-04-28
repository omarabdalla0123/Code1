


class Contact : 
    
    def __init__(self, name, phone) :

        self.name = name
        self.phone = phone 


    def info(self):

        return (f" Name : {self.name}, Phone : {self.phone}.")
    

    def add(self) :
        self.name = input("Enter the Contact Name : ")
        self.phone = input("Enter the Contact Phone : ")
        return (f"Name : {self.name}, Contact Phone : {self.phone}")



contacts = {}

user = ""


contacts[user] = Contact("","")

while True :
    
    user = input("Enter : \n (a) to add \n (i) to info \n What You Choosed : ")

    if user == "a" :
        res = Contact.add()


    elif user == "i" :
        res = contacts.info()

    else: 

        exit()






