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
    startCollectionOriginal(tn)
    
    #Executing commands
    print (tn.read_all())

    print ("Done")

def startCollectionOriginal(tnet):
    tnet.write("cd system\n")
    tnet.write("sh collection.sh &\n")
    tnet.write("exit\n")
    
    print ("Starting Collection Script")

def downloadAvacomFiles(mainFolder):
    username = 'admin'
    password = '1234'
    ip = '192.168.4.11'

    print("Downloading Files")

    subprocess.call('wget -O ' + mainFolder + 'ps_data_webcam.txt --user ' + username + ' --password ' + password + ' ' + ip + '/ps_data_webcam.txt', shell=True)
    time.sleep(1)
    subprocess.call('wget -O ' + mainFolder + 'top_data_webcam.txt --user ' + username + ' --password ' + password + ' ' + ip + '/top_data_webcam.txt', shell=True)
    time.sleep(1)
    subprocess.call('wget -O ' + mainFolder + 'date_data_webcam.txt --user ' + username + ' --password ' + password + ' ' + ip + '/date_data_webcam.txt', shell=True)
    time.sleep(1)
    subprocess.call('wget -O ' + mainFolder + 'netstat_data_webcam.txt --user ' + username + ' --password ' + password + ' ' + ip + '/netstat_data_webcam.txt', shell=True)

def main():
    os.system('clear')
    directory = '~/Documents/WebcamTest/'
    #startTCPDumpOnPi()
    #telnetIntoAvacom()
    downloadAvacomFiles(directory)
    downloadAvacomFiles(directory)

main()