# Create a list of size 5 and execute the slicing structure 
py_list = ['n', 'a', 'y', 'a', 'n']
slice_object = slice(0, 5, 2)
slice_object1 = slice(1, 5, 2)
slice_object2 = slice(0, 4, 1)
print(py_list[slice_object])
print(py_list[slice_object1])
print(py_list[slice_object2])