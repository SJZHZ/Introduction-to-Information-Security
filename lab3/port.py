import sys
from socket import *
service_ports = {
    21: 'ftp',
    22: 'ssh',
    23: 'telnet',
    80: 'http',
    443: 'https',
    3306: 'mysql'
}
target_ip = '162.105.210.3'
opened_ports = []

for port in service_ports:
    sock = socket(AF_INET, SOCK_STREAM)
    sock.settimeout(5)
    result = sock.connect_ex((target_ip, port))
    print(port, result)
    if result == 0:
        opened_ports.append(port)
print("Opened ports:")
for i in opened_ports:
    print(f'{i} ({service_ports[i]})')