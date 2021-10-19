import time
import getpass
import sys
#from pexpect import pxssh
import paramiko

#VETOR DE IPS 
vetip = ["lista","de","IP"]

#USUARIO DE ACESSO AOS DATACOM
usr = "usuario"
psswd = "senha"

#Command
command1 = "sed -i '81 s/ip_atual/Novo_IP/' /etc/zabbix/zabbix_agentd.conf"
command2 = "sed -i '81 s/ip_atual/Novo_IP/' /etc/zabbix/zabbix_agentd.conf "
command3 = "sed -i '122 s/ip_atual/Novo_IP/' /etc/zabbix/zabbix_agentd.conf "
command4 = "sed -i '122 s/ip_atual/Novo_IP/' /etc/zabbix/zabbix_agentd.conf "
command5 = r"""sed -i '274a\UserParameter=erromysql[*],cd /c5client/AcruxPDV/log/aplicacao && log=`ls -Art | tail -n 1` && dado=`tail -1 $log | grep 2006` && [[ -n "$dado" ]] && echo "true" || echo "false"' /etc/zabbix/zabbix_agentd.conf"""
command6 = '/etc/rc.d/rc.zabbix_agentd restart'

for host in vetip:
	try:
		cli = paramiko.SSHClient()
		cli.load_system_host_keys()
		cli.set_missing_host_key_policy(paramiko.WarningPolicy())
		cli.connect(host, port=22, username=usr, password=psswd)
		time.sleep(7)	

		stdin1, stdout1, stderr1 = cli.exec_command(command1)
		print(command1)
		print(stdout1.read())		
		time.sleep(1)

		stdin2, stdout2, stderr2 = cli.exec_command(command2)
		print(command2)
		print(stdout2.read())
		time.sleep(1)

		stdin3, stdout3, stderr3 = cli.exec_command(command3)
		print(command3)
		print(stdout3.read())
		time.sleep(1)

		stdin4, stdout4, stderr4 = cli.exec_command(command4)
		print(command4)
		print(stdout4.read())
		time.sleep(1)

		stdin5, stdout5, stderr5 = cli.exec_command(command5)
		print(command5)
		print(stdout5.read())
		time.sleep(1)

		stdin6, stdout6, stderr6 = cli.exec_command(command6)
		print(command6)
		print(stdout6.read())
		time.sleep(5)
	finally:
			cli.close()
