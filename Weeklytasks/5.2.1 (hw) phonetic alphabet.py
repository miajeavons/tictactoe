# Make a program that uses a lookup table to convert any set of alphabets into their corresponding NATO phonetic alphabets. Also implement the inverse function. - Input: cat- Output: charlie alfa tango

# phonetic alphabet - each word has a code word, e.g. a - alpha, b - beta, etc. 


codes = {
    'a' : "Alpha",
    'b' : "Bravo",
    'c' : "Charlie",
    'd' : "Delta",
    'e' : "Echo",
    'f' : "Foxtrot",
    'g' : "Golf",
    'h' : "Hotel",
    'i' : "India",
    'j' : "Juliet",
    'k' : "Kilo",
    'l' : "Lima",
    'm' : "Mike",
    'n' : "November",
    'o' : "Oscar",
    'p' : "Papa",
    'q' : "Quebec",
    'r' : "Romeo",
    's' : "Sierra",
    't' : "Tango",
    'u' : "Uniform",
    'v' : "Victor",
    'w' : "Whisky",
    'x' : "XRay",
    'y' : "Yankee",
    'z' : "Zulu"
}
# would be a dictionary  
word = input("Type a word:")
for letter in word:
    if letter in codes:
        print(codes[letter])

