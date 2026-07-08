import random

title = "Password Generator"
print("-" * 30)
print(title.center(30))
print("-" * 30)

# Ask the user how many characters the password should have
password_len = int(input("How many characters do you want your password to have  ? " + "\n"))


characters = "abcdefghijklmnopqrstuvwxyz0123456789"
password = ""
for i in range(password_len):
    password += random.choice(characters)

print("Your new password is:",password)    