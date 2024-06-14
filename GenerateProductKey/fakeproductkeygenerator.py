import os
import tkinter as tk
from tkinter import messagebox

# Define the filenames
certificate_file = "certificate.pem"
key_file = "key.pem"
expected_key = "8U1XU9-XSX76XU0-LOSANGRE09mI9AMin8bhhgBHGLA"

# Step 1: Check if the certificate file exists
if os.path.isfile(certificate_file):
    # Step 2: Read the content of the certificate file
    with open(certificate_file, "r") as cert_file:
        cert_content = cert_file.read().strip()  # Remove leading/trailing spaces

    # Step 3: Verify if the content matches the specified text
    expected_text = "7D1S1S1S18Utestcertificate"
    if expected_text in cert_content:
        # Step 4: Check if the key file exists
        if os.path.isfile(key_file):
            # Step 5: Read the content of the key file
            with open(key_file, "r") as key_file:
                key_content = key_file.read().strip()  # Remove leading/trailing spaces

            # Step 6: Verify if the key content matches the expected key
            if key_content == expected_key:
                print("Key is valid.")
            else:
                print("Error: Key content does not match the expected value.")
                messagebox.showerror("Error", "Application expected an error (KEY_MISMATCH_CONTEXT)")
        else:
            print("Error: Key file does not exist.")
            messagebox.showerror("Error", "Application expected an error (KEY_NOT_EXIST)")
    else:
        # Certificate content doesn't match
        print("Error: The certificate content does not match the expected text.")
        messagebox.showerror("Error", "Application expected an error (CERTIFICATE_CONTENT_MISMATCH)")
else:
    # Certificate file doesn't exist
    print("Error: The certificate file does not exist.")
    messagebox.showerror("Error", "Application expected an error (CERTIFICATE_NOT_EXISTING)")

# Generate a 25-character alphanumeric string
import random
import string

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(length))

keygen_content = generate_random_string(25)
print(f"Generated key: {keygen_content}")
print("Type Y to close app and press enter")
theansweryo = input("Answer to close app: ")
# Create a basic tkinter window

