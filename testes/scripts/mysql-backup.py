#! /usr/bin/python
# -*- coding: utf-8 -*-
import os, time, subprocess
from ConfigParser import ConfigParser

#author="Maurício Sousa"

config = ConfigParser()
# em Debian, /etc/mysql/debian.cnf contem 'root' login and password.
config.read("/etc/mysql/debian.cnf")
username = config.get('client', 'user')
password = config.get('client', 'password')
hostname = config.get('client', 'host')
date = time.strftime('%Y-%m-%d-%H:%M')
# diretorio de armazenamento dos backups
dest = "/var/backups/mysql"

def clear(directory):
  number_of_files = len([item for item in os.listdir(directory) if os.path.isfile(os.path.join(directory, item))])
  if number_of_files > 1:
    print "% s - Foram encontrados %s arquivos de backup no diretório %s" % (date, number_of_files, directory)
    purge_dir(directory)
  else:
    print "%s - Foram encontrados %s arquivos de backup nenhum será removido %s" % (date, number_of_files, directory)

def checkfile(filename):
    filestats = os.stat(filename) # pega informaçoes do arquivo
    if time.time() - filestats.st_mtime > 86400*7: # checa se o arquivo tem mais de 7 dias e remove caso positivo
        print "Removendo: %s" % (filename)
        os.remove(filename)

def purge_dir(path):
  dirList = os.listdir(path) # Lista o diretório
  for filename in dirList:
    checkfile(os.path.join(path, filename)) # executa funcao checkfile.


def backup():
 database_list_command="mysql -u %s -p%s -h %s --silent -N -e 'show databases'" % (username, password, hostname) #lista databases
 for database in os.popen(database_list_command).readlines():
     database = database.strip()
     if database == 'information_schema':
         continue
     if database == 'performance_schema':
         continue
     print "%s - Criando Backup database: %s" % (date, database)
     target_dir = "%s/%s" % (dest, database)
     if not os.path.exists(target_dir):
      print "%s - Criando novo diretório: %s" % (date, target_dir)
      os.makedirs(target_dir)
     filename = "%s/%s-%s.sql" % (target_dir, database, date)
     os.popen("mysqldump --max_allowed_packet=128M --single-transaction -u %s -p%s -h%s %s | bzip2 -c > %s.bz2" % (username, password, hostname, database, filename))
     clear(target_dir)
     
backup()
