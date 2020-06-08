# Write a program to get the sum and multiply of all the items in a given list.
numbers=[1,2,3]
total = 1
res=1
for x in numbers:
    total *= x  
print(total)
for y in numbers:
    res +=y
print(res)
