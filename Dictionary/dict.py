dict1= {'Aman': 20, 'Virju':30, 'Sonam': 90} #basic syntex.

print(dict1)

print(dict1['Sonam'])   #90

print(dict1.get('Sonam'))   #90

dict1['Aman']= 80   #chnage the value of Aman into 80

print(dict1['Aman'])

for i in dict1:

    print(i, dict1[i])


for key, values in dict1.items():

    print(key, values)

#Dictionary built in methods.

len(dict1)  #For finding the lenght

dict1['Komal']= 33 #Add an elemnt into the dictionary
print(dict1) 

dict1.pop('Aman')  #For poping it out
print(dict1) 

dict1.popitem()    #Autometically remove last one
print(dict1)

dict2 =dict1.copy() #copy the elements of the dictionary
print(dict2)

dict2.update({'uday':89, 'ankur': 28 }) #adds the element of dictionary
print(dict2)

#Squred number problem with Dictionary:

squre_num= {x: x**2 for x in range(20)}
print(squre_num)

#Making dictionary from the list and elements

ls= ['aman', 'vijay', 'rakesh', 'aditya']

value= 'pass'

new_dict= dict.fromkeys(ls, value)
print(new_dict)