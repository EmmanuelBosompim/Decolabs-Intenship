print("==========================================")
print("       PASSWORD STRENGTH CHECKER")
print("==========================================")


password = input("Enter your password: ")

has_uppercase = False
has_number = False
has_symbol = False


for character in password:

    
    if character.isupper():
        has_uppercase = True

    
    if character.isdigit():
        has_number = True

    
    if not character.isalnum():
        has_symbol = True



has_good_length = len(password) >= 8



score = 0

if has_good_length:
    score += 1

if has_uppercase:
    score += 1

if has_number:
    score += 1

if has_symbol:
    score += 1

print("\nPassword Analysis")
print("-----------------")

if has_good_length:
    print("Length (8+):       ✓")
else:
    print("Length (8+):       ✗")

if has_uppercase:
    print("Uppercase letter:  ✓")
else:
    print("Uppercase letter:  ✗")

if has_number:
    print("Number:            ✓")
else:
    print("Number:            ✗")

if has_symbol:
    print("Symbol:            ✓")
else:
    print("Symbol:            ✗")


if score <= 1:
    strength = "WEAK"
elif score <= 3:
    strength = "MEDIUM"
else:
    strength = "STRONG"


print("\n------------------------------------------")
print("Password Strength:", strength)
print("Score:", score, "/ 4")
print("------------------------------------------")

print("\nThank you for using the Password Strength Checker!")