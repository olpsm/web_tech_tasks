import socket  
import asyncore

class EchoHandler(asyncore.dispatcher_with_send):
    def handle_read (self):
	data=self.recv(1024)
	if data:
	    if data=='' or data=='close':
		self.close()
	    else:
		print 'data is: ', data
		self.send(data)
class EchoServer(asyncore.dispatcher):

    def __init__(self, host, port):
	asyncore.dispatcher.__init__(self)
	self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
	self.set_reuse_addr()
	self.bind((host,port))
	self.listen(10)
    def handle_accept(self):
	pair=self.accept()
	if pair is not None:
	    sock,addr=pair
	    print 'Incoming connections from %s' % repr(addr)
	    handler = EchoHandler(sock)
                                      

server = EchoServer ('0.0.0.0',2222)
asyncore.loop()

                          
#s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)                             
#s.bind(('0.0.0.0',2222))                                                        
#s.listen (11)                                                                   
#n=0                                                                             
#while n<=9:                                                                     
        #print 'waiting...'                                                      
        #conn, addr = s.accept()                                                 
        #n=n+1                                                                   
        #print 'try:',n,' connected:', addr                                      
        #while True:                                                             
                #data=conn.recv(1024)                                            
                #print 'data is:', data                                          
                #if not data :                                                   
                        #print  'break found'                                    
                        #break                                                   
                #conn.send(data)                                                 
        #conn.close()                                                            
        #print 'connection ',n,' is close'  
