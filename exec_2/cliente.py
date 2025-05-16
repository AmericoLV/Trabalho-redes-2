# Discentes: Americo Lucas Pereira Vilefort, Rafael Meira de Menezes e Livia Moreira

import socket

HOST = 'localhost'
PORTA = 9693
TAM_MAX = 64 * 1024  # 64 KB

def iniciar_cliente_udp():
    # cria socket UDP e define timeout
    socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket_cliente.settimeout(5)

    try:
        while True:
            texto = input("Digite mensagem (ou 'sair'): ").strip() # lê comando
            if texto.lower() == 'sair': # verifica saída
                break

            dados = texto.encode('utf-8') # codifica texto
            if len(dados) > TAM_MAX: # checa tamanho
                print("Erro: mensagem excede 64 KB.")
                continue

            socket_cliente.sendto(dados, (HOST, PORTA)) # envia para servidor
            try:
                eco, _ = socket_cliente.recvfrom(TAM_MAX) # espera eco
                print(f"Eco do servidor: {eco.decode('utf-8')}")
            except socket.timeout: # trata timeout
                print("Timeout: sem resposta do servidor.")
    finally:
        socket_cliente.close() # fecha socket

# inicia cliente UDP
iniciar_cliente_udp()

