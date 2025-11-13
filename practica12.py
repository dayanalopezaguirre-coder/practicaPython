import socket
import threading

# Configuración del servidor
HOST = '127.0.0.1'
PORT = 12345

# Lista de clientes conectados
clients = []
nicknames = []

# Función para manejar mensajes de un cliente
def handle_client(client_socket, client_address):
    try:
        # Recibir nickname
        nickname = client_socket.recv(1024).decode('utf-8')
        if not nickname:
            return
        nicknames.append(nickname)
        clients.append(client_socket)
        
        print(f"{nickname} se ha conectado desde {client_address}")
        broadcast(f"😀 {nickname} se ha unido al chat! ¡Bienvenido!", client_socket)
        
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                broadcast(f"{nickname}: {message}", client_socket)
            else:
                break
    except Exception as e:
        print(f"Error con cliente: {e}")
    finally:
        # Remover cliente desconectado
        if client_socket in clients:
            index = clients.index(client_socket)
            clients.remove(client_socket)
            nickname = nicknames[index]
            nicknames.remove(nickname)
            client_socket.close()
            broadcast(f"😢 {nickname} ha salido del chat. ¡Hasta luego!", None)
            print(f"{nickname} se ha desconectado.")

# Función para retransmitir mensajes a todos los clientes
def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                client.close()
                if client in clients:
                    clients.remove(client)

# Función principal del servidor
def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"Servidor de chat escuchando en {HOST}:{PORT}")
    
    while True:
        client_socket, client_address = server_socket.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        thread.start()

if __name__ == "__main__":
    main()