"""
Author:  Owen Widup
Date written: 11/29/2024
Assignment: Module #5 Assignment: #1 
Short Desc: The applicatio calculates the number of various types of items
(ex. Shirts, pants, etc.) that the clothing store has as well as the price of the individual types of clothing
and the overall price of the whole stock. Along with that, at any time, they can increase or
decrease the stock as they buy/sell more. 
"""
#imports GUI commands
from breezypythongui import EasyFrame

#Setting GUI Properties
class SDEV140_Final(EasyFrame):
    def __init__(self, title= "Clothing Store Manager"):
        EasyFrame.__init__(self)
        self.title = self.addLabel(text= "Clothing Store Manager (Press Enter after changing a stock value to update)", 
                                   row= 0, column= 0)
        #Shirt Stock
        self.addLabel(text= "Total Shirt Stock: ", row= 1, column= 0)
        self.shirtStock = self.addIntegerField(value= 0, row= 1, column= 1)
        self.shirtTotal = self.addIntegerField(value= 0, row= 1, column= 2, state= "readonly")
        self.addLabel(text= "Price Per Shirt: $20", row= 1, column= 3)
        self.shirtUpdate = self.addButton(text= "Update", row= 1, column= 4, command= self.shirtPrices)
        #Pants Stock
        self.addLabel(text= "Total Pants Stock: ", row= 2, column= 0)
        self.pantsStock = self.addIntegerField(value= 0, row= 2, column= 1)
        self.pantsTotal = self.addIntegerField(value= 0, row= 2, column= 2, state= "readonly")
        self.addLabel(text= "Price Per Pants Pair: $25", row= 2, column= 3)
        self.pantsUpdate = self.addButton(text= "Update", row= 2, column= 4, command= self.pantsPrices)
        #Jacket Stock
        self.addLabel(text= "Total Jacket Stock: ", row= 3, column= 0)
        self.jacketStock = self.addIntegerField(value= 0, row= 3, column= 1)
        self.jacketTotal = self.addIntegerField(value= 0, row= 3, column= 2, state= "readonly")
        self.addLabel(text= "Price Per Jacket: $35", row= 3, column= 3)
        self.jacketUpdate = self.addButton(text= "Update", row= 3, column= 4, command= self.jacketPrices)
        #Dress Stock
        self.addLabel(text= "Total Dress Stock: ", row= 4, column= 0)
        self.dressStock = self.addIntegerField(value= 0, row= 4, column= 1)
        self.dressTotal = self.addIntegerField(value= 0, row= 4, column= 2, state= "readonly")
        self.addLabel(text= "Price Per Dress: $45", row= 4, column= 3)
        self.dressUpdate = self.addButton(text= "Update", row= 4, column= 4, command= self.dressPrices)
        #Skirt Stock
        self.addLabel(text= "Total Skirt Stock: ", row= 5, column= 0)
        self.skirtStock = self.addIntegerField(value= 0, row= 5, column= 1)
        self.skirtTotal = self.addIntegerField(value= 0, row= 5, column= 2, state= "readonly")
        self.addLabel(text= "Price Per Skirt: $30", row= 5, column= 3)
        self.skirtUpdate = self.addButton(text= "Update", row= 5, column= 4, command= self.skirtPrices)
        #Sock Stock
        self.addLabel(text= "Total Sock Stock: ", row= 6, column= 0)
        self.sockStock = self.addIntegerField(value= 0, row= 6, column= 1)
        self.sockTotal = self.addIntegerField(value= 0, row= 6, column= 2, state= "readonly")
        self.sockUpdate = self.addButton(text= "Update", row= 6, column= 4, command= self.sockPrices)
        self.addLabel(text= "Price Per Sock Pair: $5", row= 6, column= 3)

    #Calculate Shirt Price
    def shirtPrices(self):
        self.shirtTotal["value"] = self.shirtStock.getNumber() * 20
    #Calculate Pants Price
    def pantsPrices(self):
        self.pantsTotal["value"] = self.pantsStock.getNumber() * 25
    #Calculate Jacket Price
    def jacketPrices(self):
        self.jacketTotal["value"] = self.jacketStock.getNumber() * 35
    #Calculate Dress Price
    def dressPrices(self):
        self.dressTotal["value"] = self.dressStock.getNumber() * 45
    #Calculate Skirt Price
    def skirtPrices(self):
        self.skirtTotal["value"] = self.skStock.getNumber() * 30
    #Calculate Sock Price
    def sockPrices(self):
        self.sockTotal["value"] = self.soStock.getNumber() * 5


#Executing the main window     
def main():
    SDEV140_Final().mainloop()

if __name__ == "__main__":
    main()