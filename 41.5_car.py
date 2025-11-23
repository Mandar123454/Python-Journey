class Car:

    def __init__(self,make,model,year,color): # special method called constructor
        self.make = make  # attributes
        self.model = model
        self.year = year
        self.color = color

    # methods
    #def drive(self):
    #    print("This car is driving")

    def drive(self):
        print("This "+self.model+" is driving")

    # def stop(self):
    #     print("This car is stopped")

    def stop(self):
        print("This "+self.model+" is stopped")

