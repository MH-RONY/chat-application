import socket
import threading

#server ip and port 
SERVER = "192.168.0.102"
PORT = 6060
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

client_list=[]

def client_handle(client, addr):
    print(f"{addr} is Connected")
    client.send("Wellcome to our server".encode())
    while True:
        try:
            message = client.recv(1024).decode()
            if message == "exit":
                break
            send(client, message)
        except:
            client.close()
            remove_client(client)

    client.close()
    remove_client(client)

def send(obj, message):
    for client in client_list:
        if client != obj:
            try:
                client.send(message.encode())
            except:
                client.close()
                remove_client(client)

def remove_client(client):
    if client in client_list:
        client_list.remove(client)

def start():
    server.listen(100)
    while True:
        client, addr = server.accept()
        client_list.append(client)
        thread = threading.Thread(target=client_handle, args=(client, addr))
        thread.start()
        count = threading.active_count()-1
        print(f"Connected Client: {count}")

print("Chat Server is running...")
start()


