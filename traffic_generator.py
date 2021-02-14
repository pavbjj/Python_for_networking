#!/usr/bin/python
import random
import socket
import string
import sys


def argumenty(*args):
    if len(sys.argv) == 6:
        protocol = sys.argv[1]
        ip = sys.argv[2]
        if sys.argv[1] == "udp" or sys.argv[1] == "UDP":
            protocol = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        elif sys.argv[1] == "tcp" or sys.argv[1] == "TCP":
            protocol = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            print("Invalid protocol! Use udp or tcp")
        port = int(sys.argv[3])
        times = int(sys.argv[4])
        repetitions = int(sys.argv[5])
    else:
        print(
            "Incorrect number of arguments, run like : protocol ip port bytes count ")
        exit(1)
    return protocol, ip, port, times, repetitions


def main():
    print("Ctrl+c to exit the program!")
    protocol, ip, port, times,repetitions = argumenty()
    print(repetitions)
    for i in range(repetitions):
        protocol, ip, port, times, repetitions = argumenty()
        send_packet = ''.join(random.choice(string.ascii_lowercase) for i in range(times))
        length = len(send_packet)
        try:
            protocol.connect((ip, port))
            protocol.send(send_packet.encode('utf-8'))
            print("Successfully sent  {} packet to {} with {} bytes, on port {}".format(i + 1, ip, length, port))
        except socket.error:
            print("Error, unable to create TCP socket, does remote end listen on:TCP/{} ?".format(port))
        finally:
            protocol.close()


if __name__ == "__main__":
    print(main())
