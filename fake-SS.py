"""
This python script is designed to fake response from Sensesurround to send infomation on demand to telegram using the ssnoti-to-TG.py script. This is a test program.
This python scripts run on python 2.7
"""

import sys
import socket

"""
Socket
"""

SSsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#replace localhost with server dns or ip address; choose a high port to use
#fake sensesurround server ip and tcp port
SSserver_address = ('localhost', 10002)
print >>sys.stderr, 'starting fake Sensesurround for info on demand use case. listening on %s %s' % SSserver_address
SSsock.bind(SSserver_address)
SSsock.listen(1)
bufferdata = ""
#connection, client_address = SSsock.accept()
while True:
  	    print >>sys.stderr, 'waiting for a connection'
                    
	    try:
	        connection, client_address = SSsock.accept()
		print >>sys.stderr, 'connection from', client_address
		#connection, client_address = SSsock.accept()
	        
		#Receive data in 16 bytes chunk
                while True:	        
			data = connection.recv(16)
			print >>sys.stderr, 'received "%s"' % data
	            
			if data:
				bufferdata = bufferdata + data
				print >>sys.stderr, 'adding bufferdata "%s"' % bufferdata
			
				#connection.close()
				
				if "SS temperature" in bufferdata:
					#send demanded data to SSnoti-to-TG.py
					print >>sys.stderr, 'sending to 30 degree to TG "%s"' % bufferdata
					connection.sendall("30 degrees C")
                        		#SSsock.close()
					bufferdata = ""
					connection.close()
					break
					
		  		elif "SS weather" in bufferdata:
					print >>sys.stderr, 'sending to gg to rain to TG "%s"' % bufferdata
					connection.sendall("Going to rain")
					#SSsock.close()
					bufferdata = ""
					data = ""
					connection.close()
					break
				
			elif "" in data:
				if "SS temperature" in bufferdata:
                                        #send demanded data to SSnoti-to-TG.py
                                        print >>sys.stderr, 'sending to elif empty to TG for "%s"' % bufferdata
                                        connection.sendall(data)
                                        #SSsock.close()
                                        bufferdata = ""
					data = ""
                                        connection.close()
                                        break

                                elif "SS weather" in bufferdata:
                                        print >>sys.stderr, 'sending to elif empty to TG for "%s"' % bufferdata
                                        connection.sendall(data)
                                        #SSsock.close()
                                        bufferdata = ""
                                        data = ""
                                        connection.close()
                                        break
				else:
					#connection.close()
                                        bufferdata = ""
                                        data = ""
                                        connection.close()
                                        break

			else:
				print >>sys.stderr, 'hitting else "%s"' % bufferdata
				bufferdata = ""
				#SSsock.close()
				bufferdata = ""
				connection.close()
				break
	    finally:
		bufferedata = ""
		connection.close()

