"Chat Room Connection Client to Client"
import threading
import socket

host = '127.0.0.1'
port = 59000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
clients = []
aliases = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle_client(client):
    while True:
        try:
           message = client.recv(1024)
           broadcast(message)
        except:
            index = clients.index(clients)
            clients.remove(client)
            client.close()
            alias = aliases[index]
            broadcast(f"{alias} has left the chat room!".encode('utf-8'))
            aliases.remove(alias)
            break

def receive():
    while True:
     print("Waiting for connection...")
     client, address = server.accept()
     print("Connection established!")
     client.send('alias?'.encode('utf-8'))
     alias = client.recv(1024).decode('utf-8')
     aliases.append(alias)
     clients.append(client)
     print(f'The alias of the client is {alias}'.encode('utf-8'))
     broadcast(f"{alias} has joined the room".encode('utf-8'))
     client.send('\nYou have now joined the room'.encode('utf-8'))
     thread = threading.Thread(target=handle_client, args=(client,))
     thread.start()

if __name__ == "__main__":
  receive()