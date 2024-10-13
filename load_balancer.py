import socket
import threading

# List of server ports
server_ports = [9991, 9992, 9993]
current_server = 0

def handle_client(client_socket):
    global current_server
    # Get the next server port
    port = server_ports[current_server]
    current_server = (current_server + 1) % len(server_ports)

    # Connect to the selected server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect(('127.0.0.1', port))
    
    # Receive message from the client
    message = client_socket.recv(1024)
    server_socket.send(message)
    
    # Receive reply from the server
    reply = server_socket.recv(1024)
    
    # Send reply back to client
    client_socket.send(reply)
    
    # Close sockets
    server_socket.close()
    client_socket.close()

def start_load_balancer(port):
    load_balancer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    load_balancer.bind(("127.0.0.1", port))
    load_balancer.listen(100)  # Can handle 100 clients
    print(f"[*] Load balancer listening on port {port}")

    while True:
        client_socket, addr = load_balancer.accept()
        print(f"Accepted connection from {addr}")
        
        # Handle the client in a new thread
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

if __name__ == "__main__":
    start_load_balancer(9990)  # Load balancer listens on port 9990
