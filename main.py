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
    @staticmethod
    
    def update() :
        with open(Bank.database,'w') as fs :
            fs.write(json.dumps(Bank.data))

    def createaccount(self):
        info={
            "name":input("Tell your name:-") ,
            "age" : int(input("Tell your age:-")),
            "email" : input("Enter your email:-"),
            "pin" : int(input("Tell your 4 number pin:-"))
            "accountNo." : 1234 , 
            "balance" : 0 
        }


    if info['age']<18 or len(str(info['pin'])) !=4 :
        print("Sorry you cannot create your account.")
    else :
        print("Account has been created successfully")
        for i in data :
            print(f"{i}:{info[i]}")
        print("Please note down your account number.")
        Bank.data.append(info)
        


user=Bank() :


print("Press 1 for creating an account.")
print("Press 2 for deposite money in the bank.")
print("Press 3 for withdrawing the money.")
print("Press 4 for details.")
print("Press 5 for updating the details.")
print("Press 6 for deleting your account.")

response=int(input("Enter your response:-"))

if response == 1 :
    user.Createaccount()