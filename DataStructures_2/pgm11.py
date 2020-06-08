# Write a program to find out the occurrence of a specific word 
# from an alphanumeric statement. Example: 12abcbacbaba344ab  
# Output: a=5 b=5 c=2 make sure you should avoid the numbers in you logic
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( word_count('This is a good day to learn python'))
