class BankAccount :
    def __init__(self, owner) :
        self.o = owner
        self.balance = 0

    def info(self):
        return(f" These Are The Information Of The Account :\n Owner Name : [{self.o}] Balance : [{self.balance}]")    
    
    def deposite(self, amount):
        self.balance = self.balance + amount
        return (f"Amount :{amount}, Balance : {self.balance}")
    
    def withdraw(self, amount):
        if self.balance != 0 :
            self.balance = self.balance - amount
            if amount > self.balance:
                return("! The Amount Is Bigger Than Your Balance !")
            else:
                self.balance = self.balance - amount
                return(f"Amount : {amount}, Balance : {self.balance}")
        else:
            return ("Your Balance is 0")


Account = BankAccount("Omer")

while True :
    print("--------------------------------------------------------------------------")
    user = input("Enter:\n (d) To Deposite \n (i) To See Account Information \n (w) To Withdraw \n (q) To Quit \n What You Entered : ").lower()

    if user == "d" :
        user = input("Put The Amount You Want To Deposite : ")
        print(Account.deposite(int(user)))
    elif user == "i" :
        print(Account.info())

    elif user == "w" :
        user = int(input("Put The Amount You Want To Withdraw : "))
        print(Account.withdraw(int(user)))
    elif user == "q":
        exit()
    else :
        print("! Please Choose One Of The Above Option !")    



