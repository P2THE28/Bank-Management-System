import json
import random
import string
from pathlib import Path


class Bank:

    database="data.json"
    data = []
    try:
        if Path(database).exists():
            with open(database,'r') as fs:
                data=json.loads(fs.read()) 
        else :
            print("No such file exists")
    except Exception as err :
        print(f"an exception occured as {err}")

    
#=========================for json file updation=======================================
    @classmethod
    def __update(cls) :
        with open(Bank.database,'w') as fs :
            fs.write(json.dumps(Bank.data,indent=4))

#=========================account number generation====================================
    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters,k=3)
        num=random.choices(string.digits,k=3)
        spchar=random.choices("@#&*%!",k=1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)

#=========================for deposite of money=======================================
    @classmethod
    def depositemoney(cls):
        username=input("Enter your account number:-")
        mpin=int(input("Enter your Mpin:-"))

        userdata=[i for i in Bank.data if i['AccountNo.'] == username and i['Mpin']==mpin]
            
        if not userdata :
            print("Wrong Account no. or Mpin")
        else :    

            amount = int(input("Enter amount to deposite(0-10000):-"))
            if amount>10000 or amount < 0 :
                print("Sorry amount should be between 0 to 10000")
            else:
                userdata[0]['Balance']+=amount
                print("Succesfully money deposited")
                print(f"Balance:{userdata[0]['Balance']}")
                Bank.__update() 


#==========================Withdraw of money=========================
    @classmethod
    def withdraw(cls):
        username=input("Enter your account number:-")
        mpin=int(input("Enter your Mpin:-"))

        userdata=[i for i in Bank.data if i['AccountNo.'] == username and i['Mpin']==mpin]
            
        if not userdata :
            print("Wrong Account no. or Mpin")
        else :
                
            amount = int(input("Enter amount to withdraw(0-5000):-"))
            if amount>5000 or amount < 0 :
                print("Sorry amount should be between 0 to 10000")
            elif amount>userdata[0]['Balance'] :
                print("Sorry you dont have enough Balance")
            else:
                userdata[0]['Balance']-=amount
                print("Succesfully money deposited")
                print(f"Balance:{userdata[0]['Balance']}")
                Bank.__update() 

#===========================Details of the user=========================================
    @classmethod
    def details(cls):
        username=input("Enter your account number:-")
        mpin=int(input("Enter your Mpin:-"))

        userdata=[i for i in Bank.data if i['AccountNo.'] == username and i['Mpin']==mpin]
            
        if not  userdata :
            print("Wrong Account no. or Mpin")
        else :
            print("User details :- ")
            for i in userdata[0] :
                print(f"{i} : {userdata[0][i]}")   

#=========================update details===========================================
    @classmethod
    def update(cls):
        username=input("Enter your account number:-")
        mpin=int(input("Enter your Mpin:-"))

        userdata=[i for i in Bank.data if i['AccountNo.'] == username and i['Mpin']==mpin]
            
        if not userdata:
            print("Wrong Account no. or Mpin")
        else :
            print("Enter your new details or leave it as it is.")

            newdata={
                "Name":input("Tell new name:-") ,
                "E-mail" : input("Enter new email:-"),
                "Mpin" : int(input("Enter new 4 number pin:-")),
            }

            if newdata['Name']=="" :
                newdata['Name']=userdata[0]['Name']
            if newdata['E-mail']=="" :
                newdata['E-mail']=userdata[0]['E-mail']
            if newdata['Mpin']=="" :
                newdata['Mpin']=userdata[0]['Mpin']

            for i in newdata :
                userdata[0][i]=newdata[i]
            
            Bank.__update()

            print("Succesfullly updated.")

               
#=====================delete account===========

    def delete(celf):
        username=input("Enter your account number:-")
        mpin=int(input("Enter your Mpin:-"))

        userdata=[i for i in Bank.data if i['AccountNo.'] == username and i['Mpin']==mpin]
            
        if not userdata:
            print("Wrong Account no. or Mpin")
        else :
            confirm=input("Enter 'y' for yes and 'n' for no :-")
            if confirm=='y' :
                index=Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("Account delted successfully")
                Bank.__update()
            else:
                print("Not deleted")
        
    
#===========================new account creation=========================================
    def createaccount(self):
        info={
            "Name":input("Tell your name:-") ,
            "Age" : int(input("Tell your age:-")),
            "E-mail" : input("Enter your email:-"),
            "Mpin" : int(input("Tell your 4 number pin:-")),
            "AccountNo." : Bank.__accountgenerate(), 
            "Balance" : 0 
        }

        if info['Age']<18 or len(str(info['Mpin'])) !=4 :
            print("Sorry you cannot create your account.")
        else :
            print("Account has been created successfully")
            for i in info :
                print(f"{i}:{info[i]}")
            print("Please note down your account number.")
            Bank.data.append(info)
            Bank.__update()


#=========================user interaction space==========================================
user=Bank()
print("Press 1 for creating an account.")
print("Press 2 for deposite money in the bank.")
print("Press 3 for withdrawing the money.")
print("Press 4 for details.")
print("Press 5 for updating the details.")
print("Press 6 for deleting your account.")

response=int(input("Enter your response:-"))

if response == 1 :
    user.createaccount()

if response == 2 :
    user.depositemoney()

if response ==3 :
    user.withdraw()

if response == 4 :
    user.details()

if response == 5 :
    user.update()

if response == 6 :
    user.delete()

