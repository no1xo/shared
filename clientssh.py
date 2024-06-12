import socket
import ssl

def create_client_socket(host, port):
    context = ssl.create_default_context()
    secure_socket = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=host)
    secure_socket.connect((host, port))
    return secure_socket

def main():
    host = 'localhost'
    port = 65432
    secure_socket = create_client_socket(host, port)

    secure_socket.sendall("Merhaba, sunucu!".encode('utf-8'))
    print(f"Sunucudan alınan mesaj: {secure_socket.recv(1024).decode('utf-8')}")

    secure_socket.close()

if __name__ == "__main__":
    main()
