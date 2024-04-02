## Function in python.

1) In Python we use the function as function defination.

2) A function is a self-contained block of code that encapsulates a specific task or related group of tasks. 

3) Basic syntex of python as follow.

```python
    def functionName(parameters){
        #code inside the python function
    }
```

4) It's not necessery to take more then 1 parameters in the function.
```python
    def functionName(parameter1, parameter2){
        #code inside the python function
    }
```

5) Polymorphism example with python.

```python
    def sum(a, b):
        return a+b;

    print(sum("HEllo", "WOrld"))

    print(sum(3,4))   
```
It mean it can handles the sum of digits and string both.


### Lambda function
---

`Lambda` function's are the function those don't have their any specific name, they are just use as `call and return.`<br>
In simple we can say `A lambda function` is a function which is just initilized in single line of code and used to do some simple problem without wasting the lot of line of code.

```python
    cube= lambda x: x**3; 
    print(cube(2))    #It will return the 8.
```
<br>

### *args in function
---
`*args` in function definitions in python is used to pass a variable number of arguments to a function. <br>
In other word's, `*args` is used to pass the the number of variable's in a function without giving them a name.

```python 
    def sum(*args):

        return sum(args)

    print(sum(3,4,5))  
    print(sum(3,4,5,4,5,6))  
    print(sum(3,4,5,6,7,8,7,3,2,9))

    #This sum function will works on the all of the above cases.  
```
* *args return's a tuple of the elements.


### **kwargs in function

`**kwargs` took the input in the `key`, `value` pair.

```python
def sayData(**kwargs):

    for key, value in kwargs.items():

        # print(type(kwargs)) #return's the dict object.
        print(f"{key}: {value}");

sayData(name= "Amna")
sayData(name="Aman", password= 1234567)
sayData(name="Aman", password= 1234567, place= "Bazpur")

```

* **kwargs return's the dictionary of the elements.

---
#### In python `*` symbole is known as unpacking operators.

Unpacking operators are operators that unpack the values from iterable objects in Python. The single asterisk operator * can be used on any iterable that Python provides, while the double asterisk operator ** can only be used on dictionaries.


---
### Yield in python

The Yield keyword in Python is similar to a return statement used for returning values or objects in Python. However, there is a slight difference. The yield statement returns a generator object to the one who calls the function which contains yield, instead of simply returning a value. 

Let's get through the concept of yield with real world example.

<p style= "color: #46dd4d; font-weight: 500; font-size: 18px;">Problem-:</p>
 

```python
def evenNumber(num):

    for i in range(2, num+1, 2):

        return i

print(evenNumber(10))
```
<p style= "color: #fbc42f; font-weight: 600">Here we can clearly notice that when we call the evenNumber() then it will return only the single value on the output but we don't need an single value output.</p>

But, suppose if we try to this thing with our code then.....

```python
for i in evenNumber(10):
    print(i);
```
<p style= "color: #ff5259; font-weight: 500; font-size: 18px;">Error-:</p>

```python
Traceback (most recent call last):
  File "/workspace/PythonCAC/Functions/yield.py", line 9, in <module>
    for i in evenNumber(10):
TypeError: 'int' object is not iterable
```
which mean we can't iterate our function like this whenever we are using the `return` keyword on a function.

So, for solving this problem in python we use an keyword called `yield`.

```python
def evenNumber(num):
    for i in range(2, num+1, 2):
        yield i

for i in evenNumber(10):
    print(i);
```
And now it will return the even number digit from 2 to 10.