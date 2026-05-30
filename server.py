import socket
import threading
import random
import pickle
from dotenv import load_dotenv
import os

load_dotenv()

fundo = 100.0
lock  = threading.Lock()  # !

HOST = '0.0.0.0'
PORT = int(os.getenv("PORT"))


def call_client(conn, addr):
    global fundo
    print(f"[+] Cliente conectado: {addr}")
    sorteado = random.randint(0, 999)

    try:
        dados = b""
        while True:
            parte = conn.recv(4096)
            if not parte:
                break
            dados += parte
            try:
                pedido = pickle.loads(dados)
                break          # conseguiu desserializar: objeto completo
            except Exception:
                continue

        nome   = pedido["nome"]
        aposta = pedido["aposta"]

        print(f"{nome} apostou {aposta}, sorteado {sorteado}")

# ── Utilizando o lock para evitar Race Condition ───────────────────────────────
        with lock:
            fundo += 10.0
            if aposta == sorteado:
                if fundo == 0:
                    mensagem = f"Você acertou, {nome}, mas o cofre já foi aberto!"
                else:
                    premio = fundo * 0.60
                    fundo  = 0.0
                    mensagem = f"Cofre aberto, {nome}! Ganhou R$ {premio:.2f}"
            else:
                mensagem = (
                    f"Código Errado, {nome}. "
                    f"O cofre tem R$ {fundo:.2f} acumulados."
                )

        # Enviar resposta
        resposta = pickle.dumps({"mensagem": mensagem})
        conn.sendall(resposta)

    except Exception as e:
        print(f"[!] Erro com {addr}: {e}")
    finally:
        conn.close()
        print(f"[-] Conexão encerrada: {addr}")


def main():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    servidor.bind((HOST, PORT))
    servidor.listen()

    print(f"Cofre Digital iniciado: {HOST}:{PORT} …")

    while True:
        conn, addr = servidor.accept()           # bloqueia até um cliente chegar
        t = threading.Thread(
            target=call_client,
            args=(conn, addr),
            daemon=True
        )
        t.start()

if __name__ == "__main__":
    main()