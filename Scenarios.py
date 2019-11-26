"""
This program uses the modules to run scenarios.
Dependencies:
    All modules imported below are required.  All required modules can be located on the same gitHub as the scenarios

"""




import audioPlayer, lampControl, utilities,AvacomControl,attacks #required modules
import time # needed to sleep between commands
import datetime
import threading # needed to operate lamp with other devices


"""
LOCAL VARIABLES: will need to be updated per device

"""
sudoPwd = "BajaB1@st"  # local password to utilize sudo


tpLightIP = "10.0.0.3"  #ip of the tp link lamp
avacomIP= "10.0.0.2"   #ip of the avacom webcam
ghIP = "10.0.0.8"      #ip of the google home


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
"""
    Wake Up Scenarios
**********************************************************************************************************
"""

def wakeUp():
    timeKeeper("WakeUp", writeFile, "Beginning")
    lampControl.lightOn(tpLightIP)
    time.sleep(5)
    audioPlayer.ghWeather()
    time.sleep(5)
    audioPlayer.compMusicOn()
    time.sleep(5)
    audioPlayer.ghYoutubeOpen()
    time.sleep(5)
    audioPlayer.compMusicOff()
    time.sleep(5)
    audioPlayer.ghYoutubeClose()
    time.sleep(5)
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

def pingWakeUp(target,size,count):
    #accepts the IP of the device to attack, the size of the packet, and the number of attacks
    attackThread = threading.Thread(target=attacks.ping, args = (target, size, count))
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
    attackThread = threading.Thread(target=attacks.scanning, args = (target))
    wakeThread = threading.Thread(target = wakeUp, args = ())
    wakeThread.start()
    timeKeeper("Scan", writeFile, "Beginning")
    attackThread.start()
    attackThread.join()
    wakeThread.join()
    timeKeeper("Scan", writeFile, "Ending")
#end scanWakeUp()

"""
    House Party Scenarios
**********************************************************************************************************
"""
    

def houseParty():
    timeKeeper("House Party", writeFile, "Beginning")
    browser = AvacomControl.accessAvacomWebPortal(avacomIP)
    time.sleep(10)
    lampThread= threading.Thread(target = lampControl.strobeLight, args=(tpLightIP,10))
    lampThread.start()
    
    audioPlayer.compMusicOn()
    time.sleep(5)
    audioPlayer.ghYoutubeOpen()
    time.sleep(5)

    AvacomControl.clickAvacomDirectionalButton(browser, "\"Right\"", 15)
    lampThread.join()


    time.sleep(5)
    audioPlayer.ghYoutubeClose()
    time.sleep(5)
    audioPlayer.compMusicOff()
    timeKeeper("House Party", writeFile, "Ending")
    
#end houseParty

def scanHouseParty(target):
    #accepts the IP of the device to scan
    attackThread = threading.Thread(target=attacks.scanning, args = (target))
    housePartyThread = threading.Thread(target = houseParty, args = ())
    houseParty.start()
    timeKeeper("Scan", writeFile, "Begining")
    attackThread.start()
    attackThread.join()
    houseParty.join()
    timeKeeper("Scan", writeFile, "Ending")
#end scanHouseParty()

def pingHouseParty(target, size, count):
    #accepts the IP of the device to ping
    attackThread = threading.Thread(target=attacks.ping, args = (target, size, count))
    housePartyThread = threading.Thread(target = houseParty, args = ())
    houseParty.start()
    timeKeeper("Ping Attack", writeFile, "Beginning")
    attackThread.start()
    attackThread.join()
    houseParty.join()
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


"""
    Enterprise Normal Business Hours Scenarios
**********************************************************************************************************
"""

def enterpriseNormalHours():
    timeKeeper("Enterprise Normal Businesss Hours", writeFile, "Begining")
    browser = AvacomControl.accessAvacomWebPortal(avacomIP)
    time.sleep(10)
    AvacomControl.avacomHorizPan(browser, 2)
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

def pingEntNH(target, size, count):
    #accepts the IP of the device to scan
    attackThread = threading.Thread(target=attacks.ping, args = (target, size, count))
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
    #Browser setup
    browser = AvacomControl.accessAvacomWebPortal(avacomIP)
    time.sleep(10)
    
    #cameraThread = threading.Thread(target = AvacomControl.avacomHorizPan, args = (avacomIP, 10))
    #cameraThread.start()
    lampControl.lightOff(tpLightIP)
    AvacomControl.avacomHorizPan(browser,5)    
    
    #cameraThread.join()
    browser.close()
    timeKeeper("Enterprise After Hours", writeFile, "Ending")
#end enterpriseAfterHours

def scanEntAf(target):
    #accepts the IP of the device to scan
    attackThread = threading.Thread(target=attacks.scanning, args = (target))
    entAfThread = threading.Thread(target = enterpriseAfterHours, args = ())
    entAfThread.start()
    timeKeeper("Scan", writeFile, "Beginning")
    attackThread.start()
    attackThread.join()
    entAfThread.join()
    timeKeeper("Scan", writeFile, "Ending")


#end scanEntAf()

def pingEntAf(target, size, count):
    #accepts the IP of the device to scan
    attackThread = threading.Thread(target=attacks.ping, args = (target, size, count))
    entAfThread = threading.Thread(target = enterpriseAfterHours, args = ())
    entAfThread.start()
    timeKeeper("Ping Attack", writeFile, "Beginning")
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
    timeKeeper("Ping Attack", writeFile, "Beginning")
    attackThread.start()
    attackThread.join()
    entAfThread.join()
    timeKeeper("Ping Attack", writeFile, "Ending")

#end DOSEntAf()



enterpriseAfterHours()

writeFile.close()




