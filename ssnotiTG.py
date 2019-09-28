from twx.botapi import TelegramBot, ReplyKeyboardMarkup
import os
import datetime
import random
import emoji
import socket
import sys

"""
Setup the bot
"""

bot = TelegramBot('808550713:AAHkkh0LkkfX3-j2pHFGED0AEuINIKq-ZnY')
print (bot)
bot.update_bot_info().wait()

last_id = 0
print(bot.username)

TELEGRAM_MSGID=0;
TELEGRAM_MSG=1;

"""
Setting up Sensesurround server address 
"""
#sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10002)
#print >>sys.stderr, 'connecting to SS via port %s %s' % server_address
#sock.connect(server_address)

"""
Send a message to a user
"""
#create objects first
updates = bot.get_updates(offset= last_id, timeout=600).wait()
msg  = updates[len(updates)-1][TELEGRAM_MSG]

#result = bot.send_message(user_id, 'test message body').wait()
#print(result)

"""
Get updates sent to the bot
"""
pmsg = 'jbufs'
welcome_list = ['Welcome to SNPS! ' + emoji.emojize(":grinning_face_with_big_eyes:"), 'SNPS welcomes you! ' + emoji.emojize("\xF0\x9F\x8D\xBB"), 'Irasshaimase! ' + emoji.emojize("\xF0\x9F\x87\xAF\xF0\x9F\x87\xB5"), 'Hwan-Yeong! ' + emoji.emojize("\xF0\x9F\x87\xB0\xF0\x9F\x87\xB7")]

while True:
    updates = bot.get_updates(offset= last_id, timeout=600).wait()
    if updates is not None:
        if len(updates) > 0:
             msg  = updates[len(updates)-1][TELEGRAM_MSG]
        chat= msg.chat
        encodedtext = msg.text
        if encodedtext is not None:
             encodedtext.encode(encoding='utf-8',errors='ignore')
             #print encodedtext.encode('utf-8')
        encodedpmsg = pmsg
        if encodedpmsg is not None:
             encodedpmsg.encode(encoding='utf-8',errors='ignore')
             #print encodedpmsg.encode('utf-8')    

        if pmsg is not msg.text:
            #if encodedpmsg is not None:
	    #print encodedpmsg.encode('utf-8')
             if len(updates) >= 0:
                 last_id = int(updates[len(updates)-1][TELEGRAM_MSGID])+1

             if msg.text is not None:
                 if "adding" in msg.text:
                      	bot.send_message(msg.chat.id, random.choice(welcome_list))
                 elif "Adding" in msg.text:
                      	bot.send_message(msg.chat.id, random.choice(welcome_list))
                 elif "Let's welcome" in msg.text:
                      	bot.send_message(msg.chat.id, random.choice(welcome_list))
                 elif "lets welcome" in msg.text:
                      	bot.send_message(msg.chat.id, random.choice(welcome_list))
                 elif "Lets welcome" in msg.text:
                      	bot.send_message(msg.chat.id, random.choice(welcome_list))
                 elif "let's welcome" in msg.text:
                      	bot.send_message(msg.chat.id, random.choice(welcome_list))
                 elif "Welcome " in msg.text:
                      	bot.send_message(msg.chat.id, random.choice(welcome_list))
                 elif "All the best" in msg.text:
                      	bot.send_message(msg.chat.id, "Good Luck..." + "\xF0\x9F\x98\x94")
                 elif "Farewell" in msg.text:
                     	bot.send_message(msg.chat.id, "Good Bye..." + "\xF0\x9F\x98\x9E")
                 elif "Take care" in msg.text:
                     	bot.send_message(msg.chat.id, "All the best.." + "\xF0\x9F\x99\x8F")
    		 elif "SS weather" in msg.text:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	      		print >>sys.stderr, 'connecting to SS via port %s %s' % server_address
			sock.connect(server_address)
			print >>sys.stderr, 'sending "%s"' % msg.text
			sock.sendall(msg.text)
			while True:
				data = sock.recv(16)
				print >>sys.stderr, 'received "%s"' % data
				if data:
					print >>sys.stderr, 'sending "%s" to TG' % data
					bot.send_message(msg.chat.id, data)
				else:
					print >>sys.stderr, 'no more data from SS'
					sock.close()
					break
		 elif "SS temperature" in msg.text:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			print >>sys.stderr, 'connecting to SS via port %s %s' % server_address
			sock.connect(server_address)
			print >>sys.stderr, 'sending "%s"' % msg.text
			sock.sendall(msg.text)
			while True:
                                data = sock.recv(16)
                                print >>sys.stderr, 'received "%s"' % data
                                if data:
                                        print >>sys.stderr, 'sending "%s" to TG' % data
                                        bot.send_message(msg.chat.id, data)
                                else:
                                        print >>sys.stderr, 'no more data from SS'
                                        sock.close()
					break


    pmsg=msg.text
