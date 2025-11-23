class Animal: # parent class

    def eat(self):
        print("This animal is eating")

class Rabbit(Animal): # rabbit child class
    #pass
    def eat(self):
        print("This rabbit is eating carrot")

rabbit = Rabbit()
rabbit.eat()