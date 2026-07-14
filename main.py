import random
# Program to generate a random password based on user input
def presentation():
    title = "Password Generator"
    print("-" * 30)
    print(title.center(30))
    print("-" * 30)
presentation()

# Ask the user how many characters the password should have and check if the input is a valid number
while True:

    try:     
        password_len = input("How many characters do you want your password to have  ? " + "\n")
        password_len = int(password_len)
        break
    except ValueError:
        print("Please enter a valid number")
 
 
 
# Define the characters that can be used in the password
characters =  "abcdefghijklmnopqrstuvwxyz"

# Check if the user wants to include numbers
include_numbers = input("Do you want to include numbers ? (y/n)\n").lower()
if include_numbers == "y":
 characters += "0123456789"


# Check if the user wants to include uppercase letters
include_uppercase = input("Do you want to include uppercase letters ? (y/n)\n").lower()
if include_uppercase == 'y':
    characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
# Check if the user wants to include special characters
include_special = input("Do you want to include special characters ? (y/n)\n")
if include_special == 'y':
    characters += "!@#$%^&*()-+"
    
# Generate the password
def generate_password(length, characters):
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    return password    

password = generate_password(password_len, characters)
print("Your new password is:", password)    