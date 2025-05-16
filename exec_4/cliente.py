# Discentes: Americo Lucas Pereira Vilefort, Rafael Meira de Menezes e Livia Moreira
import socket

HOST = '127.0.0.1'
PORTA = 9197

def iniciar_cliente_hora():
    # cria socket TCP e conecta ao servidor
    socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_cliente.connect((HOST, PORTA))
    print("Use 'h' para hora, 'stop' para sair.")

    try:
        while True:
            cmd = input().strip() # lê comando do usuário
            socket_cliente.sendall(cmd.encode())
            if cmd.lower() == 'stop': # encerra se receber 'stop'
                break
            resposta = socket_cliente.recv(1024).decode() # recebe resposta
            print(f"Servidor: {resposta}")
    finally:
        socket_cliente.close() # garante fechamento do socket

# executa a função principal
iniciar_cliente_hora()


