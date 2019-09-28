"""
This python script is designed to support a single telegram bot. Please change bot auth-code accordingly
This python scripts run on python 2.7 and twx.botapi unofficial Telegram Bot API Client 1.0B3
"""

from twx.botapi import TelegramBot, ReplyKeyboardMarkup
import os
import datetime
import random
import emoji
import sys
import socket

"""
Setup the test bot named @ssnoti_bot 
Change authcode below for new bots setup.
To setup a new bot, read botfather documentation in Telegram
"""

bot = TelegramBot('808550713:AAHkkh0LkkfX3-j2pHFGED0AEuINIKq-ZnY')
print (bot)
bot.update_bot_info().wait()

last_id = 0
print(bot.username)

TELEGRAM_MSGID=0;
TELEGRAM_MSG=1;

"""
Socket
"""

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#replace localhost with server dns or ip address; choose a high port to use
server_address = ('localhost', 10003)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)
sock.listen(1)
bufferdata = ""

while True:
        #create objects for bot
        updates = bot.get_updates(offset= last_id, timeout=600).wait()
        #if updates is not None:
		#if len(updates) > 0:
	msg  = updates[len(updates)-1][TELEGRAM_MSG]
	#bufferdata = ""
        #wait for a connection from Sensesurround
	#	chat = msg.chat
	#	encodedteext = msg.text
	#if encodedtext is not None:
	#	encodedtext.encode(encoding='utf-8',errors='ignore')
	#encodedpmsg = pmsg	
	#if encodedpmsg is not None:
	#	encodedtext.encode(encoding='utf-8',errors='ignore')
	if updates is not None:
  	    print >>sys.stderr, 'waiting for a connection'
            connection, client_address = sock.accept()
        
	    try:
	        print >>sys.stderr, 'connection from', client_address
	        #Receive data in 16 bytes chunk
	        while True:
		    data = connection.recv(16) 
		    print >>sys.stderr, 'received "%s"' % data
	            
		    if data:
			bufferdata = bufferdata + data
		    elif "" in data:
			bot.send_message(msg.chat.id, bufferdata)
			bufferdata = ""
			connection.close()
			break
		    else:
		        #send message to Telegram
	                bot.send_message(msg.chat.id, bufferdata)
			bufferdata = ""
			connection.close()
		        break

	    finally:
		bufferedata = ""
	        connection.close()

