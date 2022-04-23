# Desenvolvimento de um cliente TCP
# Código: 5kUNoshHl6Y

import socket
import sys


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print('A conexão falhou!!!')
        print('Erro: {}'.format(e))
        sys.exit()

    print('Socket criado com sucesso!')

    HostAlvo = input('Informe o Host ou IP a ser conectado: ')
    PortaAlvo = input('Informe a porta a ser utilizada: ')

    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print('Cliente TCP conectado com sucesso ao Host: ' + HostAlvo + ', através da porta ' + PortaAlvo + '!')
        s.shutdown(2)
    except socket.error as e:
        print('Não foi possível conectar ao host: ' + HostAlvo + ', através da porta ' + PortaAlvo+ '!')
        print('Erro: {}'.format(e))
        sys.exit()

if __name__ == '__main__':
    main()
