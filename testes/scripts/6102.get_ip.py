#!/usr/bin/python
import urllib.request

pagina = urllib.request.urlopen("http://meuip.com.br/index.php")

texto = pagina.read().decode("utf8")
busca = texto.find('div_ip").innerHTML = "')

inicio = busca + 22
final = texto[inicio:]
final = final.find('"')
final = inicio + final

ip = texto[inicio:final]
print (ip)
