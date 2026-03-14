import random

userinp = int(input("enter the number of dice you want"))
record =[]
i=0
while i<userinp:
 roll = random.randint(1,6)
 record.append(roll)
 i+=1
print(record, end="")


