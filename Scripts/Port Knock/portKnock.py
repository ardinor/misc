#!/usr/bin/python3
import argparse
import socket


def knock(host, port):

    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.setblocking(0)
    try:
        conn.connect((host, port))
    except socket.error:
        print('Knocked on {} {}'.format(host, port))

        
def knock_range(host, ports):

    for port in ports:
        knock(host, port)
        
        
if __name__ == '__main__':

    arg_parser = argparse.ArgumentParser(description='Simple Port Knocker.')
    arg_parser.add_argument('Host', help='The host you wish to knock on')
    arg_parser.add_argument('Ports', nargs='*', type=int, help='List of ports to knock on')
    args = arg_parser.parse_args()
    host = args.Host
    ports = args.Ports
    if ports:
        knock_range(host, ports)
    else:
        print('No ports listed, try listing some ports to knock on')
    