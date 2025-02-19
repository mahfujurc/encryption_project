import os
from cryptography.fernet import Fernet

# Function to generate and save encryption key
def generate_key():
    key = Fernet.generate_key()
    with open('secret.key', 'wb') as key_file:
        key_file.write(key)

# Function to encrypt files in a folder
def encrypt_folder(folder_path):
    # Generate and save key if it doesn't exist
    if not os.path.exists('secret.key'):
        generate_key()

    with open('secret.key', 'rb') as key_file:
        key = key_file.read()
    cipher = Fernet(key)

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            with open(file_path, 'rb') as file:
                file_data = file.read()

            encrypted_data = cipher.encrypt(file_data)

            with open(file_path + '.enc', 'wb') as encrypted_file:
                encrypted_file.write(encrypted_data)

            # Optionally, remove the original file
            os.remove(file_path)
    print(f'Files in "{folder_path}" have been encrypted.')

if __name__ == "__main__":
    folder_path = input("Enter the path of the folder to encrypt (e.g., M:\\yeasmisorna): ")
    encrypt_folder(folder_path)
