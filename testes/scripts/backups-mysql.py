#! /usr/bin/python
# Gera backups com o mysqldump e mantem historico de backups antigos.

import sys
import commands
import os
from datetime import datetime, timedelta

# declaracao

host      = "seu-host"
usuario   = "seu-login"
senha     = "sua-senha"
bancos    = ["banco-de-dados1", "banco-de-dados2"]
historico = 30
pathParaBackups = "/var/www/public_html/backups/"

# inicio
for banco in bancos:
    # prepara nomes & variaveis
    gerarBackup   = banco+"_"+datetime.now().strftime('%d%m%Y')+".sql"
    deletarBackupAntigo = pathParaBackups+banco+"_"+(datetime.now()-timedelta(days=historico)).strftime('%d%m%Y')+".sql"
    cmd   = "mysqldump -h "+host+" -u "+usuario+" --password="+senha+" "+banco+" > "+pathParaBackups+gerarBackup
    # executa comando no s.o
    commands.getoutput(cmd)
    # checa backup gerado
    backupGerado   = open(gerarBackup)
    backupGeradoConteudo = backupGerado.readline()
    # se gerou backup com conteudo, deleta backup mais antigo
    if len(backupGeradoConteudo) > 1:
        try:
            os.remove(deletarBackupAntigo)
        except OSError:
            pass
        except Error:
            pass
    else:
        pass
    # fecha backup
    backupGerado.close()

# fim
sys.exit(0)
