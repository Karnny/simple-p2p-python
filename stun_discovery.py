
import stun

def discover_public_ip_port():
    # Choose a STUN server (using Google's as an example)
    stun_server = 'stun.l.google.com'
    stun_port = 19302

    # Discover public IP and port using STUN
    nat_type, external_ip, external_port = stun.get_ip_info(stun_host=stun_server, stun_port=stun_port)
    print(f"NAT Type: {nat_type}, External IP: {external_ip}, External Port: {external_port}")
    return external_ip, external_port

if __name__ == "__main__":
    discover_public_ip_port()
