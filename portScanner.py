import os
import datetime

def scanningMachine(ips):
#ips: a list of string formatted ip addresses to be scanned
#add a list of all desired IPs and it will output the scan results to a file
    filename =  str(datetime.date.today()) + "PortScan"
    #os.system("touch " + filename)
    for ip in ips:
        os.system("nmap -p- -oN -T5 " + filename + " --append-output " + str(ip)) 
    

scanningMachine(["192.168.1.104","192.168.1.105","192.168.1.107","192.168.1.109","192.168.1.112","192.168.1.113","192.168.1.115","192.168.1.116","192.168.1.120","192.168.1.127","192.168.1.128","192.168.1.129","192.168.1.134"])
