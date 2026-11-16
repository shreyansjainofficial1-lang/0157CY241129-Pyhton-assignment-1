class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show_vehicle(self):
        print("Brand:", self.brand)

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def show_car(self):
        print("Model:", self.model)

class ElectricCar(Car):
    def __init__(self, brand, model, battery_range):
        super().__init__(brand, model)
        self.battery_range = battery_range

    def show_details(self):
        self.show_vehicle()
        self.show_car()
        print("Battery range:", self.battery_range, "km")

car = ElectricCar("Tata", "Nexon EV", 300)
car.show_details()
