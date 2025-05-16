# Discentes: Americo Lucas Pereira Vilefort, Rafael Meira de Menezes e Livia Moreira

import socket

HOST = 'localhost'
PORTA = 9693
TAM_MAX = 64 * 1024  # 64 KB

def iniciar_servidor_udp():
    # cria socket UDP
    socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # associa IP e porta
    socket_servidor.bind((HOST, PORTA))
    print(f"Servidor UDP aguardando em {HOST}:{PORTA}...")

    while True:
        # recebe dados do cliente
        dados, endereco = socket_servidor.recvfrom(TAM_MAX)
        texto = dados.decode('utf-8').strip()  # decodifica e limpa
        print(f"Mensagem de {endereco}: {texto}")
        # envia eco de volta
        socket_servidor.sendto(dados, endereco)

# inicia o servidor
iniciar_servidor_udp()

