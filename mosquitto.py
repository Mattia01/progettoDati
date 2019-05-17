import subprocess
import time
import threading

event = threading.Event()
event2 = threading.Event()
event3 = threading.Event()

def ricevi_dati():
	global event
	c = 0
	with open('prova.txt','r+') as file:
		while c!=60:
			subprocess.Popen(['mosquitto_sub','-t','/calvino-08/#','-h','broker.shiftr.io','-u','calvino00','-P','0123456789','-d','-C','1'], stdout = file)
			c+=1
			time.sleep(1)
		event.set()
def minuto():
	global event
	if event.wait():
		contatore = 0
		cont = 1
		lista = []
		temperatura = 0
		with open("prova.txt","r+")as file:
			for item in file:
				if cont == 30:
					break
				contatore += 1
				if contatore == ((8*cont)-1):
					item = float(item)
					lista.append(item)
					cont += 1
			for i in range(len(lista)):
				temperatura = temperatura + lista[i]
			media = temperatura / cont
		return media
if __name__ == '__main__':
	t = threading.Thread(target = ricevi_dati)
	t.start()
	t.join()
	t1 = threading.Thread(target = minuto)
	t1.start()
	t1.join()
