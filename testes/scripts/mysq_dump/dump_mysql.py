#!/usr/bin/python

import MySQLdb
import os
import shutil
import commands
import datetime
import smtplib
from email.MIMEText import MIMEText
from envia_email import envia_email

#INSIRA AQUI OS DADOS DO SERVIDOR MYSQL 
USER = 'root'
PASS = 'senha-bd'
HOST = 'localhost'
PATH = 'MYSQL_DUMP'
BARRA = '/'
DOIS_PONTOS = ":"
EMAIL= "email@dominio.com.br"
#DIRETORIO ONDE DEVERA SALVAR OS ARQUIVOS DE DUMP
PWD = os.getcwd()
#VARIAVEL QUE DEFINE QUANTOS DIAS DEVE ARMAZENAR O DUMP
DIAS_ATRAS = 3

#VERIFICANDO SE EXISTE O DIRETORIO PRINCIPAL
if os.path.exists(PATH):
    log = 'Dir ja existe'
else:
    os.mkdir(PATH) 
    
NOW  = datetime.datetime.now()  
HOJE = NOW.strftime('%d-%m')
HORARIO_ATUAL = str(NOW.hour) + DOIS_PONTOS + str(NOW.minute) 

#VERIFICANDO SE EXISTE O DIRETORIO DO DIA
if os.path.exists(PWD + BARRA + PATH + BARRA + HOJE):
    log = 'Dir ja existe'
else:
    os.mkdir(PWD + BARRA + PATH + BARRA + HOJE)

#CRIANDO O DIRETORIO DA HORA DO DUMP
DIR_HORAIO = (PWD + BARRA + PATH + BARRA + HOJE + BARRA + HORARIO_ATUAL)
os.mkdir(DIR_HORAIO)

#GERANDO O LOG PARA ENVIO DE EMAIL - RELATORIO DE BACKUP
DATA = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
INICIO = DATA + ' Started dump backup'

#INICIANDO O SCRIPT E GERANDO O LOG NO ARQUIVO
DUMP = "_dump"
var_file = open(DIR_HORAIO + BARRA + DUMP, "a")
var_file.write(INICIO + "\n")

#INTERAGINDO COM O MYSQL
db = MySQLdb.connect(HOST, USER, PASS)
cursor = db.cursor()
cursor.execute("show databases")
databases = cursor.fetchall()

#DUMP
TABELA = '<table class="border" align="center" valign="top" width="600">'
messages = TABELA
for base in databases:
        DESTINO = DIR_HORAIO + BARRA + base[0]+'.sql.gz'
        HORARIO = commands.getoutput("date +'%r'")
        if base[0] != 'information_schema':
                print base[0]
                if os.system('mysqldump -x -e -u %s -p%s -h %s --databases %s | gzip > %s' %(USER,PASS,HOST,base[0],DESTINO)) == 0:
                        messages += "<tr><td>%s</td><td>%s</td><td><b style='color:green'>OK</b></td></tr>" \
                        %(HORARIO,base[0])
                else:
                        messages += "<tr><td>%s</td><td>%s</td><td><b style='color:red'>NOT</b></td></tr>" \
                        %(HORARIO,base[0])
messages += "</table>"
print messages

#REMOVENDO OS ARQUIVOS E DIRETORIO ANTERIORES
AGORA = datetime.date.today()
DATAANTIGA = (AGORA - datetime.timedelta(DIAS_ATRAS)).strftime('%d-%m')
if os.path.exists(PATH + BARRA + DATAANTIGA):
    shutil.rmtree(PATH + BARRA + DATAANTIGA)

#LOG
DATA = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
FIM = DATA + ' Finish dump backup'
DUMP = "_dump"
var_file = open(DIR_HORAIO + BARRA + DUMP, "a")
var_file.write(FIM + "\n")



#DISPARANDO EMAIL
envia_email(EMAIL,messages)


