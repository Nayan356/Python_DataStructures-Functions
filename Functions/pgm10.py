# Write a program which can filter() to make a list whose elements are even number
#  between 1 and 20 ( both included)
# Python code to filter even values from a list 

# Initialisation of list 
lis = [1,2,3,4,5.6,7,8] 

# Output list initialisation 
out = [] 

for num in lis: 
	
	# checking condition 
	if num % 2 == 0: 
		out.append(num) 
		

# printing output 
print(out) 
