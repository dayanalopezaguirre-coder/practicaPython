import tkinter as tk
from tkinter import scrolledtext, messagebox
from practica13 import ChatClient

class ChatGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat 😀")
        self.root.geometry("500x400")
        self.root.configure(bg="#E0F7FA")  # Fondo azul claro
        
        # Instancia del cliente
        self.client = ChatClient()
        self.client.set_receive_callback(self.display_message)
        
        # Área de mensajes
        self.message_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', bg="#FFFFFF", fg="#000000", font=("Arial", 10))
        self.message_area.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        # Campo de entrada
        self.entry = tk.Entry(root, font=("Arial", 12), bg="#FFFFFF")
        self.entry.pack(side=tk.LEFT, padx=10, pady=5, fill=tk.X, expand=True)
        self.entry.bind("<Return>", self.send_message)  # Enviar con Enter
        
        # Botón de enviar
        self.send_button = tk.Button(root, text="Enviar 📤", command=self.send_message, bg="#4CAF50", fg="#FFFFFF", font=("Arial", 10, "bold"))
        self.send_button.pack(side=tk.RIGHT, padx=10, pady=5)
        
        # Conectar al iniciar
        self.connect_to_chat()
    
    def connect_to_chat(self):
        """Solicita nickname y conecta."""
        nickname = tk.simpledialog.askstring("Nickname", "Ingresa tu nickname:")
        if nickname and self.client.connect(nickname):
            self.display_message("🎉 ¡Bienvenido al chat amigable! Escribe un mensaje y presiona Enviar o Enter.")
        else:
            messagebox.showerror("Error", "No se pudo conectar al servidor.")
            self.root.quit()
    
    def send_message(self, event=None):
        """Envía el mensaje."""
        message = self.entry.get().strip()
        if message:
            self.client.send_message(message)
            self.entry.delete(0, tk.END)
    
    def display_message(self, message):
        """Muestra mensajes en el área de texto."""
        self.message_area.config(state='normal')
        self.message_area.insert(tk.END, message + "\n")
        self.message_area.config(state='disabled')
        self.message_area.see(tk.END)  # Scroll automático

def main():
    root = tk.Tk()
    app = ChatGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()