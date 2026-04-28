


contacts = {

        "omer" : "0505249254"
}

contact_name = ""
contact_phone = ""

def add(contact_name,contact_phone):
    contact_name =  input("Enter New Contact Name : ")
    contact_phone = input("Enter New Contact Phone : ")
    if contact_name not in contacts :
        contacts[contact_name] = contact_phone
    else:
        print("This Name Is Already Exist") 



def search_name(contact_name) :
    contact_name = input("Enter Contact Name :")
    if contact_name in contacts:
        print("Contact Name is exist")
        print(f"Contact's Number [{contacts[contact_name]}]")
    else:
        print("There Is No Contact By This Name")

# #my
# def search_phone(contact_phone):   
#     contact_phone = input("Enter Contact Phone :") 
#     if contact_phone in contacts.values()  :
#         print("Contact Phone is exist")  
#         print(contact_name == contact_phone)
#         print(f"Contacts Name's [{contact_name}] ")
#     else:
#         print("There Is No Contact By This Phone")
#         print(contacts.values())


def show():
    for contact_name, contact_phone in contacts.items() :
        print(f"These are Name [{contact_name}], and Numbers [{contact_phone}]")

def search_phone(contact_phone):   
    contact_phone = input("Enter Contact Phone :") 
    if contact_phone in contacts.values():
        print("Contact Phone exists")
        for name, phone in contacts.items():
            if phone == contact_phone:
                print(f"Contact's Name [{name}]")
    else:
        print("There Is No Contact By This Phone")


# def remove_phone(contact_phone):
#     contact_phone = input("Enter Contact Phone You Want To Remove : ")
#     if contact_phone in contacts.values()  :
#         del contact_phone
#         print("[Removed]")
#     else :
#         print("This Phone Is Not Exist")


def remove_name(contact_name):
    contact_name =  input("Enter Contact Name You Want To Remove : ")
    if contact_name in contacts :
        del contacts[contact_name]
    else :
        print("This Name Is Not Exist")        

def quite():
    exit() 
    
    
    
def search(contact_name,contact_phone):
    contact_name = input("Enter Contact Name :")
    contact_phone = input("Enter Contact Phone :") 
    if contact_name in contacts and contact_phone in contacts.values() :
        print("Contact Name is exist")   
    else:
        print("There Is No Contact By This Name")




while True :
    print("-------------------------------------------------------------------")
    contact_name = input(" Choose from this Options\n (a) to add \n (rn) to remove the name " + 
            "\n (s) to show the list \n (q) to quit \n (rp) to remove the phone \n (sn) to search on names \n (sp)to search on phone number "+ 
            ""
            +
            " \n Your choice : ") 
            
    if contact_name == "a" :
        res = add(contact_name,contact_phone)
    elif contact_name == "s" :
        res = show()    
    elif contact_name == "q" :
        res = quite()    
    elif contact_name == "sn" :
        res = search_name(contact_name)    
    elif contact_name == "sp" :
        res = search_phone(contact_phone) 
    elif contact_name == "rn" :
        res = remove_name(contact_name)         
    elif contact_name == "sa" :
        res = search(contact_name,contact_phone)         
    else :
        print("! Please Choose From The Opions Above !")    
# for contact_name,contact_phone in contacts :
#     if contact_name == "a" :
#         res = add(contact_name,contact_phone)


    # elif contact_name == "rp" :
    #     res = remove_phone(contact_phone) 