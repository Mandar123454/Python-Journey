from car import Car

car_1 = Car("Chevy","Corvette","2021","blue")
car_2 = Car("Ford","Mustang","2022","red")

#car_1.wheels = 2

Car.wheels = 2

print(car_1.wheels)
print(car_2.wheels)

#print(Car.wheels)

# an instance variable is declared inside of constructor and they can be given unique values
# an class variables they are declared within a class but outside of the constructor & you can set default value for all instances of unique class & you can change those values


