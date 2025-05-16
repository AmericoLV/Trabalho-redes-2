# Discentes: Americo Lucas Pereira Vilefort, Rafael Meira de Menezes e Livia Moreira


import socket

HOST = '127.0.0.1'
PORTA = 9898

def iniciar_cliente_tcp():
    # cria socket TCP e conecta ao servidor
    socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_cliente.connect((HOST, PORTA))

    mensagem = "Mensagem enviada com sucesso!"
    if not mensagem.strip(): # valida mensagem vazia
        print("Não envie mensagem vazia.")
        socket_cliente.close()
        return

    socket_cliente.send(mensagem.encode()) # envia mensagem
    resposta = socket_cliente.recv(1024).decode().strip() # recebe confirmação
    print(f"Servidor respondeu: {resposta}")

    socket_cliente.close() # fecha conexão

# inicia o cliente
iniciar_cliente_tcp()

