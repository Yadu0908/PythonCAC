ls = ["Sachin", "Virat", "Rohit", "Dhone", "Kapil"]

print(ls)   #['Sachin', 'Virat', 'Rohit', 'Dhone', 'Kapil']
print(ls[0:1])  #['Sachin']
print(ls[:])    #Return the whole list

ls[2]= "Sahwag"
print(ls)       #it will chnage Rohit into Sahwag

ls[1:3] = ["Dhawan", "Bumrah"]  #For changing the more then 1 data at a time.
print(ls)

ls[1:1] = ['Virat', 'Rohit']    #Adds 2 elemnts after 1 index.
print(ls)

ls[3:5]= []     #Remove the item num 3 and 5 both.
print(ls)

#Loop operations in the list items


for i in ls:
    print(i, end=", ")

#list functions

numLs= [1,3,83,43,45,65,6]
numLs.sort()    #sort the list
len(numLs)      #lenght of list
max(numLs)      #max number on list
min(numLs)      #minimum number on list

#list methods

numLs= [1,3,83,43,45,65,6]
numLs.append(20)  #append at the end of the list
numLs.clear()     #delete the whole list
numLs.copy()      #For making an swallow copy the list
numLs.count()     #count the element on the list
numLs= [1,3,83,43,45,65,6]
num1= [3,4,5]
numLs.extend(num1) #joins the both list
numLs.index()      #returns the index of the given element
numLs.insert(89, 6) #insert the element at given index
numLs.pop()         #Can pass an argument otherwise it will poped out from the last.

#list comprehension

new_list= [x ** 2 for i in range(10)]

