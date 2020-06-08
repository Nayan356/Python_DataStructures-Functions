# Create a new list which contains the specified numbers after removing the even numbers from a predefined list.
num = [7,8, 120, 25, 44, 20, 27]
num = [x for x in num if x%2!=0]
print(num)