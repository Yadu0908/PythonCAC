<body style ="background-color: #171717; color: #fff;">

# Numbers in python.

1) We dont have to use keyword's while making variable or defining variables.

2) We can convert our numbers (deciaml) into other like binary, octal, hexa-decimal. By using built in function's as shown below:
```python
    number = 128; 
    print(bin(number))
    print(hex(number))
    print(oct(number))

````

3) We can also convert by using: 

```python
    int('42', 8)    #this will convert 42 into octal
```

4) We can also use `random` liberary, which is capable of handing random number's and random data.

```python
    import random

    random.random()    #Display random number's like 0.8247234289359883

    random.randint(1,10) #random number btw 1 and 10

    ls= ['tea', 'coffee', 'mink', 'juice', 'softy']

    random.choice(ls) #random choice btw list `ls`

    random.shuffle(ls) #Shuffle's the list `ls`
```
5) We might get some random value's whlie doing operation on floating point numbers, Like shown below:

```python
    print((0.1) + (0.1) + (0.1) - (0.3))
```
<p style="color: Red;">5.551115123125783e-17</p>
But we know at this condition it is wrong answer.

<p style="color: #ffd254;">So, the solution for this condition is importing decimal liberary.</p>

```python
    from decimal import Decimal
    print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))
    
```

6) Now lets play with `Set's`

```python
    set1= {1,2,3}

    print(set1 & {2,3})     #For intersection.
    print(set1 | {2,3})     #For union.
    print(set1 - {2,3})     #For difference.

```
* In python `Empty set` is represented as `set()` not like `{}`, this is because the `empty curly braces` mean dictionary data type but set is an another data type.
</body>

----
7) Here in python we always confuse between `function` and `method`, So here is the difference.

- `Function` can be defined anywhere on the program or file.
- `Method` should be always defined inside the class and should contain one parameter atleast name `self`.