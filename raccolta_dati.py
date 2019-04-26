import pzgram
import requests
bot=pzgram.Bot("758461360:AAG1uPeuhZMi1k-Jt2-mknmjyZLUMztNi6I")
bot1=pzgram.Bot("760136774:AAGaGil-U8PTbRMIQpmSyTHA-f_bF2aghPc")
button1 = pzgram.create_button("Command1", data="istantanea")
button2 = pzgram.create_button("Command1", data="pressione")
button3 = pzgram.create_button("Command1", data="altitudine")
button4 = pzgram.create_button("Command1", data="luce")

keyboard_array = [["button1", "button2","button3","button4"]]
keyboard=pzgram.create_keyboard(keyboard_array)
pzgram.Chat.send("press a button",reply_markup=keyboard)

def sendIstantanea(chat):
	#chat.send

def ricerca_istantanea(chat,message):
	chat.send("ricerca istantanea avviata!")
	chat.send(message)
	#bot.set_next(chat,nome della funzione da eseguire)
	pass

def ricerca_un_minuto(chat,message):
	chat.send("ricerca da un minuto avviata!")
	pass

#def ricerca_dieci_minuti(chat,message):
#	chat.send("ricerca da 10 minuti avviata!")
#	pass
#def ricerca_un_ora(chat,message):
#	chat.send("ricerca da un'ora avviata!")
#	pass
#553695220

#def ric1():
	#scelta=1
	#mqtt.ricerca()


#def ric2():
	#scelta=2
	#mqtt.ricerca()


#def ric3():
	#scelta=3
	#mqtt.ricerca()


#def ric4():
	#scelta=4
	#mqtt.ricerca()

def start_command(chat):
	keyboard=pzgram.create_keyboard([["command1", "command2"]])
	pzgram.Chat.send("Select a command", reply_markup=keyboard)

def process_message(message,chat):
	if message.text=="Command1":
		ricerca_istantanea
	elif message.text =="Command2":
		ricerca_un_minuto(790671030,message)
#start_
bot.set_commands({"ricerca_istantanea": ricerca_istantanea})
bot.set_commands({ "istantanea": sendIstantanea}) 
#bot.set_commands({"ricerca_10_minuti":ricerca_dieci_minuti,"ricerca_un_ora":ricerca_un_ora})
       #fa partire il bot
#pzgram.Chat(bot1, 553695220).send("sm")     #manda un messaggio su telegram
pzgram.Chat.send("Script runned ")
bot.run()
