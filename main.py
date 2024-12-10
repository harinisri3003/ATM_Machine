class Bank:
    def __init__(self):
        self.closingBal=0
    def display(self):
        print("Enter Your Options: ")
        print("1 for deposit: \n 2 for withdraw:")
        getOption =input()

        if getOption == "1":
            self.deposit()

        elif getOption=="2":
            self.withdraw()
        
        elif getOption !=1 or getOption !=2:
            print("Thanks")
            return
        
        print("Your closing balance is :",self.closingBal)
        print("Do you want to continue:")
        a=input()
        if a =="Y" or a =='y':
            self.display()
        else:
            print("Thanks for visting our bank")
    
    def deposit(self):
        depositAmount = int(input("Enter your deposit Amount:"))
        self.closingBal=self.closingBal+depositAmount
        return self.closingBal
    
    def withdraw(self):
        withdrawAmount = int(input("Enter your withdraw Amount: "))
        if self.closingBal>=withdrawAmount:
            self.closingBal=self.closingBal-withdrawAmount
            print("After withdraw your balance amount is :",self.closingBal)
        else:
            print("No sufficient balance")
        return self.closingBal
bankObj =Bank()
bankObj.display()