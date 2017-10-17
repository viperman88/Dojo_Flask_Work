
# Creating a class called Bike
class Bike(object):

    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print "This bike costs $" + str(self.price)
        print "It's maximum speed is " + str(self.max_speed) + "MPH"
        print "Total miles on this bike are " + str(self.miles)

    def ride(self):
        print "Riding"
        self.miles += 10

    def reverse(self):
        print "Reversing"
        if self.miles >= 5:
            self.miles -= 5

bike1 = Bike(274.99, 20)
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()

bike2 = Bike(167.49, 15)
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()

bike3 = Bike(110.99, 10)
bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayInfo()
