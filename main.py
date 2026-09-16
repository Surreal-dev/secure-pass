import random

print("Welcome to the Secure Password Generator!")

while True:
    try:
        passlen = int(input("Desired password length? (min 8): "))
        break
    except ValueError:
        print("Please enter a valid number.")

if passlen < 8:
    passlen = 8
    print("Length was too small. Defaulted to 8 characters.")

use_upper = input("Include uppercase letters? (Y/N): ").upper() == "Y"
use_lower = input("Include lowercase letters? (Y/N): ").upper() == "Y"
use_digits = input("Include digits? (Y/N): ").upper() == "Y"
use_special = input("Include special characters? (Y/N): ").upper() == "Y"

if not (use_upper or use_lower or use_digits or use_special):
    print("No character types selected. Defaulting to lowercase letters.")
    use_lower = True

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
special = "!@#$%&*()_-;:,.~"

combined = ""
required_chars = []

if use_upper:
    combined += upper
    required_chars.append(random.choice(upper))
if use_lower:
    combined += lower
    required_chars.append(random.choice(lower))
if use_digits:
    combined += digits
    required_chars.append(random.choice(digits))
if use_special:
    combined += special
    required_chars.append(random.choice(special))

remaining = passlen - len(required_chars)
password_chars = required_chars + [random.choice(combined) for _ in range(remaining)]
random.shuffle(password_chars)
password = "".join(password_chars)

print("Your generated password:", password)