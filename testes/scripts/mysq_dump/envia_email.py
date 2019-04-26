#!/usr/bin/python

# LIBS
import os
import commands
import time
import smtplib
from email.MIMEText import MIMEText

# FUNCAO ENVIA EMAIL
def envia_email(recebe1,recebe2):
    # DEFINA AS VARIAVEIS ABAIXO DE ACORDO COM O SEU AMBIENTE
    SMTP    =   "smtp.googlemail.com"
    PORTA   =   "587"
    LOGIN   =   "email@gmail.com"
    EMAIL   =   "email@gmail.com"
    PASS    =   "senha-aqui"
    if (PORTA == 465):
        SMTPSERVER = smtplib.SMTP_SSL
        PORTA = str(PORTA)
        ASSUNTO="Dump Mysql - Prod"
        HOSTNAME = commands.getoutput("hostname")
        MENSAGEM="Servidor: %s <br />Local do dump: %s<br /><br /><center>Databases%s</center>" %(HOSTNAME,os.getcwd(),recebe2)
        FROM=EMAIL
        TO=recebe1
        serv=SMTPSERVER()
        serv.connect(SMTP,PORTA)
        serv.login(LOGIN,PASS)
        msg1 = MIMEText("%s"% MENSAGEM,"html")
        msg1['Subject']=(ASSUNTO)
        msg1['From']=FROM
        msg1['To']=TO
        msg1['Content-type']="text/html"
        serv.sendmail(FROM,TO, msg1.as_string())
        serv.quit()
    else:
        SMTPSERVER = smtplib.SMTP
        PORTA = str(PORTA)
        ASSUNTO="Dump Mysql - Prod"
        HOSTNAME = commands.getoutput("hostname")
        MENSAGEM="Servidor: %s <br />Local do dump: %s<br /><br /><center>Databases%s</center>" %(HOSTNAME,os.getcwd(),recebe2)
        FROM=EMAIL
        TO=recebe1
        serv=SMTPSERVER()
        serv.connect(SMTP,PORTA)
        serv.starttls()
        serv.login(LOGIN,PASS)
        msg1 = MIMEText("%s"% MENSAGEM,"html")
        msg1['Subject']=(ASSUNTO)
        msg1['From']=FROM
        msg1['To']=TO
        msg1['Content-type']="text/html"
        serv.sendmail(FROM,TO, msg1.as_string())
        serv.quit()
  

