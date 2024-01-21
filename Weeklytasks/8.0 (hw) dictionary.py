# Given a text file as a command line argument, read the text file and do spell checks on individual words in the text file (a list of english words will be provided as another command line argument)
# Output the spell check corrected file to another location specified by another command line argument
# Print into the console any number of relevant information that you deem necessary
# Example command: python3 main.py -i cyberspace.txt -o corrected.txt -d dictionary.txt
# Example files available below.

# from levenshtein import distance 
from turtle import distance


text = open("cyberspace.txt")
lines = text.readlines()
# print(lines)
# Load in dictionary 
dictionary_file = open("dictionary.txt")
dictionary = dictionary_file.readlines()
print(dictionary)
for index, word in enumerate(dictionary): 
  dictionary[index] = word.strip()

# # split into words 
split_lines = []
for line in lines: 
    split_lines.append(line.split(""))

# spellchecking
for line in split_lines:
   for i, word in enumerate(line): 
    if word.lower().strip() in dictionary or word == "/n":
        #  spelled correctly 
        line[i] = word 
    else:
    #   misspelled 
        minimum = 3
        correct_word = word 
        for dict_word in dictionary: 
           final_distance = distance(word.lower(),dict_word)
           if minimum > final_distance:
              minimum = final_distance
              correct_word = dict_word 

        print(str(minimum)+ " " + correct_word)
        line[i] = correct_word 

#  output text 
join_lines = []
for split_line in split_lines: 
   join_lines.append(" ".join(split_line))

with open("./corrected.text", "w") as file: 
   file.write("".join(join_lines))

# - followed video to help 