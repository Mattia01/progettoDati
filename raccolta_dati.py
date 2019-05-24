import pzgram
import requests
import threading
import mosquitto
import time
media=0
#bot=pzgram.Bot("758461360:AAG1uPeuhZMi1k-Jt2-mknmjyZLUMztNi6I")
#bot1=pzgram.Bot("760136774:AAGaGil-U8PTbRMIQpmSyTHA-f_bF2aghPc")
def setbot(chat):
	button1 = pzgram.create_keyboard([["/istantanea","/un_min"],["/dieci_min","/una_ora"]])
	chat.send("Select a command", reply_markup=button1)

def sendIstantanea(chat):
	chat.send("ricerca istantanea avviata!")
	t=threading.Thread(target=mosquitto.istantanea)
	t.start()
	t1 = threading.Thread(target = mosquitto.calcolo)
	t1.start()
	t1.join()
	chat.send(media)

def ricerca_un_minuto(chat,message):
	global media
	chat.send("ricerca da un minuto avviata!")
	t = threading.Thread(target =mosquitto.ricevi_dati_minuto)
	t.start()
	t1 = threading.Thread(target = mosquitto.calcolo2)
	t1.start()
	t1.join()
	chat.send(media)



def ricerca_dieci_minuti(chat,message):
	chat.send("ricerca da 10 minuti avviata!")
	t = threading.Thread(target =mosquitto.ricevi_dati_minuti)
	t.start()
	t1 = threading.Thread(target = mosquitto.calcolo3)
	t1.start()
	t1.join()
	chat.send(media)



def ricerca_una_ora(chat,message):
        chat.send("ricerca da un' ora  avviata!")
	t = threading.Thread(target =mosquitto.ricevi_dati_ora)
	t.start()
	t1 = threading.Thread(target = mosquitto.calcolo4)
	t1.start()
	t1.join()
	chat.send(media)
def lauch():
	bot.set_commands({"avvia": setbot})
	bot.set_commands({"istantanea": sendIstantanea})
	bot.set_commands({"un_min": ricerca_un_minuto})
	bot.set_commands({"dieci_min": ricerca_dieci_minuti})
	bot.set_commands({"una_ora": ricerca_una_ora})
	bot.run()

if __name__ == '__main__':
	bot=pzgram.Bot("758461360:AAG1uPeuhZMi1k-Jt2-mknmjyZLUMztNi6I")
	lauch()
#bot.set_commands({"ricerca_10_minuti":ricerca_dieci_minuti,"ricerca_un_ora":ricerca_un_ora})
       #fa partire il bot
#pzgram.Chat(bot1, 553695220).send("sm")     #manda un messaggio su telegram
#if __name__ == "__main__":
#	telebot().setbot()
#	bot.run()
