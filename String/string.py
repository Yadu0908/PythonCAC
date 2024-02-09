string1= "hello world"
string2 = " is concatinated"



print(string1[0])
print(type(string1))

print(string1[0:5])
print(string1[:])   #returns whole string
print(string1[: -1])    #whole string but 1 char not include from last
print(string1[0:11:2])  #skips each char after 1 
print(string1 + string2) #concatinate the string1 and stirng2

#string functions.

print(string1.upper())  #HELLO WORLD
print(string1.lower())  #hello world
print(string1.capitalize())  #Hello world
print(string1.split())  #['Hello', 'world']
print(string1.replace("Hello", "It's my")) #It's my world
print(string1.count("Hello")) #Counts how much time it include Hello

#string function for checking the specific condition.

print(string1.isalnum()) #Check the string is it alpha numeric
print(string1.isdigit()) #Check the string is an digit
print(string1.islower()) #Check the string is in lower case

#Some useful functions

print(len(string1)) #total letters on the string contain spaces
print(ascii(string1)) #total letters on the string contain spaces

#use of format()

var1= "Sachin"
var2= "Virat"
string= "{} and {} Play cricket"

print(string.format(var1, var2)) #Sachin and Virat Play cricket

#list into string

ls= ["cricket", "football", "tenis", "chess"]

print(" ".join(ls)) #cricket football tenis chess