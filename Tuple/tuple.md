## Tuple

1) Implemented version of `list` which is immutable (It can't be change).
<br>
Or In simple we can say  a tuple is a built-in data type that allows you to create immutable sequences of values.

2) Tuple is initilized with `()` or `parenthesis`.

3) Basic syntax for python. 
```python
    tuple1= ('Sachin', 'Virat', 'Rohit', 'Dhoni')
```
4) And we can also create an instance of `tuple` or an tuple with `tuple()`.

5) We can concatinate our tuple same as list.

```python
    tuple1= ('Sachin', 'Virat', 'Rohit', 'Dhoni')
    tuple2= ('Rohit', 'Dhawan', 'Kapil', 'Dravid')

    print(tuple1+ tuple2)   
    #('Sachin', 'Virat', 'Rohit', 'Dhoni', 'Rohit', 'Dhawan', 'Kapil', 'Dravid')
```

6) Sometime we can also get the `tuple` inside the `tuple`.
```python
    t1= ('Aman', 'Vijay', ('English', 'Hindi'))

    print(t1[2][1])     #Hindi
```

7) We can also use skip element in `tuple`.

```python
    tuple2= ('Rohit', 'Dhawan', 'Kapil', 'Dravid')
    print(t2[1::2])     #('Dhawan', 'Dravid')

```

8) Python has the notion of `packing` and `unpacking` tuples. We can use them for assiging the variable to value through the tuple elements. 

```python
    #Packing and unpacking in tuple with python

    tuple3= (1,2,3,4,5,6,7)
    x,y,z,a,b,c,d = tuple3
    print(a)      #4

```

9) In python, We have an built-in funciton 