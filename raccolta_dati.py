import pzgram
import requests
bot=pzgram.Bot("758461360:AAG1uPeuhZMi1k-Jt2-mknmjyZLUMztNi6I")
#bot1=pzgram.Bot("760136774:AAGaGil-U8PTbRMIQpmSyTHA-f_bF2aghPc")
def setbot(chat):
	button1 = pzgram.create_keyboard([["istantanea","1min","10min","1ora"]])
	chat.send("Select a command", reply_markup=button1)


def sendIstantanea(chat):
	chat.send("ciao")
	#pass
def ricerca_istantanea(chat,message):
	chat.send("ricerca istantanea avviata!")
	chat.send(message)
	#bot.set_next(chat,nome della funzione da eseguire)
	#pass

def ricerca_un_minuto(chat,message):
	chat.send("ricerca da un minuto avviata!")
	#pass

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
#start_
#bot.set_commands({"ricerca_istantanea": ricerca_istantanea})

bot.set_commands({"avvia": setbot})
bot.set_commands({"istantanea": sendIstantanea}) 

bot.run()
#bot.set_commands({"ricerca_10_minuti":ricerca_dieci_minuti,"ricerca_un_ora":ricerca_un_ora})
       #fa partire il bot
#pzgram.Chat(bot1, 553695220).send("sm")     #manda un messaggio su telegram
#if __name__ == "__main__":
#	telebot().setbot()
#	bot.run()
