import sys
import socket
import datetime


if (len(sys.argv) == 4): 
    target = socket.gethostbyname(sys.argv[1]) 
    
else:
    print("Invalid amount of arguments!")
    print("Syntax: python3 portscanner.py <ip> <initial port #> <end port #> ")
    

print("-" * 50)
print("Scanning target: " + target)
print("Time started: " + str(datetime.datetime.now()))
print("-" * 50) 

try:

    for port in range(int(sys.argv[2]), int(sys.argv[3]) + 1 ): 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port)) 
    
        if (result == 0):
            print(f"Port {port} open")
        
        else:
            print(f"Port {port} closed")
        s.close()    
    
except KeyboardInterrupt:
    print("\nExiting...")
    sys.exit()
    
except socket.gaierror:
    print("The hostname couldn't be resolved.")
    sys.exit()
    
except socket.error:
    print("Couldn't connect to the server.")
    sys.exit()   
    
