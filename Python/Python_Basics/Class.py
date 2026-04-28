class car :
    def __init__(self,brand,color,name):
        self.brand = brand 
        self.color = color
        self.name = name
    def drive(self) :
        print(f"{self.brand} is driving")

    def info(self):
        print(f"Brand {self.brand}, Color : {self.color}")

    def driver(self):
        print(f"the driver name is {self.name}")





my_car = car("Toyota", "Red", "omer")
my_car.drive()  # prints: Toyota is driving!
my_car.info()
my_car.driver()