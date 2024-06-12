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

def create_server_socket(host, port):
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile="server.crt", keyfile="server.key")

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    server_socket.bind((host, port))
    server_socket.listen(5)
    secure_socket = context.wrap_socket(server_socket, server_side=True)

    return secure_socket

def handle_client_connection(client_socket):
    encrypted_data_layer2 = client_socket.recv(1024)
    decrypted_data_layer1 = decrypt(encrypted_data_layer2, key2, iv2)
    decrypted_data = decrypt(decrypted_data_layer1, key1, iv1)
    print(f"Alınan mesaj: {decrypted_data.decode('utf-8')}")
    response = encrypt(encrypt(b'Merhaba, istemci!', key1, iv1), key2, iv2)
    client_socket.sendall(response)

def main():
    host = 'localhost'
    port = 65432
    server_socket = create_server_socket(host, port)
    print(f"{host}:{port} üzerinde sunucu dinleniyor...")

    while True:
        client_socket, _ = server_socket.accept()
        handle_client_connection(client_socket)
        client_socket.close()

if __name__ == "__main__":
    main()
