import random
# This program generates a list of names and randomly chooses one name from the list

# Input: A list containing string of names.
# Output: A random name from from the list.

# Psuedocode
# Ask for user input of names (Stored as a long list).
# Split the names and store each one in a unique index of the list.
# Generate a random number between 0 and last index. 
# Print out result. 

names_string = input("Give me everybody's names, separated by a comma and a space. ")
names = names_string.split(", ")
random_number = random.randint(0, len(names)-1)
print(f"{names[random_number]} is going to buy the meal today!")
