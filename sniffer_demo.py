import socket
import struct
import textwrap

#looping and listening for packets and we'll take the info
def main():
    conn = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
 #raw data is what's being passed into ethernet frame
    while True:
        raw_data, addr = conn.recvfrom(65536)
        dest_mac, src_mac, eth_proto, data = ethernet_frame(raw_data)
        print('\nEthernet Frame: ')
        print('Destination: {}, Source: {}, Protocol: {}'.format(dest_mac, src_mac, eth_proto))





#unpack ethernet frame
def ethernet_frame(data):
    dest_mac, src_mac, proto = struct.unpack(' ! 6s 6s H', data[:14])
    return get_mac_addr(dest_mac), get_mac_addr(src_mac), socket.htons(proto), data[:14]
    #change to human readable MA, big or little endian and make bytes compatible

#return properly formatted mac address (ie AA:BB:CC:DD:EE:FF)
def get_mac_addr(bytes_addr):
    #pass a function and an iterable and it runs each item through the function
    bytes_str = map('{:02x}'.format, bytes_addr) # 2 decimal places for each one
    mac_addr = ':'.join(bytes_str).upper()

main()