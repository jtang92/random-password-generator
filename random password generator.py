import random
import string

def generate_password(length):
    if length < 6:
        print("Password length should be at least 6 characters for security reasons.")
        return None

    # Define the characters to choose from
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation
    
    # Ensure the password is diverse by including at least one of each character type
    password = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(symbols)
    ]
    
    # Fill the rest of the password length with a mix of all character types
    all_characters = uppercase_letters + lowercase_letters + digits + symbols
    password += random.choices(all_characters, k=length-4)
    
    # Shuffle the resulting password list to avoid predictable patterns
    random.shuffle(password)
    
    # Convert the list of characters into a string
    return ''.join(password)

# Ask user for the desired password length
user_length = int(input("Enter the desired password length (minimum 6 characters): "))

# Generate and display the password
password = generate_password(user_length)
if password:
    print("Generated Password:", password)
