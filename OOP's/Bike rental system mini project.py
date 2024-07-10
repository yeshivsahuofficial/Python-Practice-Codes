class bikeShop:

    def __init__(self,stock):
        self.stock=stock
    def displayBike(self):
        print("Total Bikes:",self.stock)
    def rentForBike(self,quantity):
        if quantity<=0:
            print("Please enter a positve value: ")
        elif quantity>self.stock:
            print(f"Enter the value less than stock i.e., {self.stock}: ")
        else:
            self.stock=self.stock-quantity
            print("Total price: ",quantity*500)
            print("Availabel stocks of bike is:",self.stock)

while True:
    obj=bikeShop(100)
    userInput=int(input('''
1 Stocks
2 Bike Rent
3 Exit
    '''))

    if userInput == 1:
        obj.displayBike()
    elif userInput == 2:
        quantity = int(input("Enter the quantity of bike to rent:"))
        obj.rentForBike(quantity)
    else:
        break
