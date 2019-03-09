#!/usr/bin/python
#telnet code based from example on https://docs.python.org/2/library/telnetlib.html

import os,subprocess,random,time,datetime,sys,telnetlib


def startTCPDumpOnPi():
    print ('Starting SSH')
    
    username = 'pi'
    password = 'pinkbanana55'
    ip = '192.168.4.1'

    #Executes tcpDump_5Min.py on RPI wireless interface for 5 mins and saves pcap in the Documents/Packet_Captures directory
    cmd = 'python Documents/Code/tcpDump_5Min.py'
    subprocess.call('sshpass -p '+ password + ' ssh ' + username + '@' + ip + ' ' + cmd, shell=True)


def telnetIntoAvacom():
    
    print ('Starting Telnet')
    currentDT = datetime.datetime.now()
    print (str(currentDT))

    username = 'root'
    password = 'hslwificam'
    ip = '192.168.4.11'

    #Start telnet connection
    tn = telnetlib.Telnet(ip)

    #wait until login prompt
    tn.read_until("login: ")

    #enter username
    tn.write(username + "\n")
    
    #wait for password and enter password
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")

    #Write commands
    tn.write("cd system\n")
    tn.write("sh collection.sh &\n")
    tn.write("exit\n")
    
    print ("Starting Collection Script")

    #Executing commands
    print (tn.read_all())

    print ("Done")
    
def listAllFiles():
    cmd = "ls\n"
    return cmd





def main():


    os.system('clear')
    #startTCPDumpOnPi()
    telnetIntoAvacom()

main()