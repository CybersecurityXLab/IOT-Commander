import os
import time
"""
Requirements:
This program requirse the dotnet package.  
Instructions for this can be found at https://dotnet.microsoft.com/download/linux-package-manager/ubuntu16-04/sdk-current
Once this is instaleld run: "npm i -g tplink-lightbulb" to get the lightbulb specfic data.
Details on the lightbulb command can be found at : https://www.npmjs.com/package/tplink-lightbulb



"""
def scan():
#scans for tplight bulbs
    os.system("tplight scan")

#end scan

def lightOn(ip):
#accepts the ip address of the tplight and turns it on
    os.system("tplight on " + ip)
#end lightOn

def lightOff(ip):
    #accepts the ip of the tplight and turns it off
    os.system("tplight off " + ip)
#end lightoff


def strobeLight(ip, strobeCT):
    #accepts the ip of the tplight and number of repetitions and causes the light to perform a strobelight effect
    i = 0    
    for i in range(strobeCT):
        lightOn(ip)
        time.sleep(2)
        lightOff(ip)
#end strobeLight


       



