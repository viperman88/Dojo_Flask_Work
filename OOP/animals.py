class Animal(object):

    def __init__(self, name):
        self.name = name
        self.health = 100

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def display_health(self):
        print "My name is " + self.name
        print "MY health is " + str(self.health)
        print ""
        return self

animal1 = Animal("Rufus")
animal1.walk().walk().walk().run().run().display_health()

class Dog(Animal):

    def __init__(self,name):
        super(Dog, self).__init__(name)
        self.health = 150

    def pet(self):
        self.health += 5
        return self

dog1 = Dog("Franklin")
dog1.walk().walk().walk().run().run().pet().display_health()

class Dragon(Animal):

    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170

    def fly(self):
        self.health -= 10
        return self

    def display_health(self):
        print "I am a Dragon"
        super(Dragon, self).display_health()
        return self

dragon1 = Dragon("Puff")
dragon1.fly().fly().fly().display_health()
