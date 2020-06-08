# Create a new dictionary by concatenating the following two dictionaries:
# a={1:10,2:20}
# b={3:30,4:40}
# Expected Result: {1:10,2:20,3:30,4:40}
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3 = {}
for d in (dic1, dic2): dic3.update(d)
print(dic3)