#!/usr/bin/python
# From http://superuser.com/a/567595

from socket import *
myHost = ''
myPort = 17

s = socket(AF_INET, SOCK_STREAM)    # create a TCP socket
s.bind ( (myHost, myPort) )
s.listen (5)

while 1:
  connection, address = s.accept() 
  connection.send("echo Hello World\n")
  connection.close() 
