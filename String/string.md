## String Manupulation in Python.

1) Collections of text in Python are called strings, `And we can also treat our string as a list of character as other languages`.

2) As we can see an example of string treating as list but if we try to fetch the type of string1 variable it will return `<class 'str'>`.

```python
    string1= "Hello world"
    print(string1[0]) #It will return H
    print(type(string1)) #return <class 'str'>
```

3) As we can also do `slicing` our string, And play with it.
```python
    string1= "Hello world"
    print(string1[0:5]) #It will return Hello
    print(string1[:])   #returns whole string
    print(string1[: -1]) #whole string but 1 char not include from last
    print(string1[0:11:2])  #skips each char after 1 
    print(string1 + string2) #concatinate the string1 and stirng2
```

4) Python provides a lot of built-in functions to manipulate strings. Python String is immutable, so all these functions return a new string and the original string remains unchanged. Some of `String functions are as below`,

```python
#We can see all the string functions on our vs-code IDE while typing name of variable and then '.' ,It will show the whole functions.

#string functions.

print(string1.upper())  #HELLO WORLD
print(string1.lower())  #hello world
print(string1.capitalize())  #Hello world
print(string1.split())  #['Hello', 'world']
print(string1.replace("Hello", "It's my")) #It's my world

#string function for checking the specific condition.

print(string1.isalnum()) #Check the string is it alpha numeric
print(string1.isdigit()) #Check the string is an digit
print(string1.islower()) #Check the string is in lower case

#Some useful functions

print(len(string1)) #total letters on the string contain spaces
print(ascii(string1)) #total letters on the string contain spaces


````
<a href= "https://www.digitalocean.com/community/tutorials/python-string-functions" style =" color: doer blue; font-weight: 600; text-decoration: underline">Click me</a> for all the string operation and their use in Python with their importance.
