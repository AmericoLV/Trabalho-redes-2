# Discentes: Americo Lucas Pereira Vilefort, Rafael Meira de Menezes e Livia Moreira

import socket
import threading

HOST = 'localhost'
PORTA = 9999
clientes = []

def difundir(mensagem: bytes, remetente: socket.socket):
    """Envia mensagem a todos exceto quem enviou."""
    for cliente in clientes:
        if cliente is not remetente:
            try:
                cliente.sendall(mensagem)
            except:
                pass

def tratar_cliente(cliente_socket, endereco):
    """Lê mensagens do cliente e as difunde."""
    print(f"[+] Conexão com {endereco}")
    try:
        while True:
            dados = cliente_socket.recv(1024) # recebe dados
            if not dados:
                break
            texto = dados.decode().strip() # decodifica e limpa
            if texto.lower() == 'sair': # comando de saída
                break
            print(f"[{endereco}] {texto}")
            difundir(f"[{endereco}] {texto}".encode('utf-8'), cliente_socket)
    finally:
        clientes.remove(cliente_socket) # remove da lista
        cliente_socket.close() # fecha socket
        print(f"[-] {endereco} desconectou")

def iniciar_servidor_chat():
    """Configura e inicia o servidor de chat."""
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((HOST, PORTA)) # associa IP e porta
    servidor.listen(2) # até 2 conexões
    print(f"Servidor de chat em {HOST}:{PORTA} (até 2 clientes)")

    # aceita exatamente 2 clientes
    while len(clientes) < 2:
        conexao, endereco = servidor.accept() # espera conexão
        clientes.append(conexao) # registra cliente
        print(f"[i] Cliente conectado: {endereco}")
        threading.Thread(
            target=tratar_cliente,
            args=(conexao, endereco),
            daemon=True
        ).start() # trata em thread

    print("[i] Dois clientes conectados — chat iniciado")
    threading.Event().wait() # mantém servidor ativo

# inicia o servidor
iniciar_servidor_chat()
