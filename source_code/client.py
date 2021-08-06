import socket
import threading

SERVER = "192.168.0.102"
PORT = 6060
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect(ADDR)
    connected = True
except:
    print(">> client couldn't connected")
    connected = False

# message_list =["Hi. Whatsup. I am Client-1", "How are you client-2", "I am also fine"]

def send():
    while connected:
        message = input("Enter Something: ").encode()
        try:
            client.send(message)
        except:
            print(f"[Error..] {message} doesn't send.")

def receive():
    print("Receiveing Thread Started...")
    while connected:
        try:
            receive = client.recv(1024).decode()
            print(">> ",receive)
        except:
            pass
        
thread = threading.Thread(target=receive, args=())
thread.start()
send()
