# Write a function that takes in any English word and turns it into pig latin.
# - Example input: “technique”, “omelet”, “string”
# - Example output: “echniquetay”, “omeletyay”, “ingstray”

print("Welcome to Pig Latin")
# create variable 
# in pig latin "ay" is added to everything and the first letter is added to the end of the word 
pyg = "ay"
original = input("Enter a Word:")
# isalpha is for numbers btw 
if len(original) > 0 and original.isalpha(): 
    word = original.lower()
    # saying that a new variable - word equals the original word thats entered by the user, and puts it into lower case. 
    first = original[0]
    # python counts words starting from 0, not 1.  
else: 
    print ("empty")
# new variable:
new_word = word + first + pyg
# saying the word starts on the first letter, not letter zero.
new_word = new_word[1:]
print(new_word)   


#  How do you do it so the first letter, if upper case goes to a lower case letter because the string converter did not work. 