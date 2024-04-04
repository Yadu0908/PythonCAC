class Car:

    def __init__(self, name, model):
        self.name= name
        self.model= model


    def printData(self):
            print(f"{self.name} => {self.model} => {self.battery}")

class Electric(Car):

    def __init__(self,name, model, battery):

        super().__init__(name, model)
        self.battery= battery


ec = Car("Tesla", 53)
ev = Electric("Tesla", 53, "32Hr")
ev.printData()