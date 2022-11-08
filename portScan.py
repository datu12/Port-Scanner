import socket
import sys
import subprocess
from datetime import datetime


#ip portrange (ASK FOR INPUT)
remoteServer = input(" + Enter remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)
print("\n")
print(" + Please wait scanning host")

time1 = datetime.now()

#write conn -> to IP/DNS/HOST (Create Conn, IPv4 - TCP)
try:
    for port in range(1,65000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((remoteServerIP,port))
        if result == 0:
            print(" Port {}:               Open".format(port))
        s.close()
except KeyboardInterrupt() as e:
    while e is True:
        print(" + CTRL + C has been pressed")
        print(" + Program will exit")
        sys.exit()
#If hostname is wrong
except socket.gaierror() as f:
    while f is True:
        socket.close()
        print("Invalid hostname {}".format(remoteServer))
        sys.exit()
except socket.setdefaulttimeout(120) as g:
    while g is True:
        print(" + User has taken more than 2 minutes to decide")
        print(" + Program will now close")
        socket.close()
    sys.exit()
print('\n')
time2 = datetime.now()
totalRunTime = time2 - time1
print(" + Scanning completed in: {}".format(totalRunTime))

#Next part of this code -- 
#Fix -- Error handling issues
#Add -- type of port services 
