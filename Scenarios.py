"""
This program uses the modules to run scenarios.
Dependencies:
    All modules imported below are required.  All required modules can be located on the same gitHub as the scenarios

"""




import audioPlayer, lampControl, utilities,AvacomControl,attacks #required modules
import time # needed to sleep between commands
import datetime
import threading # needed to operate lamp with other devices
from multiprocessing import Process


"""
LOCAL VARIABLES: will need to be updated per device

"""
sudoPwd = "BajaB1@st"  # local password to utilize sudo


tpLightIP = "192.168.1.104"  #ip of the tp link lamp
avacomIP= "192.168.1.116"   #ip of the avacom webcam
ghIP = "10.0.0.10"      #ip of the google home
commanderIP = "192.168.1.100" #ip of iot commander
computerIP = "192.168.1.129" #ip of Amazon echo "computer"


"""
Time Keeping File
"""
timeFile = str(datetime.datetime.now()) + "_Scenario_Times.txt"

writeFile = open(timeFile, "w")
writeFile.close()
writeFile = open(timeFile, "a+")


def timeKeeper(moduleName,textFile, mode):
    #This functions accepts the name of the module, the name of the text file to write to, and whether the method started or ended and adds the start and end timestamps to a textfile for logging

    currentTime = datetime.datetime.now()
    #print(currentTime)    
    #O = open(textFile, "a+")
    output = str(moduleName) + " " + mode + " " + str(currentTime) + "\n"
    textFile.write(str(output))
    #O.close()
#end timeKeeper

def stringCopy(string2Copy):
    newString = ""
    for char in string2Copy:
        newString += char

    return newString
"""
    Wake Up Scenarios
**********************************************************************************************************
"""

def wakeUp():
    timeKeeper("WakeUp ", writeFile, "Beginning")
    timeKeeper("Light Turning On ", writeFile, "Beginning")
    lampControl.lightOn(tpLightIP)
    time.sleep(5)
    timeKeeper("Querrying Weather on Goolge Home", writeFile, "Beginning")
    audioPlayer.ghWeather()
    time.sleep(10)
    timeKeeper("Alexa turning on music ", writeFile, "Beginning")
    audioPlayer.compMusicOn()
    time.sleep(5)
    timeKeeper("Google home play music video", writeFile, "Beginning")
    audioPlayer.ghYoutubeOpen()
    time.sleep(5)
    timeKeeper("Alexa turn off muisc", writeFile, " ")
    audioPlayer.compMusicOff()
    time.sleep(5)
    timeKeeper("Google home stop playing music", writeFile, " ")
    audioPlayer.ghYoutubeClose()
    time.sleep(5)
    timeKeeper("light turning off", writeFile, " ")
    lampControl.lightOff(tpLightIP)
    timeKeeper("WakeUp", writeFile, "Ending") 
#end wakeUp

def DOSWakeUp(target):
    #accepts the IP of the device to attack
    dosThread = threading.Thread(target=attacks.hPing3, args = (target, 5000, sudoPwd))
    wakeThread = threading.Thread(target = wakeUp, args = ())
    wakeThread.start()
    timeKeeper("DoS Attack", writeFile, "Beginning")
    dosThread.start()
    dosThread.join()
    wakeThread.join()
    timeKeeper("DoS Attack", writeFile, "Ending")
#end DOSWakeUp()

def pingWakeUp(target):
    #accepts the IP of the device to attack, the size of the packet, and the number of attacks
    attackThread = threading.Thread(target=attacks.avacomPing, args = (str(avacomIP), str(target)))
    wakeThread = threading.Thread(target = wakeUp, args = ())
    wakeThread.start()
    timeKeeper("Ping Attack", writeFile, "Beginning")
    attackThread.start()
    attackThread.join()
    wakeThread.join()
    timeKeeper("Ping Attack", writeFile, "Ending")
#end PingWakeUp()

def scanWakeUp(target):
    #accepts the IP of the device to scan
    #attackThread = threading.Thread(target=attacks.scanning, args = (target))
    wakeThread = threading.Thread(target = wakeUp, args = ())
    wakeThread.start()
    timeKeeper("Scan", writeFile, "Beginning")
    attacks.scanning(target)
    #attackThread.start()
    #attackThread.join()
    wakeThread.join()
    timeKeeper("Scan", writeFile, "Ending")
#end scanWakeUp()

"""
    House Party Scenarios
**********************************************************************************************************
"""
    

def houseParty():
    timeKeeper("House Party", writeFile, "Beginning")
    lampThread= threading.Thread(target = lampControl.strobeLight, args=(tpLightIP,10))
    browser = AvacomControl.accessAvacomWebPortal(avacomIP)
    time.sleep(5)

    timeKeeper("Strobe Light ", writeFile, "Beginning")
    lampThread.start()
    
    timeKeeper("Alexa play music ", writeFile, "Beginning")
    audioPlayer.compMusicOn()
    time.sleep(5)
    timeKeeper("Google home open youtube", writeFile, "Beginning")
    audioPlayer.ghYoutubeOpen()
    
    timeKeeper("Avacom horizontal panning", writeFile, "Beginning")
    AvacomControl.avacomHorizPan(browser, 2)  
    timeKeeper("avacom horizontal panning", writeFile, "ending")
    lampThread.join(5)
    timeKeeper("strobe light ", writeFile, "ending")
    time.sleep(5)
    timeKeeper("google home close youtube ", writeFile, " ")
    audioPlayer.ghYoutubeClose()
    time.sleep(5)
    timeKeeper("computer turn off music ", writeFile, " ")
    audioPlayer.compMusicOff()
    time.sleep(2)
    timeKeeper("House Party", writeFile, "Ending")
    browser.close()
    
#end houseParty

def scanHouseParty(target):
    #accepts the IP of the device to scan
    attackThread = threading.Thread(target=attacks.scanning, args = (target))
    housePartyThread = threading.Thread(target = houseParty, args = ())
    housePartyThread.start()
    timeKeeper("Scan", writeFile, "Begining")
    attackThread.start()
    attackThread.join()
    housePartyThread.join()
    timeKeeper("Scan", writeFile, "Ending")
#end scanHouseParty()

def pingHouseParty(target):
    #accepts the IP of the device to ping
    attackThread = threading.Thread(target=attacks.avacomPing, args = (str(avacomIP), str(target)))
    housePartyThread = threading.Thread(target = houseParty, args = ())
    housePartyThread.start()
    timeKeeper("Ping Attack", writeFile, "Beginning")
    attackThread.start()
    attackThread.join()
    housePartyThread.join()
    timeKeeper("Ping", writeFile, "Ending")

#end pingHouseParty()
def DOSHouseParty(target):
    #accepts the IP of the device to DOS
    timeKeeper("DoS Attack", writeFile, "Beginning")
    attackThread = threading.Thread(target=attacks.hPing3, args = (target, 5000, sudoPwd))
    housePartyThread = threading.Thread(target = houseParty, args = ())
    housePartyThread.start()
    attackThread.start()
    attackThread.join()
    housePartyThread.join()
    timeKeeper("Dos Attack", writeFile, "Ending")

#end DOSHouseParty()

def bruteForceHouseParty(target, pwdFile):
    attackThread = threading.Thread(target = attacks.bruteForce, args = (target, pwdFile, sudoPwd))
    partyThread = threading.Thread(target = houseParty, args = ())
    partyThread.start()
    timeKeeper(("Brute Force Attack on"  + str(target)), writeFile, "Beginning")
    attackThread.start()
    attackThread.join()
    partyThread.join()
    timeKeeper("Brute Force Attack", writeFile, "Ending") 
#end bruteForceHouseParty


"""
    Enterprise Normal Business Hours Scenarios
**********************************************************************************************************
"""

def enterpriseNormalHours():
    timeKeeper("Enterprise Normal Businesss Hours", writeFile, "Begining")
    browser = AvacomControl.accessAvacomWebPortal(avacomIP)
    time.sleep(5)
    timeKeeper("Light Turned on", writeFile, " ")
    lampControl.lightOn(tpLightIP)
    timeKeeper("Avacom horizontal pan", writeFile, "Beginning")
    AvacomControl.avacomHorizPan(browser, 2)
    timeKeeper("Avacom horizontal pan", writeFile, "Ending")

    browser.close()
    timeKeeper("Enterprise Normal Business Hours", writeFile, "Ending")
#end enterpriseNormalHours

def scanEntNH(target):
    #accepts the IP of the device to scan

    attackThread = threading.Thread(target=attacks.scanning, args = (target))
    entNHThread = threading.Thread(target = enterpriseNormalHours, args = ())
    entNHThread.start()
    timeKeeper("Scan", writeFile, "Beginning")
    attackThread.start()
    attackThread.join()
    entNHThread.join()
    timeKeeper("Scan", writeFile, "Ending")
#end scaneEntNH()

def pingEntNH(target):
    #accepts the IP of the device to scan
    attackThread = threading.Thread(target=attacks.avacomPing, args = (str(avacomIP), str(target)))
    entNHThread = threading.Thread(target = enterpriseNormalHours, args = ())
    entNHThread.start()
    timeKeeper("Ping Attack", writeFile, "Beginning")
    attackThread.start()
    attackThread.join()
    entNHThread.join()
    timeKeeper("Ping Attack", writeFile, "Ending")

#end pingEntNH()
def DOSEntNH(target):
    #accepts the IP of the device to scan
    attackThread = threading.Thread(target=attacks.hPing3, args = (target, 5000, sudoPwd))
    entNHThread = threading.Thread(target = enterpriseNormalHours, args = ())
    entNHThread.start()
    timeKeeper("DoS Attack", writeFile, "Beginning")
    attackThread.start()
    attackThread.join()
    entNHThread.join()
    timeKeeper("DoS Attack", writeFile, "Ending")

#end DOSEntNH()

"""
    Enterprise After Hours Scenarios
**********************************************************************************************************
"""

def enterpriseAfterHours():
    timeKeeper("Enterprise After Hours", writeFile, "Begining")
    print("starting")
    #Browser setup
    browser = AvacomControl.accessAvacomWebPortal(avacomIP)
    time.sleep(10)

    #cameraThread = threading.Thread(target = AvacomControl.avacomHorizPan, args = (avacomIP, 10))
    #cameraThread.start()
    timeKeeper("Turning light of ", writeFile, " ")
    lampControl.lightOff(tpLightIP)
    timeKeeper("Avacom Horizontal Pan ", writeFile, "Beginning")
    AvacomControl.avacomHorizPan(browser,5)   
    timeKeeper("Avacom Horizontal Pan ", writeFile, "Ending") 
    timeKeeper("Avacom Vertical Pan ", writeFile, "Beginning")
    AvacomControl.avacomVertPan(browser,5)
    timeKeeper("Avacom Vertical Pan ", writeFile, "Ending")  
    
    #cameraThread.join()
    browser.close()
    timeKeeper("Enterprise After Hours", writeFile, "Ending")
#end enterpriseAfterHours

def scanEntAf(target):
    #accepts the IP of the device to scan
    entAfThread = threading.Thread(target = enterpriseAfterHours, args = ())
    #attackThread = threading.Thread(target=attacks.scanning, args = (target))
    entAfThread.start()
    timeKeeper(("Scan on " + str(target)), writeFile, " Beginning")
    attacks.scanning(target)
    #attackThread.start()
    #attackThread.join()
    timeKeeper("Scan", writeFile, "Ending")
    entAfThread.join()
    


#end scanEntAf()

def pingEntAf(target):
    #accepts the IP of the device to scan
    attackThread = threading.Thread(target=attacks.avacomPing, args = (str(avacomIP), str(target)))
    entAfThread = threading.Thread(target = enterpriseAfterHours, args = ())
    entAfThread.start()
    timeKeeper(("Ping Attack on " + str(target)), writeFile, "Beginning")
    attackThread.start()
    attackThread.join()
    entAfThread.join()
    timeKeeper("Ping Attack", writeFile, "Ending")

#end pingEntAf()
def DOSEntAf(target):
    #accepts the IP of the device to scan
    attackThread = threading.Thread(target=attacks.hPing3, args = (target, 5000, sudoPwd))
    entAfThread = threading.Thread(target = enterpriseAfterHours, args = ())
    entAfThread.start()
    timeKeeper(("DOS Attack on"  + str(target)), writeFile, "Beginning")
    attackThread.start()
    attackThread.join()
    entAfThread.join()
    timeKeeper("DOS Attack", writeFile, "Ending")

#end DOSEntAf()

def bruteForceEntAf(target, pwdFile):
    attackThread = threading.Thread(target = attacks.bruteForce, args = (target, pwdFile, sudoPwd))
    entAfThread = threading.Thread(target = enterpriseAfterHours, args = ())
    entAfThread.start()
    timeKeeper(("Brute Force Attack on"  + str(target)), writeFile, "Beginning")
    attackThread.start()
    attackThread.join()
    entAfThread.join()
    timeKeeper("Brute Force Attack", writeFile, "Ending") 
#end bruteForceEntAf



wakeUp()
time.sleep(20)

DOSWakeUp(computerIP)
time.sleep(20)

scanWakeUp(computerIP)
time.sleep(20)

pingWakeUp(computerIP)
time.sleep(20)

bruteForceWakeUp(computerIP,"pwds.txt")







