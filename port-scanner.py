import sys
import socket
import datetime


if (len(sys.argv) == 4): 
    target = socket.gethostbyname(sys.argv[1]) 
    
else:
    print("Yanlış argüman!")
    print("Hata ip, başlangıç portu, bitiş portu şeklinde yazın.")
    

print("-" * 50)
print("Taranan adres: " + target)
print("Başlangıç zamanı: " + str(datetime.datetime.now()))
print("-" * 50) 

try:

    for port in range(int(sys.argv[2]), int(sys.argv[3]) + 1 ): 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port)) 
    
        if (result == 0):
            print(f"Port {port} açık")
        
        else:
            print(f"Port {port} kapalı")
        s.close()    
    
except KeyboardInterrupt:
    print("\nExiting...")
    sys.exit()
    
except socket.gaierror:
    print("Host adresi çözümlenemedi!")
    sys.exit()
    
except socket.error:
    print("Sunucuya bağlanılamıyor..!")
    sys.exit()   
    
