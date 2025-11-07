# Car class with attributes and methods

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False
    
    def start(self):
        if not self.is_running:
            self.is_running = True
            print(f"{self.year} {self.make} {self.model} is now running.")
        else:
            print("Car is already running!")
    
    def stop(self):
        if self.is_running:
            self.is_running = False
            print(f"{self.year} {self.make} {self.model} has stopped.")
        else:
            print("Car is already stopped!")
    
    def display_info(self):
        status = "running" if self.is_running else "stopped"
        print(f"\nCar Info: {self.year} {self.make} {self.model}")
        print(f"Status: {status}")

# Example usage
car1 = Car("Toyota", "Camry", 2023)
car1.display_info()
car1.start()
car1.display_info()
car1.stop()
car1.display_info()
