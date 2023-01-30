#Accessing a List
#Printing all Values
print("Printing all value")
Values = [15,20,96,32,17,]
print (Values)

#Printing one value
print("\nPrinting one value")
print (Values[3])# inside square bracket should type index of the relevrnt value

#Printing value range
print("\nPrinting value range")
print (Values[0:3])
print (Values[2:5])

#Adding new value to end of the list
print("\nAdding new value to end of the list")
Values.append(60)
print (Values)

#Deleting a value from the list
print("\nDelete a value from the list")
Values.remove(60)
#del Values[2]
print(Values)


#Updating a value in a list 
print("\nUpdating a value in a list")
Values[2] = 60
print (Values)

#Exercise 01
print("\n***Exercise 01 ***")
list = ['ph','ch',1997,2000,2000,2009]
list[2] = 2001
list.remove(2000)
list.append(2015)
print(list[2:])

#Multi - Dimentional Lists
print("\n***Multi - Dimentional Lists***")
data = [[1,1,1] , [2,2,2] , [3,3,3]]
print(data)

#printing one value
print("\nprinting one value")
print(data [2][2])#Printing 3 in the 3rd row 3rd column

#Update a value
print("\n***Update a value***")
data [0][1] = 5
print(data)

#Add new value
print("\n***Add new value***")
data[2].append (10)
print(data)

#Exercise 2
print("\n***Exercise 2***")
num_list = [2,4,6,8,3,4,2,1] #list of all numbers
even_list = [] #defining a list to store even numbers
for i in num_list: #go through all indexes inside num_list
    if (i%2==0) and (i not in even_list):#check the numbers are even and they do not repeat
        even_list.append(i)#add all selected numbers to even_list
print(even_list)#printing even_list








