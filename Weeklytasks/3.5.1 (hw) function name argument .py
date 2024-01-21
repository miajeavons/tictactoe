# Task 1: Make a function that takes two arguments (given name and family name), the second of which is optional. Print a greeting according to which arguments are provided.Example output: “Hello Kenneth.” or “Hello there, Kenneth of Lim!”

def greet(name,famname=True):
    greetings = "Hello, " + name
    if famname:
        greetings += " Jeavons."
    return greetings 
print(greet("Mia",False))