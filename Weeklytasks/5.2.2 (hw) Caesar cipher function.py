# Implement a Caesar Cipher function that takes a string and shift amount, outputs the encrypted string. - Input: hello word - Shift by: 7 - Output: olssv dvysk
 # caesar cipher - incryption method - abcdefghijklmnopqrstuvwxyz --> would shift everything by a factor of 4 - efghijklmnopqrstuvwxyzabcd ; then a would be e and ect. 


# def caesar_encrypt(realText, step):
#     # initialize two empty lists to store the output and the corresponding numeric values. 
#     outText = []
#     cryptText = []

#     # Define lists for uppercase and lowercase letters of the English alphabet. 
#     uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# # Iterate through each letter in the 'realText' string.
#     for eachLetter in realText:
#         # Check if the letter is an uppercase letter.
#         if eachLetter in uppercase:
#             # Find the index of the letter in the 'uppercase' list.
#             index = uppercase.index(eachLetter)
            
#             # Perform Caesar cipher encryption by adding 'step' and taking the modulus 26.
#             crypting = (index + step) % 26
#             cryptText.append(crypting)

#             # Find the new letter corresponding to the encrypted value and append it to the 'outText' list.
#             newLetter = uppercase[crypting]
#             outText.append(newLetter)
#         # Check if the letter is a lowercase letter.
#         elif eachLetter in lowercase:
#             # Find the index of the letter in the 'lowercase' list.
#             index = lowercase.index(eachLetter)

#             # Perform Caesar cipher encryption by adding 'step' and taking the modulus 26.
#             crypting = (index + step) % 26
#             cryptText.append(crypting)

#             # Find the new letter corresponding to the encrypted value and append it to the 'outText' list.
#             newLetter = lowercase[crypting]
#             outText.append(newLetter)

#     # Return the 'outText' list containing the encrypted letters.
#     return outText

# # Call the caesar_encrypt function with the input 'abc' and a step of 2, and store the result in 'code'.
# code = caesar_encrypt('abc', 2)

# # Print an empty line for spacing.
# print()

# # Print the 'code', which contains the result of the Caesar cipher encryption.
# print(code)

# # Print an empty line for spacing.
# print()

# SOURCE: https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-25.php 

# ONE WAY
# cipher = ["a", "b", "c", "d", "e", "f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
# # made a list 
# def encrypt(word, shift):
#     result = "" 
#     # made an empty string
#     for i in word: 
#         for j in cipher: 
#             if i == j: 
#                 result = result + cipher[shift]
#                 # tracking how many times its gone through the main alphabet list


cipher = ["a", "b", "c", "d", "e", "f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
# # made a list 
def encrypt(word, shift):
    # list1 = cipher[:shift]
    # # shift list from the left 
    # list2 = cipher[shift:]
    # # shift list from the right
    # list3 = list2 + list1
    # # adds both lists together
    # # to make more consise: 
    list1 = cipher[:shift] + cipher[shift:] 
   
    table = dict(zip(cipher,list1))
# zip pairs them together
    
    for i in word: 
        letter = table[i]
        print(letter, end="")
encrypt("hello world", 7)
 
