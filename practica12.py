import socket
import threading
import requests  # Para hacer solicitudes HTTP POST
from datetime import datetime  # Para obtener fecha y hora

# Configuración del servidor
HOST = '0.0.0.0'  # Cambiado para permitir conexiones desde cualquier IP
PORT = 12345

# URL de la API de Laravel (reemplaza con la tuya)
API_URL = 'http://127.0.0.1:8000/api/mensajes/crear'  # Ejemplo: endpoint para guardar mensajes

# Lista de clientes conectados
clients = []
nicknames = []

# Función para enviar datos a la API de Laravel
def send_to_api(nombre_usuario, mensaje):
    """Envía el mensaje a la API de Laravel con POST."""
    fecha_hora = datetime.now().isoformat()  # Formato ISO 8601
    data = {
        'nombre_usuario': nombre_usuario,
        'mensaje': mensaje,
        'fecha_hora': fecha_hora
    }
    try:
        response = requests.post(API_URL, json=data)  # Envía como JSON
        if response.status_code == 200 or response.status_code == 201:
            print(f"Mensaje enviado a API: {data}")
        else:
            print(f"Error al enviar a API: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Error de conexión con API: {e}")

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
                # Enviar mensaje a la API de Laravel
                send_to_api(nickname, message)
                # Retransmitir a otros clientes
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
    print(f"Servidor de chat escuchando en {HOST}:{PORT} (acceso desde cualquier IP)")
    
    while True:
        client_socket, client_address = server_socket.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        thread.start()

if __name__ == "__main__":
    main()
