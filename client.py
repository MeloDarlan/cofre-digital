import socket
import pickle
import os
from dotenv import load_dotenv

load_dotenv()

HOST = '127.0.0.1'
PORT = int(os.getenv("PORT"))

def main():
    try:
        nome = input("Seu nome: ").strip()
        aposta = int(input("Seu número (0 a 999): ").strip())
        if not 0 <= aposta <= 999:
            raise ValueError
    except ValueError as e:
        return e

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        pedido = {"nome": nome, "aposta": aposta}
        s.sendall(pickle.dumps(pedido)) # pickle para converter o dict em bytes

        dados = b""
        while True:
            parte = s.recv(4096)
            if not parte:
                break
            dados += parte
            try:
                resposta = pickle.loads(dados)
                break
            except Exception:
                continue
    print(resposta["mensagem"])

if __name__ == "__main__":
    main()