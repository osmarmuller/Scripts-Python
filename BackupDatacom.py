import time
import getpass
import sys
#from pexpect import pxssh
import paramiko

#VETOR DE IPS 
vetip = "192.168.0.25"
vetsrv = ["192.168.0.131"]
vetproto = "tftp"
#VETOR DE SENHAS
vetsenha = []
vetresultado = []

#USUARIO DE ACESSO AOS DATACOM
psswd= "admin"
usr = "admin"

#command
nomearq = "testebkp.txt"
svfile = "show running-config | save"
rmfile = "file delete "

if vetip == "192.168.0.25" :
	print (vetip)
	#command1 salva o arquivo de backup na caixa
	command1 = svfile + " " + nomearq 
	#command2 exporta o backup para o servidor externo
	command2 = "copy file " + nomearq + " " + vetproto + "://" + "192.168.0.131"
	#command3 deleta o arquivo de backup da caixa
	command3 = rmfile + " " + nomearq 
	mkip = vetip
	try:
		cli = paramiko.SSHClient()
		cli.load_system_host_keys()
		cli.set_missing_host_key_policy(paramiko.WarningPolicy())
		cli.connect(mkip, port=22, username=usr, password=psswd)
		print "opa"
		time.sleep(10)	

		##salva o arquivo de backup na caixa
		print (command1)
		stdin1, stdout1, stderr1 = cli.exec_command(command1)
		print (stdin1)
		print (stdout1.read())
		time.sleep(7)

		##exporta o backup para o servidor externo
		print (command2)
		print "enviando arquivo"		
		stdin2, stdout2, stderr2 = cli.exec_command(command2)
		print (stdin2)
		print (stdout2.read())
		time.sleep(7)

		##deleta o arquivo da caixa
		print (command3)
		print "excluindo arquivo"
		stdin3, stdout3, stderr3 = cli.exec_command(command3)
		print (stdin3)
		print (stdout3.read())
		time.sleep(7)

	finally:
		cli.close()
