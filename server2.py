import socket
import threading
import logging
import sys

# Setup logging to record connection times and messages
logging.basicConfig(filename="server_log.txt", level=logging.INFO, format="%(asctime)s - %(message)s")

def handle_client(client_socket, address, port):
    logging.info(f"New connection from {address} on server port {port}")
    
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            
            logging.info(f"Message received from {address}: {message}")
            reply = f"Server {port} received: {message}"
            client_socket.send(reply.encode('utf-8'))
            logging.info(f"Reply sent to {address}")

        except ConnectionResetError:
            logging.info(f"Connection with {address} was closed.")
            break

    client_socket.close()
    logging.info(f"Connection closed with {address}")

def start_server(port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", port))
    server.listen(5)
    print(f"[*] Server listening on port {port}")

    while True:
        client_socket, addr = server.accept()
        logging.info(f"Accepted connection from {addr} on port {port}")

        # Start a new thread to handle client
        client_handler = threading.Thread(target=handle_client, args=(client_socket, addr, port))
        client_handler.start()

if __name__ == "__main__":
    # Get the port number from command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python server.py <port>")
        sys.exit(1)
    
    port = int(sys.argv[1])
    if port not in [9991, 9992, 9993]:
        print("Invalid port. Choose from 9991, 9992, or 9993.")
        sys.exit(1)
    
    start_server(port)
