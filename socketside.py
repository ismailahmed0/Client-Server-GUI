'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
#####
Ismail A Ahmed
serverside.py
Version 1.0
'''
#!/usr/bin/python           # This is server.py file

import socket               # Import socket module
import time

s = socket.socket()         # Create a socket object
host = str.encode(socket.gethostname()) # Get local machine name, encodes so we can send
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection. Connects up to 5 clients.

while True:
   c, addr = s.accept()# Establish connection with client.
   file = str.encode(time.ctime(time.time()))  # server time
   c.send(file) #sends server time