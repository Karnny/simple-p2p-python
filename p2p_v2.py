# p2p_connection.py
import socket
import threading
from stun_discovery import discover_public_ip_port

ext_ip, ext_port = discover_public_ip_port()
print(f"My IP: {ext_ip}, My port: {ext_port}")

# Ask for the peer's IP and port
peer_ip = input("Enter the peer's IP address: ")
peer_port = int(input("Enter the peer's port: "))

# Define separate ports for sending and receiving
receive_port = 42424  # Port for listening on this device
send_port = 42425     # Port to send from on this device

def receive_messages():
    print("Start listening for messages...")
    recv_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    recv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    recv_sock.bind(('0.0.0.0', receive_port))
    
    while True:
        data, addr = recv_sock.recvfrom(1024)
        print(f"Received from {addr}: {data.decode()}")

def main():
    # Start the receiving thread
    recv_thread = threading.Thread(target=receive_messages, daemon=True)
    recv_thread.start()

    send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    send_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    send_sock.bind(('0.0.0.0', send_port))  # Bind to a local port for sending

    while True:
        message = input("Enter message to send: ")
        send_sock.sendto(message.encode(), (peer_ip, peer_port))

if __name__ == "__main__":
    main()
