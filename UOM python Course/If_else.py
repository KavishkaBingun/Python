#in if statements execute all the statements weather it correct or wrong
x = 6

if x >= 7 :#This line execute but this Wrong
    print("Over 7")#This not excute
if x >= 5 : #This line execute and its correct
    print("Over 5")#This line execute
if x >= 2 : #This line execute and its correct
    print("Over 2")#This line execute
if x <= 2 : #This line execute but this Wrong
    print("Under 2")#This not excute



#in elif statements only execute lines until meet the correct line
x = 6

if x >= 7 : #This line execute but this Wrong
    print("Over 7") #This not excute
elif x >= 5 : #This line execute and its correct
    print("Over 5") #This line execute
elif x >= 2 : #This not excute
    print("Over 2")#This not excute
else  : #This not excute
    print("Under 2")#This not excute
