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