#!/usr/bin/python2                                                              
                                                                                
import socket                                                                   
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)                             
s.bind(('0.0.0.0',2222))                                                        
s.listen (10)                                                                   
while True:                                                                     
        conn, addr = s.accept()                                                 
        print 'connected:', addr                                                
        while True:                                                             
                data=conn.recv(1024)                                            
                print 'data is:', data                                          
                if not data :break                                          
                conn.send(data)                                                 
        conn.close()                                                            
                       
                       
                       
#!/usr/bin/python2                                                              
                                                                                
import socket                                                                   
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)                             
s.bind(('0.0.0.0',2222))                                                        
s.listen (10)                                                                   
n=0                                                                             
while True:                                                                     
        conn, addr = s.accept()                                                 
        n=n+1                                                                   
        print 'try:',n,' connected:', addr                                      
        while True:                                                             
                data=conn.recv(1024)                                            
                print 'data is:', data                                          
                if not data :break                                              
                conn.send(data)                                                 
        conn.close()     
        
        
#!/usr/bin/python2                                                              
                                                                                
import socket                                                                   
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)                             
s.bind(('0.0.0.0',2222))                                                        
s.listen (11)                                                                   
n=0                                                                             
while n<=9:                                                                     
        print 'waiting...'                                                      
        conn, addr = s.accept()                                                 
        n=n+1                                                                   
        print 'try:',n,' connected:', addr                                      
        while True:                                                             
                data=conn.recv(1024)                                            
                print 'data is:', data                                          
                if not data :                                                   
                        print  'break found'                                    
                        break                                                   
                conn.send(data)                                                 
        conn.close()                                                            
        print 'connection ',n,' is close'         