#!/usr/bin/python
import socket
import sys

"""Traffic generator, it generates simple udp or tcp stream"""

def arguments(*args):
    if len(sys.argv) == 4:
        protocol = sys.argv[1]
        ip = sys.argv[2]
        if sys.argv[1] == "udp" or sys.argv[1] == "UDP":
            protocol = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        elif sys.argv[1] == "tcp" or sys.argv[1] == "TCP":
            protocol = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            print("Invalid protocol! Use udp or tcp")
        port = int(sys.argv[3])
    else:
        print(
            "Incorrect number of arguments, run like : protocol ip port ")
        exit(1)
    return protocol, ip, port


def main():
    print("Ctrl+c to exit the program!")
    for i in range(10):
        protocol, ip, port = argumenty()
        send_packet = "Testing data"
        length = len(send_packet)
        try:
            protocol.connect((ip, port))
            protocol.send(send_packet.encode('utf-8'))
            print("Successfully sent {} packet to {} with {} bytes, on port {}".format(i + 1, ip, length, port))
        except socket.error:
            print("Error, unable to create TCP socket, does remote end listen on:TCP/{} ?".format(port))
        finally:
            protocol.close()


if __name__ == "__main__":
    print(main())
