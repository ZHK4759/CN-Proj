# CN-Proj
Network load Balancer (CN Project)
This project implements a load balancing system using Python, with a load balancer (load.py), multiple application servers (server.py), and a client simulation (client.py).

Features

Multi-threaded HTTP servers

Load balancing based on active connections

Simulated load testing with retry logic

Enhanced logging for monitoring

Files

server.py: Starts a multi-threaded HTTP server.

load.py: Implements a load balancer and manages connections between clients and servers.

client.py: Simulates traffic to the load balancer.

100MB.bin: A sample file served by the HTTP servers.

Prerequisites

Python 3.7 or higher

requests library (install using pip install requests)

Linux/MacOS/Windows terminal
