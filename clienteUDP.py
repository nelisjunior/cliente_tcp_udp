# Desenvolvimento de um cliente UDP
# IPV4 UDP
# Código: A4QMR-H8XJs

import socket

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Socket criado com sucesso!\n')

host = "127.0.0.1"
port = 5000
msg = 'E ae, man, de boas?!\n'

try:
    print('Cliente: ' + msg)
    udp.sendto(msg.encode(), (host, port))

    dados, servidor = udp.recvfrom(4096)
    dados = dados.decode()
    print('Cliente: ' + dados)
finally:
    print('Cliente: fechando a conexão\n')
    udp.close()
