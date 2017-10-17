
class Product(object):

    def __init__(self, price, item_name, weight):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.status = "For Sale"
        self.cost = 0

    def Sell(self):
        self.status = "Sold"
        self.price = 0
        return self

    def Add_Tax(self,tax):
        total = self.price * tax
        self.cost = self.price + total

    def Return(self,status):
        if status == "defective":
            self.status = "defective"

        elif status == "opened":
            self.status = "used"
            discount = self.price * .2
            self.price -= discount

        elif status == "like_new":
            self.status = "For Sale"

    def displayInfo(self):
        print "Name: " + self.item_name
        print "Status: " + self.status
        print "Weight: " + str(self.weight) + "lb"
        print "Price: $" + str(self.price)
        print "Cost w/tax: $" + str(self.cost)
        print "        "
        return self

product1 = Product(24.99,"dish set",2)
product1.Return("defective")
product1.displayInfo()

product2 = Product(668.99,"oven",110)
product2.Return("opened")
product2.Add_Tax(.15)
product2.displayInfo()

product3 = Product(1099.98,"65in LCD",35)
product3.Return("like_new")
product3.Add_Tax(.25)
product3.displayInfo()

product4 = Product(368.98,"Lawnmower",60)
product4.Add_Tax(.35)
product4.displayInfo()

product5 = Product(110.99,"Sneakers",4)
product5.Sell().displayInfo()
#product5.displayInfo()
