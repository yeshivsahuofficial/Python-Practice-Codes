class Account:

    def __init__(self,balance,accNumber):
        self.balance=balance
        self.accNumber=accNumber
    
    #Debit
    def debit(self,amount):
        self.balance -= amount
        print("Rs.",amount ,"was debited")
        print("Total balance is:",self.get_balance())

    #Credit
    def credit(self,amount):
        self.balance += amount
        print("Rs.",amount ,"was credited")
        print("Total balance is:",self.get_balance())

    def get_balance(self):
        return self.balance

acc1=Account(10000,12345)
acc1.debit(500)

acc1.credit(200)
        