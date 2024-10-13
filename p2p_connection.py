# p2p_connection.py
import socket
import threading
import time
from stun_discovery import discover_public_ip_port

ext_ip, ext_port = discover_public_ip_port()
print(f"My IP: {ext_ip}, My port: {ext_port}")

# Ask for the peer's IP and port
peer_ip = input("Enter the peer's IP address: ")
peer_port = int(input("Enter the peer's port: "))

talking_port = 12344

def receive_messages():
    print(f"Start listening..")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Enable address reuse
    sock.bind(('', peer_port))
    
    while True:
        data, addr = sock.recvfrom(1024)
        print(f"Peer {addr}: {data.decode()}")

def main():
    print('Start punching hole..')
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # sock.bind(('0.0.0.0', peer_port))
    sock.sendto(b'0', (peer_ip, talking_port))
    
    # Start the receiving thread
    recv_thread = threading.Thread(target=receive_messages, daemon=True)
    recv_thread.start()
    
    sock.close()
    # time.sleep(5)
    sock = None
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # sock.bind(('0.0.0.0', talking_port))
    
    while True:
        message = input("Enter message to send: ")
        sock.sendto(message.encode(), (peer_ip, peer_port))

if __name__ == "__main__":
    main()
