import socket
import ssl

def create_server_socket(host, port):
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile="server.crt", keyfile="server.key")

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    server_socket.bind((host, port))
    server_socket.listen(5)
    secure_socket = context.wrap_socket(server_socket, server_side=True)

    return secure_socket

def handle_client_connection(client_socket):
    data = client_socket.recv(1024)
    print(f"Alınan mesaj: {data.decode('utf-8')}")
    client_socket.sendall("Merhaba, istemci!".encode('utf-8'))

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
