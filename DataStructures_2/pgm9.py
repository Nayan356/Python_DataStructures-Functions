# Write a program in python to print the pair of numbers 
# whose sum is equal to result number that is let's say 8.

class py_solution:
   def twoSum(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target - num], i )
            lookup[num] = i
print("index1=%d, index2=%d" % py_solution().twoSum((2,3,1,6,10),8))
