# CN-Proj
Network load Balancer (CN Project)
This project implements a load balancing system using Python, with a load balancer (load.py), multiple application servers (server.py), and a client simulation (client.py).

###################################################Features#########################################################################

Multi-threaded HTTP servers

Load balancing based on active connections

Simulated load testing with retry logic

Enhanced logging for monitoring

##################################################Files#############################################################################

server.py: Starts a multi-threaded HTTP server.

load.py: Implements a load balancer and manages connections between clients and servers.

client.py: Simulates traffic to the load balancer.

100MB.bin: A sample file served by the HTTP servers.

###################################################Prerequisites###################################################################

Python 3.7 or higher

requests library (install using pip install requests)

Linux/MacOS/Windows terminal

#################################################Setup Instructions###################################################################
step 1: Place all the project files in the same directory.

Ensure 100MB.bin exists in the directory to be served by the servers.

Step 2: Run the Application Servers

Open a terminal.

Start the application servers by specifying the start and end port numbers (e.g., ports 8001 to 8005):

python3 load.py 8001 8005

This initializes the load balancer on port 6000 and starts the servers on the specified port range.

Step 3: Simulate Client Requests

Open another terminal.

Run the client simulation script:

python3 client.py

This sends multiple HTTP requests to the load balancer and distributes the load across the servers.
