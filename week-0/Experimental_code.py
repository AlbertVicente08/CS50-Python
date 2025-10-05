# Ask user for their name 
#Remove white space from str and capitalize user's name
name = input("What's your name? ").strip().title()

# Capitalize user's name, only the first word
#name = name.capitalize()

# Split user's name into first name and last name
first, last = name.split(" ")

#Say hello to user,  f-string  is a way to embed expressions inside string 
print(f"Hello, {first}")
