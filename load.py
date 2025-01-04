from time import sleep
import sys
import os
import threading
import socket
import random
import logging
from random import randint

BUFFER_SIZE = 4096
MAX_CONNECTIONS = 50

logging.basicConfig(
    filename="load_balancer.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

server_list = []
server_conn = []


def loadBalance():
    min_index = server_conn.index(min(server_conn))
    logging.info(f"{server_list[min_index]} chosen, active connections: {server_conn}")
    server_conn[min_index] += 1
    return server_list[min_index]


def sendToServer(conn, serverSock):
    try:
        ssock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ssock.connect(serverSock)
        logging.info(f"Server Connected: {serverSock}")

        while True:
            data = conn.recv(BUFFER_SIZE)
            if not data:
                break
            ssock.send(data)
            response = ssock.recv(BUFFER_SIZE)
            if response:
                conn.send(response)
    except Exception as e:
        logging.error(f"Error during connection: {e}")
    finally:
        server_conn[server_list.index(serverSock)] -= 1
        conn.close()
        ssock.close()
        logging.info(f"Connection closed: {serverSock}")


def startLoadBalancer(port):
    clientSideSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSideSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    clientSideSocket.bind(('127.0.0.1', port))
    logging.info(f"Load balancer listening on {port}")
    clientSideSocket.listen(MAX_CONNECTIONS)

    threading.Thread(target=accept_conn, args=(clientSideSocket,)).start()


def accept_conn(clientSideSocket):
    while True:
        try:
            conn, addr = clientSideSocket.accept()
            logging.info(f"Connection accepted from {addr}")
            threading.Thread(target=sendToServer, args=(conn, loadBalance())).start()
        except Exception as e:
            logging.error(f"Connection acceptance error: {e}")


def serverThread(port):
    os.system(f"python3 server.py {port}")


def startApplicationServers(startPort, endPort):
    for port in range(startPort, endPort + 1):
        server_list.append(('localhost', port))
        server_conn.append(0)
        threading.Thread(target=serverThread, args=(port,)).start()
    logging.info(f"Application servers initialized: {server_list}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 load.py <start_port> <end_port>")
        sys.exit(1)

    startApplicationServers(int(sys.argv[1]), int(sys.argv[2]))
    startLoadBalancer(6000)