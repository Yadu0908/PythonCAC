class myClass:  # decleration of the class

        def __init__(self, name, password): # Constructor 

            self.name= name     #variable decleration.
            self.password= password
        
c1= myClass("Aman", "123232")   #Object calling.

print(c1.name)
print(c1.password)