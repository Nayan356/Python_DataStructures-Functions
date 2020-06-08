# Flatten the list [[1,2,3].,[4,5],[6,7,8]] into [1,2,3,4,5,6,7,8] using reduce
# Goal : Turn [1,2,3,4,5,6,7] to 1234567 
lists = [[1, 2, 3], [4, 5], [6, 7, 8]]
joinedlist = []
for list in lists:
	joinedlist += list

print(joinedlist)  # prints [1, 2, 3, 4, 5, 6, 7, 8]