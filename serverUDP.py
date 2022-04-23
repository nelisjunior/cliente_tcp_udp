# Desenvolvimento de um Server
# Ipv4 UDP Server
# Código: UeCcfdaYXM4

import socket

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket criado sucesso!\n')

host = "127.0.0.1"  # Endereço IP do servidor
port = 5000  # Porta usada pelo servidor

udp.bind((host, port))  # faz ligação entre cliente/servidor através da porta!
msg = '\nServidor: E ai, Cliente. Tranquilo!?'

while 1:
    dados, end = udp.recvfrom(4096)

    if dados:
        print('Servidor enviando mensagem...\n')
        udp.sendto(dados + (msg.encode()), end)
