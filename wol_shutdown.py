import socket
import os
def listen_for_wol_packets():
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Bind to the default WOL port (usually 9 or 7)
    sock.bind(('', 9))

    print("Listening for WOL packets...")
    while True:
        # Receive packet
        data, addr = sock.recvfrom(1024)

        # Check if the packet matches the magic packet format
        if len(data) >= 102 and data[:6] == b'\xff' * 6:
            print(f"Magic Packet received from {addr}")
            # Trigger your desired action here
            shutdown_system()

def shutdown_system():
    print("Shutting down the system...")
    # Execute the shutdown command
    os.system('shutdown now')

if __name__ == '__main__':
    listen_for_wol_packets()
