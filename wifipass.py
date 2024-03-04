
import random
import string

def crack_password(password):  # Corrected function name and parameter name
    attempts = 0  # Corrected variable name
    while True:
        guess = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(len(password)))  # Corrected syntax
        attempts += 1  # Corrected variable name
        if guess == password:
            return attempts

password = input("Enter the password to crack: ")
print("Cracking password...")

attempts = crack_password(password)  # Corrected function call

print(f"The password was cracked in {attempts} attempts.")  # Corrected typo in print statement

