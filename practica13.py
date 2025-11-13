import socket
import threading

class ChatClient:
    def __init__(self, host='127.0.0.1', port=12345):
        self.host = host
        self.port = port
        self.client_socket = None
        self.running = False
        self.receive_callback = None  # Callback para manejar mensajes recibidos en la GUI
    
    def set_receive_callback(self, callback):
        """Establece una función de callback para manejar mensajes recibidos."""
        self.receive_callback = callback
    
    def connect(self, nickname):
        """Conecta al servidor y envía el nickname."""
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((self.host, self.port))
            self.client_socket.send(nickname.encode('utf-8'))
            self.running = True
            # Iniciar hilo para recibir mensajes
            threading.Thread(target=self.receive_messages, daemon=True).start()
            return True
        except Exception as e:
            if self.receive_callback:
                self.receive_callback(f"❌ Error al conectar: {e}")
            return False
    
    def send_message(self, message):
        """Envía un mensaje al servidor."""
        if self.client_socket and self.running:
            try:
                self.client_socket.send(message.encode('utf-8'))
                if self.receive_callback:
                    self.receive_callback(f"✅ Mensaje enviado: {message}")
            except:
                self.disconnect()
    
    def receive_messages(self):
        """Recibe mensajes del servidor en un hilo separado y los pasa al callback."""
        while self.running:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if message and self.receive_callback:
                    self.receive_callback(message)
                elif not message:
                    break
            except:
                break
        self.disconnect()
    
    def disconnect(self):
        """Desconecta del servidor."""
        self.running = False
        if self.client_socket:
            self.client_socket.close()
        if self.receive_callback:
            self.receive_callback("😢 Te has desconectado del chat. ¡Hasta luego!")
