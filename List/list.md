## List in python

1) The list class is a `fundamental built-in data type` in Python. It has an impressive and useful set of features, allowing you to efficiently organize and manipulate heterogeneous data.
2) list is `Mutable` which stands for it can be chnage.

3) Basic list is given below.
```python
    ls = ["Sachin", "Virat", "Rohit", "Dhone", "Kapil"]

    print(ls)   #['Sachin', 'Virat', 'Rohit', 'Dhone', 'Kapil']
``` 

4) A list can contain `Hetrogenious` mixture of elements.
```python
    ls = [ (1,2,3), 7,6, {"eight": 8, "nine": 9}] #This list contain tuple, dictionary and basic elements.
```

5) We can initilize our list by thorough `list()` or can say list `constructor`.

```python
    list((1,2,3,4,5,6,7))
```

6) We can do different operations on our list and play with it.

```python
    ls = ["Sachin", "Virat", "Rohit", "Dhone", "Kapil"]

    print(ls)   #['Sachin', 'Virat', 'Rohit', 'Dhone', 'Kapil']
    print(ls[0:1])  #['Sachin']
    print(ls[:])    #Return the whole list

    ls[2]= "Sahwag"
    print(ls)       #it will chnage Rohit into Sahwag

    ls[1:3] = ["Dhawan", "Bumrah"]  #For changing the more then 1 data at a time.
    print(ls)

    ls[1:1] = ['Virat', 'Rohit']    #Adds 2 elemnts after 1 index.

    ls[3:5]= []     #delete both the elemnts


```

7) We can use `loop` operations in our list.

```python
    for i in ls:
    print(i)    #Prints the whole list items
    print(i, end= ",")  #return , after every element
```

8) List contain different `Function` which can be use for implementing the list.

```python
    #list functions

    numLs= [1,3,83,43,45,65,6]
    numLs.sort()    #sort the list
    len(numLs)      #lenght of list
    max(numLs)      #max number on list
    min(numLs)      #minimum number on list

```

9) List contain different `Methods` also, which an user can use for implementing the list according to his.

```python
    #list methods

    numLs= [1,3,83,43,45,65,6]
    numLs.append(20)  #append at the end of the list
    numLs.clear()     #delete the whole list
    numLs.copy()      #For making an copy the list (allocate in different location)
    numLs.count()     #count the element on the list
    numLs= [1,3,83,43,45,65,6]
    num1= [3,4,5]
    numLs.extend(num1) #joins the both list
    numLs.index()      #returns the index of the given element
    numLs.insert(89, 6) #insert the element at given index
    numLs.pop()         #Can pass an argument otherwise it will poped out from the last.
    numLs.remove()      #for removing the elemnt
```

10) ___Here is the short note about `insert` and `append`.<br>
insert() takes two argument (element, index), but whereas append() takes one argument (element)___.

### List Comprehension
It is a technique for acheiving the code reusability in the Python. Where we can transform our list can convert 3 or 4 line of code into a single line or code.
Example as shown below. 

```python
    #before list comprehension

    new_list= []
    for i in range(10):
        new_list.append(i ** 2)

    #after list comprehension
    new_list= [x ** 2 for i in range(10)]
```
So here is the difference so that we can implement our logic into single line of code from 3 line of code. This type of logic will works with code reusablility feature in programming lanuages.