import os
import datetime

def scanningMachine(ips):
#ips: a list of string formatted ip addresses to be scanned
    filename =  str(datetime.date.today()) + "PortScan"
    #os.system("touch " + filename)
    for ip in ips:
        os.system("nmap -p- -oN " + filename + " --append-output " + str(ip)) 
    

scanningMachine(["192.168.1.116","192.168.1.104"])
