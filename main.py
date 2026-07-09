import random

title = "Password Generator"
print("-" * 30)
print(title.center(30))
print("-" * 30)

# Ask the user how many characters the password should have
password_len = int(input("How many characters do you want your password to have  ? " + "\n"))

characters =  "abcdefghijklmnopqrstuvwxyz"
# Check if the user wants to include numbers
include_numbers = input("Do you want to include numbers ? (y/n)\n")

if include_numbers == 'y':
     characters += "0123456789"
    
# Check if the user wants to include uppercase letters
include_uppercase = input("Do you want to include uppercase letters ? (y/n)\n")    

if include_uppercase == 'y':
    characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
password = ""
for i in range(password_len):
    password += random.choice(characters)

print("Your new password is:",password)    