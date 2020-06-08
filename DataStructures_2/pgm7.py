# # Write a program in Python to reverse a string and 
# # print only the vowel alphabet if exist in the string with their index.

def reverse_string(str1):
    return ''.join(reversed(str1))
print()
print(reverse_string("random"))
print(reverse_string("consultadd"))
print()

# def vowel(text):
#     vowels = "aeiuoAEIOU"
#     print(len([letter for letter in text if letter in vowels]))
#     print([letter for letter in text if letter in vowels])
# vowel('consultadd')