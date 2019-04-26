#!/usr/bin/python
# -*- coding: utf-8 -*-
# Nome do arquivo: backup.py
import os
import time
import glob

# Mantem apenas 1 arquivo de bkp, removendo o anterior antes de criar
# devido o diretório estar sendo sincronizado com o dropbox (limitação de espaço)

origem = [' ~/.mozilla',' ~/.thunderbird']
dir_bkp = '/home/esl1h/Dropbox/LABS/BKP'
alvo = dir_bkp + os.sep + time.strftime('%Y%m%d%H%M')+'_thunderbird_firefox-profiles.zip'
zip = "zip -qr {0} {1}".format(alvo,''.join(origem))

filelist = glob.glob("/home/esl1h/Dropbox/LABS/BKP/*.zip")
for f in filelist:
    os.remove(f)
    
if os.system(zip) == 0:
     print('backup Concluído' , alvo)
     os.system("zenity --info --text='O Backup foi concluido ! \n' ")
else:
     print('backup falhou! Revise os parametros no código, pontos de montagem e os diretórios.')
     os.system('zenity --error --text="O Backup Falhou ! \n Revise os parametros e os diretórios." ') 

