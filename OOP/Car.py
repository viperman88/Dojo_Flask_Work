
# create class Car
class Car(object):

    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.displayInfo()

    def displayInfo(self):
        print "Price: $" + str(self.price)
        print "Speed: " + str(self.speed) + "mph"
        print "Fuel: " + self.fuel
        print "Mileage: " + str(self.mileage) + "mpg"
        print "Tax: " + str(self.tax) + "%"

car1 = Car(5000,110,"half",20)

car2 = Car(15000,145,"full",22)

car3 = Car(8000,90,"empty",45)

car4 = Car(45000,180,"quarter",7)

car5 = Car(18000,160,"half",28)

car6 = Car(5000,96,"full",60)
