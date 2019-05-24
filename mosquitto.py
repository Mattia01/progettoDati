import subprocess
import time
import threading

event = threading.Event()
event2 = threading.Event()
event3 = threading.Event()
event4 = threading.Event()

def ricevi_dati_minuto():
	global event
	c = 0
	subprocess.call(['touch','prova.txt'])
	with open('prova.txt','r+') as file:
		while c!=12:
			subprocess.call(['mosquitto_sub','-t','/calvino-08/#','-h','broker.shiftr.io','-u','calvino00','-P','0123456789','-d','-C','1'], stdout = file)
			c+=1
			time.sleep(5)
		event.set()
def calcolo():
	global event
	if event.wait():
		event.clear()
		contatore = 0
		cont = 1
		lista = []
		temperatura = 0

		with open("prova.txt","r+")as file:
			for item in file:
				contatore += 1
				if contatore == ((8*cont)-1):
					item = float(item)
					lista.append(item)
					cont += 1
			for i in range(len(lista)):
				temperatura = temperatura + lista[i]
			media = temperatura / cont
			subprocess.call(['rm','prova.txt'])
		print(media)

def calcolo2():
	global event2
	if event2.wait():
		event2.clear()
		contatore = 0
		cont = 1
		lista = []
		temperatura = 0
		with open("prova.txt","r+")as file:
			for item in file:
				contatore += 1
				if contatore == ((8*cont)-1):
					item = float(item)
					lista.append(item)
					cont += 1
			for i in range(len(lista)):
				temperatura = temperatura + lista[i]
			media = temperatura / cont
			subprocess.call(['rm','prova.txt'])
		print(media)

def calcolo3():
	global event3
	if event3.wait():
		event3.clear()
		contatore = 0
		cont = 1
		lista = []
		temperatura = 0
		with open("prova.txt","r+")as file:
			for item in file:
				contatore += 1
				if contatore == ((8*cont)-1):
					item = float(item)
					lista.append(item)
					cont += 1
			for i in range(len(lista)):
				temperatura = temperatura + lista[i]
			media = temperatura / cont
			subprocess.call(['rm','prova.txt'])
		print(media)

def calcolo4():
	global event4
	if event4.wait():
		event4.clear()
		contatore = 0
		cont = 1
		lista = []
		temperatura = 0
		with open("prova.txt","r+")as file:
			for item in file:
				contatore += 1
				if contatore == ((8*cont)-1):
					item = float(item)
					lista.append(item)
					cont += 1
			for i in range(len(lista)):
				temperatura = temperatura + lista[i]
			media = temperatura / cont
			subprocess.call(['rm','prova.txt'])
		print(media)



def ricevi_dati_minuti():
	global event2
	c = 0
	subprocess.call(['touch','prova.txt'])
	with open('prova.txt','r+')as file:
		while c != 120:
			subprocess.call(['mosquitto_sub','-t','/calvino-08/#','-h','broker.shiftr.io','-u','calvino00','-P','0123456789','-d','-C','1'], stdout = file)
			c += 1
			time.sleep(5)
		event2.set()

def ricevi_dati_ora():
	global event3
	c = 0
	subprocess.call(['touch','prova.txt'])
	with open('prova.txt','r+')as file:
		while c != 720:
			subprocess.call(['mosquitto_sub','-t','/calvino-08/#','-h','broker.shiftr.io','-u','calvino00','-P','0123456789','-d','-C','1'], stdout = file)
			c += 1
			time.sleep(5)
		event3.set()

def istantanea():
	global event4
	cont = 1
	subprocess.call(['touch','prova.txt'])
	with open('prova.txt','r+') as file:
		subprocess.call(['mosquitto_sub','-t','/calvino-08/#','-h','broker.shiftr.io','-u','calvino00','-P','0123456789','-d','-C','1'], stdout = file)
		event4.set()


#if __name__ == '__main__':
	#t = threading.Thread(target = ricevi_dati_minuti)
	#t.start()
	#t1 = threading.Thread(target = calcolo2)
	#t1.start()
	#t1.join()
