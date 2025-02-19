import os
from cryptography.fernet import Fernet

# Function to decrypt files in a folder
def decrypt_folder(folder_path):
    with open('secret.key', 'rb') as key_file:
        key = key_file.read()

    cipher = Fernet(key)

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if filename.endswith('.enc'):
            with open(file_path, 'rb') as encrypted_file:
                encrypted_data = encrypted_file.read()

            decrypted_data = cipher.decrypt(encrypted_data)

            # Save the decrypted file without the .enc extension
            with open(file_path[:-4], 'wb') as decrypted_file:
                decrypted_file.write(decrypted_data)

            # Optionally, remove the encrypted file
            os.remove(file_path)
    print(f'Files in "{folder_path}" have been decrypted.')

if __name__ == "__main__":
    folder_path = input("Enter the path of the folder to decrypt (e.g., M:\\yeasmisorna): ")
    decrypt_folder(folder_path)
