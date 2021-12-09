# Author: Omkar

# Public Private Key cryptography



# Generate key
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
public_key = private_key.public_key()

print(public_key)

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def encrypt(public_key,message):
    byte_message=str.encode(message)
    encrypted_message = public_key.encrypt(
        byte_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return encrypted_message

def decrypt(private_key,encrypted_message):
    bytes_decrypted_message = private_key.decrypt(
        encrypted_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    str_decrypted_message = bytes_decrypted_message.decode()
    return str_decrypted_message

message='Hello There'
print(message)

encrypted_message=encrypt(public_key,message)
print("Encrypted: ",encrypted_message)

decrypted_message=decrypt(private_key,encrypted_message)

print("Decrypted: ",decrypted_message)
