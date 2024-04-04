class Car:

    def __init__(self, __brand, model):

        self.__brand= __brand
        self.model= model
    
    def getBrand(self):

        return self.__brand

C1= Car("Tesla", "S34")

print(C1.getBrand())