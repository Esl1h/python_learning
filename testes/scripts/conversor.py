def celtokel(C): # Celsius para Kelvin
    K = (C + 273.15)
    return ('\n{K:.2f}K' .format(K = K))

def celtofah(C): # Celsius para Fahrenheit
    F = (C * 1.8 + 32)
    return('\n{F:.2f}°F' .format(F = F))

def keltocel(K): # Kelvin para Celsius
    C = (K - 273.15)
    return ('\n{C:.2f}°C' .format(C = C))

def keltofah(K): # Kelvin para Fahrenheit
    F = (K * 1.8 - 459.7)
    return('\n{F:.2f}°F' .format(F = F))

def fahtocel(F): # Fahrenheit para Celsius
    C = ((F -32) / 1.8)
    return ('\n{C:.2f}°C' .format(C = C))

def fahtokel(F): # Fahrenheit para Kelvin
    K = ((F - 32) / 1.8 + 273)
    return ('\n{K:.2f}K' .format(K = K))
	
def menu():	
	escolha = int(input('''
	Menu:
	1 - Celsius para Kelvin
	2 - Celsius para Fahrenheit
	3 - Kelvin para Celsius
	4 - Kelvin para Fahrenheit
	5 - Fahrenheit para Celsius
	6 - Fahrenheit para Kelvin
	7 - Sair
	
Escolha: '''))
	if escolha == 1:
		print(celtokel(int(input('Valor em °C(celsius) para ser convertido em K(Kelvin): '))))
	elif escolha ==2:
		print(celtofah(int(input('Valor em °C(Celsius) para ser convertido em °F(Fahrenheit): '))))
	elif escolha == 3:
		print(keltocel(int(input('Valor em K(Kelvin) para ser convertido em °C(Celsius): '))))
	elif escolha == 4:
		print(keltofah(int(input('Valor em K(Kelvin) para ser convertido em °F(Fahrenheit): '))))
	elif escolha == 5:
		print(fahtocel(int(input('Valor em °F(Fahrenheit) para ser convertido em °C(celsius): '))))
	elif escolha == 6:
		print(fahtokel(int(input('Valor em °F(Fahrenheit) para ser convertido em K(Kelvin): '))))
	elif escolha == 7:
		exit()
	else:
		print('Escolha Inválida')
		menu()
menu()
