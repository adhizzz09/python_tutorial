# Base Class
class Vehicle:
    def __init__(self, vehicle_id, brand, price):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.price = price

    def display_vehicle(self):
        print("Vehicle ID:", self.vehicle_id)
        print("Brand:", self.brand)
        print("Price:", self.price)


# Derived Class
class Car(Vehicle):
    def __init__(self, vehicle_id, brand, price, num_doors, fuel_type):
        super().__init__(vehicle_id, brand, price)
        self.num_doors = num_doors
        self.fuel_type = fuel_type

    def display_car_details(self):
        self.display_vehicle()
        print("Doors:", self.num_doors)
        print("Fuel Type:", self.fuel_type)
        print()


# Creating objects
car1 = Car(201, "Toyota", 800000, 4, "Petrol")
car2 = Car(202, "Honda", 900000, 4, "Diesel")

# Displaying details
car1.display_car_details()
car2.display_car_details()