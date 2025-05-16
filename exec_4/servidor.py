# Discentes: Americo Lucas Pereira Vilefort, Rafael Meira de Menezes e Livia Moreira
import socket
import threading
import datetime
import logging

HOST = '127.0.0.1'
PORTA = 9197

# registra solicitações em arquivo
logging.basicConfig(
    filename='log_info.log',
    level=logging.INFO,
    format='%(asctime)s %(message)s'
)

def tratar_requisicao(cliente_socket, endereco):
    print(f"Conectado com {endereco}")
    try:
        while True:
            req = cliente_socket.recv(1024).decode().strip() # lê comando
            if not req:
                continue
            logging.info(f"Requisição de {endereco}: {req}")
            if req.lower() == 'h':
                agora = datetime.datetime.now().strftime('%H:%M:%S') # formata hora
                cliente_socket.sendall(agora.encode('utf-8'))
                logging.info(f"Enviado hora {agora} para {endereco}")
            elif req.lower() == 'stop':
                break # encerra conexão
            else:
                texto = "comando inválido. use 'h' ou 'stop'."
                cliente_socket.sendall(texto.encode('utf-8'))
    except Exception as e:
        logging.error(f"Erro com {endereco}: {e}")
    finally:
        cliente_socket.close() # garante fechamento
        print(f"{endereco} desconectou")

def iniciar_servidor_hora():
    socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_servidor.bind((HOST, PORTA)) # associa endereço e porta
    socket_servidor.listen() # aguarda conexões
    print(f"Servidor de hora em {HOST}:{PORTA}")

    while True:
        cliente_sock, endereco = socket_servidor.accept() # aceita cliente
        threading.Thread(
            target=tratar_requisicao,
            args=(cliente_sock, endereco),
            daemon=True
        ).start() # atende em thread

# inicia servidor
iniciar_servidor_hora()



