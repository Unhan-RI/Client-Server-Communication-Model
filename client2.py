import socket
import threading
import time
import sys

def client_thread(client_id):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 9990))  # Connect to load balancer
    
    message = f"Hello from client {client_id}!"
    message_size = len(message.encode('utf-8'))  # Calculate the size of the message in bytes

    # Start timing for latency and response time
    start_time = time.time()

    # Send the message
    client.send(message.encode('utf-8'))

    # Receive the reply
    reply = client.recv(1024).decode('utf-8')
    reply_size = len(reply.encode('utf-8'))  # Calculate the size of the reply in bytes

    # End timing
    end_time = time.time()

    # Calculate latency and response time
    latency = (end_time - start_time) / 2  # Round-trip divided by 2 for one-way latency
    response_time = end_time - start_time  # Total response time

    # Throughput calculation: total data size divided by response time
    total_data = message_size + reply_size  # Sum of message and reply sizes
    throughput = total_data / response_time  # Bytes per second

    # Print results
    print(f"Client {client_id} received: {reply}")
    print(f"Latency: {latency:.6f} seconds")
    print(f"Response Time: {response_time:.6f} seconds")
    print(f"Throughput: {throughput:.2f} bytes/second")

    client.close()

def start_clients(num_clients):
    threads = []
    for i in range(num_clients):
        thread = threading.Thread(target=client_thread, args=(i+1,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    # Get the number of clients from command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python client.py <num_clients>")
        sys.exit(1)
    
    num_clients = int(sys.argv[1])
    start_clients(num_clients)
