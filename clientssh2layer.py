import socket
import ssl
from OpenSSL import crypto
import base64

# Çift katmanlı şifreleme için anahtarlar ve IV'ler
key1 = b'ilk_katman_anahtar'
iv1 = b'ilk_katman_iv'
key2 = b'ikinci_katman_anahtar'
iv2 = b'ikinci_katman_iv'

def encrypt(data, key, iv):
    cipher = crypto.Cipher('aes-256-cbc', key, iv, 1)
    encrypted_data = cipher.update(data) + cipher.final()
    return base64.b64encode(encrypted_data)

def decrypt(encrypted_data, key, iv):
    encrypted_data = base64.b64decode(encrypted_data)
    cipher = crypto.Cipher('aes-256-cbc', key, iv, 0)
    decrypted_data = cipher.update(encrypted_data) + cipher.final()
    return decrypted_data

def create_client_socket(host, port):
    context = ssl.create_default_context()
    secure_socket = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=host)
    secure_socket.connect((host, port))
    return secure_socket

def main():
    host = 'localhost'
    port = 65432
    secure_socket = create_client_socket(host, port)

    message = encrypt(encrypt(b'Merhaba, sunucu!', key1, iv1), key2, iv2)
    secure_socket.sendall(message)
    encrypted_response_layer2 = secure_socket.recv(1024)
    decrypted_response_layer1 = decrypt(encrypted_response_layer2, key2, iv2)
    decrypted_response = decrypt(decrypted_response_layer1, key1, iv1)
    print(f"Sunucudan alınan mesaj: {decrypted_response.decode('utf-8')}")

    secure_socket.close()

if __name__ == "__main__":
    main()
