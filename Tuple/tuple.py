#Basic tuple syntex

t1= ('Sachin', 'Virat', 'Rohit', 'Dhoni')
print(t1)

#Can concatinate our tuple same as list

t2= ('Rohit', 'Dhawan', 'Kapil', 'Dravid')

print(t1+ t2)   #('Sachin', 'Virat', 'Rohit', 'Dhoni', 'Rohit', 'Dhawan', 'Kapil', 'Dravid')

t1[3] #For getting the element at 3rd index in t1 tuple.

#Tuple inside the tuple

t1= ('Aman', 'Vijay', ('English', 'Hindi'))

print(t1[2][1])

#Fetch the element at continuous break.

print(t2[1::2])     #('Dhawan', 'Dravid')


#Packing and unpacking in tuple with python

tuple3= (1,2,3,4,5,6,7)

x,y,z,a,b,c,d = tuple3

print(d)