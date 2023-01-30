#Printing a loop
for counter in [1,2,3,4,5]:
    print("This is a loop : Counter = " , counter)

#Example
#Write a programe to compute the sum of all even numbers upto 100, inclusing 100 using a loop
print("\n***Example***")

total = 0 #assign the total in the begining to 0
for counter in range(0,101,2): #go through all even numbers between 0 to 101
    total = total + counter #get total so far
print("Total : ", total)#Printing total
