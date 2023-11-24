class vehicle:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

        print(f"{self.make} {self.model} launch in {self.year}")

class car(vehicle):
    def __init__(self, make, model, year,color):
        super().__init__(make, model, year)     ## imp line
        self.color=color
        print(f"the car is in {self.color} color.")

    def stop(self):
        print("the car has started.")

data=car("BMW","coupe",2005,"blue")    ##  imp line
data.stop()