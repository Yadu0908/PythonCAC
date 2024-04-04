## Concept of OOP's


1) Object-oriented programming (OOP) is a method of `structuring a program` by bundling related properties and behaviors into individual objects.

2) It contain's many of concepts like class's, object's, inheritance, abstraction and show on.

3) Defination of the class might looks like this.

```python

    class myClass:  # decleration of the class

        def __init__(self, name, password): # Constructor 

            self.name= name     #variable decleration.
            self.password= password
        
    c1= myClass("Aman", "123232")   #Object calling.

```

And, now in the above class we can access the variable's like `c1.name` or `c1.password`.

----
### Concept of inheritance-: <br> 
----
4) Inheritance models what’s called an is a relationship. This means that when you have a Derived class that inherits from a Base class, you’ve created a relationship where Derived is a specialized version of Base.


```python
class Car:

    def __init__(self, name, model):
        self.name= name
        self.model= model


    def printData(self):
            print(f"{self.name} => {self.model} => {self.battery}")

class Electric(Car):        # class inhertad

    def __init__(self,name, model, battery):

        super().__init__(name, model)
        self.battery= battery


ec = Car("Tesla", 53)
ev = Electric("Tesla", 53, "32Hr")
ev.printData()

```

### Concept of Encapsulation-: 

Encapsulation, which is the practice of obscuring data or implementation details within a class, is one of the fundamental concepts of object-oriented programming (OOP). 

`In other terms-:` Encapsulation is a technique for hiding a class’ internal operations and exposing only the information required for external interactions.

In Python we can `Private` a variable by using `__varnane` or (Double underscore).

A private vairable can't access directly through the object.
```python
class Car:

    def __init__(self, __brand, model): #brand is private variable
        self.__brand= __brand
        self.model= model
    
    def getBrand(self):
        return self.__brand


C1= Car("Tesla", "S34")
print(C1.getBrand())
```