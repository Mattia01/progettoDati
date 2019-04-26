import subprocess
import time

temperatura = ""
pressione = ""
altitudine = ""
luce = ""

class mqtt:
	def ricevi_dati(self):
		cont = 0
		global temperatura, pressione, altitudine, luce
		with open('prova.txt','r+') as file:
			#print(time.strftime('%H:%M:%S'))
			subprocess.Popen(['mosquitto_sub','-t','/calvino-08/#','-h','broker.shiftr.io','-u','calvino00','-P','0123456789','-d','-C','4'], stdout=file)
			for item in file:
				cont += 1
				if cont == 7:
					temperatura = item.strip()
				elif cont == 9:
					pressione = item.strip()
				elif cont == 11:
					altitudine = item.strip()
				elif cont == 13:
					luce = item.strip()					
			print(temperatura)		
			print(pressione)
			print(altitudine)
			print(luce)			
			
	def ricerca(self,scelta):
		global temperatura, pressione, altitudine, luce
		ora_attuale = time.strftime('%H')
		minuti_attuali = time.strftime('%M')
		secondi_attuali = time.strftime('%S')
		with open('prova.txt','r+') as file:
			if scelta == 1:
				pass
			elif scelta == 2:
				pass
			elif scelta == 3:
				pass
			elif scelta == 4:
				pass		

if __name__ == '__main__':
	mqtt().ricevi_dati()
	mqtt().ricerca(1)
