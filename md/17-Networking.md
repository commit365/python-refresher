
## 17. Networking: Basics of Networking in Python, Working with Sockets 

Python provides powerful tools for network programming, primarily through the `socket` module. This allows for low-level network communication and the creation of client-server applications. 

### Introduction to Sockets 

A socket is an endpoint of a two-way communication link between two programs running on a network. Python's `socket` module provides a way to work with sockets. 

```python 
import socket
```

## Creating a Socket

```python
# Create a TCP/IP socket 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

- `AF_INET`: Address Family for IPv4
- `SOCK_STREAM`: TCP socket type

## Server-Side Socket Programming

## Basic Server

```python
import socket 

# Create a socket object 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# Bind the socket to a specific address and port 
server_address = ('localhost', 12345) 
server_socket.bind(server_address) 

# Listen for incoming connections 
server_socket.listen(1) 
print(f"Server is listening on {server_address}") 

while True:     
	# Wait for a connection    
	connection, client_address = server_socket.accept()    
	try:        
		print(f"Connection from {client_address}")                 
		
		# Receive data        
		data = connection.recv(1024)        
		print(f"Received: {data.decode()}")                 
		
		# Send a response        
		connection.sendall(b"Message received")    
	finally:        
		# Clean up the connection        
		connection.close()
```

## Client-Side Socket Programming

## Basic Client

```python
import socket 

# Create a socket object 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# Connect to the 
server server_address = ('localhost', 12345) client_socket.connect(server_address) 

try:     
	# Send data    
	message = "Hello, server!"    
	client_socket.sendall(message.encode())         
	
	# Receive response    
	data = client_socket.recv(1024)    
	print(f"Received: {data.decode()}") 
finally:     
	# Clean up the connection    
	client_socket.close()
```

## Working with Hostnames and IP Addresses

```python
import socket 

# Get hostname 
hostname = socket.gethostname() 
print(f"Hostname: {hostname}") 

# Get IP address 
ip_address = socket.gethostbyname(hostname) 
print(f"IP Address: {ip_address}") 

# Get hostname by IP address 
print(socket.gethostbyaddr('8.8.8.8'))
```

## Handling Multiple Connections

For handling multiple connections, consider using `select` or asynchronous libraries like `asyncio`.

## Using `select`

```python
import select 
import socket 

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server_socket.bind(('localhost', 12345)) 
server_socket.listen(5) 

inputs = [server_socket] 

while inputs:     
	readable, _, _ = select.select(inputs, [], [])    
	for s in readable:        
		if s is server_socket:            
			connection, client_address = s.accept()
			inputs.append(connection)        
		else:            
			data = s.recv(1024)            
			if data:                
				s.send(data)            
			else:                
				s.close()                
				inputs.remove(s)
```

## Error Handling

Always use try-except blocks to handle network-related errors:

```python
try:     
	# Socket operations 
except socket.error as e:     
	print(f"Socket error: {e}")
```

## Practical Example: Simple Chat Server

```python
import socket 
import threading 

def handle_client(conn, addr):     
	print(f"New connection from {addr}")   
	while True:        
		try:            
			data = conn.recv(1024)            
			if not data:                
				break            
			message = data.decode()            
			print(f"Message from {addr}: {message}")
			conn.sendall(f"Server received: {message}".encode())        
		except:            
			break    
	conn.close() 
	
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) server.bind(('localhost', 12345)) 
server.listen() 
print("Server is listening...") 

while True:     
	conn, addr = server.accept()    
	thread = threading.Thread(target=handle_client, args=(conn, addr))   
	thread.start()
```

## Exercise

1. Create a simple echo server that repeats back any message sent by a client.
2. Implement a basic HTTP server that responds with "Hello, World!" to any GET request.
3. Write a client that can send multiple messages to the server and receive responses.

## Key Points

- Sockets provide low-level networking capabilities in Python.
- The `socket` module is used for creating both client and server applications.
- Always close sockets after use to free up system resources.
- Use error handling to manage network-related exceptions.
- For handling multiple connections, consider using `select` or asynchronous programming.
- Network programming requires careful consideration of security and error handling.
