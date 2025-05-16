# Discentes: Americo Lucas Pereira Vilefort, Rafael Meira de Menezes e Livia Moreira

import socket
import threading

HOST = 'localhost'
PORTA = 9999

def receber_loop(socket_cliente: socket.socket):
    """Recebe e imprime mensagens do servidor."""
    while True:
        dados = socket_cliente.recv(1024) # aguarda dados
        if not dados:
            break
        print(dados.decode()) # exibe mensagem

def iniciar_cliente_chat():
    """Conecta no servidor e envia mensagens."""
    socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_cliente.connect((HOST, PORTA)) # conecta ao servidor

    # inicia thread para receber mensagens
    threading.Thread(
        target=receber_loop,
        args=(socket_cliente,),
        daemon=True
    ).start()

    try:
        while True:
            texto = input().strip() # lê entrada do usuário
            socket_cliente.sendall(texto.encode())
            if texto.lower() == 'sair': # fecha se 'sair'
                break
    finally:
        socket_cliente.close() # garante fechamento

# inicia o cliente
iniciar_cliente_chat()

