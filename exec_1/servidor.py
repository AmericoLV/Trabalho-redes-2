# Discentes: Americo Lucas Pereira Vilefort, Rafael Meira de Menezes e Livia Moreira

import socket
import threading

HOST = '127.0.0.1'
PORTA = 9898

def tratar_cliente(conexao, endereco):
    """Processa uma conexão: recebe e confirma mensagem."""
    try:
        with conexao:
            mensagem = conexao.recv(1024).decode().strip() # lê dados
            if not mensagem:
                conexao.sendall(b"Erro: mensagem vazia\n") # validação
                return
            print(f"mensagem recebida de {endereco}: {mensagem}")
            conexao.sendall(b"Mensagem recebida\n") # confirmação
    except Exception as e:
        print(f"[!] Erro com {endereco}: {e}") # erro genérico

def iniciar_servidor_tcp():
    socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_servidor.bind((HOST, PORTA)) # associa IP e porta
    socket_servidor.listen(5) # fila de conexões
    print(f"servidor TCP ouvindo em {HOST}:{PORTA}...")

    while True:
        conexao, endereco = socket_servidor.accept() # aceita cliente
        threading.Thread(
            target=tratar_cliente,
            args=(conexao, endereco),
            daemon=True
        ).start() # atende em thread

# inicia o servidor
iniciar_servidor_tcp()

