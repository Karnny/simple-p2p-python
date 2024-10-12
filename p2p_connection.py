# p2p_connection.py
import socket
import threading

# Ask for the peer's IP and port
peer_ip = input("Enter the peer's IP address: ")
peer_port = int(input("Enter the peer's port: "))

# The local port for listening and sending
local_port = 12345

def receive_messages(sock):
    while True:
        data, addr = sock.recvfrom(1024)
        print(f"Received message from {addr}: {data.decode()}")

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', local_port))
    
    # Start the receiving thread
    recv_thread = threading.Thread(target=receive_messages, args=(sock,))
    recv_thread.daemon = True
    recv_thread.start()
    
    # Send an initial message to start the connection
    print(f"Sending message to {peer_ip}:{peer_port}")
    sock.sendto(b"Hello from this device!", (peer_ip, peer_port))
    
    while True:
        message = input("Enter message to send: ")
        sock.sendto(message.encode(), (peer_ip, peer_port))

if __name__ == "__main__":
    main()
