#!/usr/bin/python
#-*-coding:iso-8859-1 -*-

#############################################################################################################
#############################################################################################################
###-------------------------------------------------------------------------------------------------------###
###  Script: Conn.py                                                                                      ###
###  Versão: 1.0     Data:08/05/2010                                                                      ###
###  Autor: Rafael Iguatemy dos Santos - rafael.dsantos@bol.com.br                                        ###
###-------------------------------------------------------------------------------------------------------###
### Este script testa a conexão de uma lista de ips, conecta via telnet todos os que estão disponíveis,   ###
### aplica e salva em arquivos separados as configurações necessárias em nos roteadores                   ###
#############################################################################################################
#############################################################################################################
import os
import telnetlib

def pingar(ips):
	''' 
	  Testar a Conectividade e separar os IPs que estão conectados
	'''
	ipok = []
	ipfora = []
	for ip in ips:
		ping = os.popen('ping -c 10 %s' % ip).read()
		print ping
		print 75*"-"
		if ('64 bytes from') in ping:
			ipok.append(ip)
		else:
			ipfora.append(ip)
	return ipok
	
def verifica_ip(ip):
	'''Verifica se o ip e valido e separa os octetos
	'''
	oct1,oct2,oct3,oct4 = "","","",""
		
	for i in range(len(ip)):
		if ip[i] != '.':
			oct1 += ip[i]
		else:
			ipr1 = ip[i+1:]
			break
	for j in range(len(ipr1)):
		if ipr1[j] != '.':
			oct2 += ipr1[j]
		else:
			ipr2 = ipr1[j+1:]
			break
	for w in range(len(ipr2)):
		if ipr2[w] != '.':
			oct3 += ipr2[w]
		else:
			oct4 = ipr2[w+1:]
			break
	if int(oct1) == 0 or int(oct1)>255 or int(oct2)>255 or int(oct3)>255 or int(oct1)>255 or len(ip)>15 or ip.count('.')!=3:
		print "ip incorreto"
	else:
		ips = oct1+'.'+oct2+'.'+oct3+'.'+oct4
		return ips



user = 'CISCO'
password = 'CISCO'	  
ip = ''
ips = []

# Quando o ip 1.0.0.0 for digitado, o looping da entrada de dados terminará
while ip != '1.0.0.0':
	ip = raw_input('Entre com IP / Digite 1.0.0.0 para sair')
	x = verifica_ip(ip)
	ips.append(x)
ips.remove('1.0.0.0')

ipsok = pingar(ips)
print ipsok
for HOST in ipsok:
	#Autenticação no roteador via Telnet
	tn = telnetlib.Telnet(HOST)
	tn.read_until("Username: ", 3)
	tn.write(user + "\r\n")
	tn.read_until("Password: ", 3)
	tn.write(password + "\r\n")
	
	#Comandos da IOS Cisco (Aqui que customizamos o script para qualquer configuração feita no roteador)
	tn.write("term length 0"+ "\r\n")
	tn.write("sh ip bgp sum" + "\r\n")
	tn.write("logout" + "\r\n")
	
	#
	str_all = tn.read_all()
	tn.close()
	try: # Teremos de saída 1 arquivo para cada roteador        
		arq = "arq_"+HOST+".txt"
		f = open(arq, "w")
		try:
			f.write(str_all)
		finally:
			f.close
	except IOError:
		pass
		