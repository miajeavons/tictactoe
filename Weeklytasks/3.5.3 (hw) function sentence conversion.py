# Write another function that converts a whole sentence from original english to pig latin. 

print("Welcome to Pig Latin")
# create variable 
# in pig latin "ay" is added to everything and the first letter is added to the end of the word 
pyg = "ay"
original = input("Enter a Sentence:")
# isalpha is for numbers btw 
# IDK HOW TO DO THAT --- WORK IN PROGRESS. 

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