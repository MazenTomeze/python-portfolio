#port_facts.py
# Reference 1: RFC 9293 - TCP Source and Destination Ports are 16 bits each.
# Reference 2: RFC 791 - IPv4 Addresses are fixed length of four octets (32 bits).
PORT_BITS = 16
IPV4_BITS = 32
total_ports = (2 ** PORT_BITS)
highest_port = (2 ** PORT_BITS) - 1
total_ipv4_addresses = (2 ** IPV4_BITS)
print (f"Total ports: {total_ports}")
print (f"Highest port: {highest_port}")
print (f"Total IPv4 addresses: {total_ipv4_addresses}")