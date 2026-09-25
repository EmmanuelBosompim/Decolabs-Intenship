print("========================================")
print("      BASIC ENCRYPTION & DECRYPTION")
print("========================================")

text = input("Enter the text you want to encrypt: ")

shift = int(input("Enter the shift key (1-25): "))
shift = shift % 26

encrypted_text = ""

for character in text:
    if character.isupper():
        encrypted_text += chr((ord(character) - ord('A') + shift) % 26 + ord('A'))
    elif character.islower():
        encrypted_text += chr((ord(character) - ord('a') + shift) % 26 + ord('a'))
    else:
        encrypted_text += character

decrypted_text = ""

for character in encrypted_text:
    if character.isupper():
        decrypted_text += chr((ord(character) - ord('A') - shift) % 26 + ord('A'))
    elif character.islower():
        decrypted_text += chr((ord(character) - ord('a') - shift) % 26 + ord('a'))
    else:
        decrypted_text += character

print("\n========================================")
print("                RESULTS")
print("========================================")

print("Original Text:  ", text)
print("Encrypted Text: ", encrypted_text)
print("Decrypted Text: ", decrypted_text)

print("========================================")
print("          Encryption completed!")
print("========================================")
