# Write a program in Python to iterate through the string 
# “hello my name is abcde” and print the string which has even length of word.
def printWords(s):

# split the string
    s = s.split(' ')
# iterate in words of string
    for word in s:
        if len(word)%2==0:
            print(word)
# main
s = "Hello my name is abcde"
printWords(s)