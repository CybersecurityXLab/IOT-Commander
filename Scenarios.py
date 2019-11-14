"""
This program uses the modules to run scenarios.
Dependencies:
    All modules imported below are required.  All required modules can be located on the same gitHub as the scenarios

"""




import audioPlayer, lampControl, utilities,AvacomControl,attacks #required modules
import time # needed to sleep between commands
import threading # needed to operate lamp with other devices


"""
LOCAL VARIABLES: will need to be updated per device

"""
sudoPwd = "N@chos4life"  # local password to utilize sudo


tpLightIP = "10.0.0.4"  #ip of the tp link lamp
avacomIP= "10.0.0.11"   #ip of the avacom webcam
ghIP = "10.0.0.10"      #ip of the google home

"""
    Wake Up Scenarios
**********************************************************************************************************
"""

def wakeUp():
 
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
    
#end wakeUp

def DOSWakeUp(target):
    #accepts the IP of the device to attack
    dosThread = threading.Thread(target=attacks.hPing3, args = (target, 5000, sudoPwd))
    wakeThread = threading.Thread(target = wakeUp, args = ())
    wakeThread.start()
    dosThread.start()
    dosThread.join()
    wakeThread.join()
#end DOSWakeUp()

def PingWakeUp(target,size,count):
    #accepts the IP of the device to attack, the size of the packet, and the number of attacks
    attackThread = threading.Thread(target=attacks.ping, args = (target, size, count))
    wakeThread = threading.Thread(target = wakeUp, args = ())
    wakeThread.start()
    attackTread.start()
    attackThread.join()
    wakeThread.join()
#end PingWakeUp()

def scanWakeUp(target):
    #accepts the IP of the device to scan
    attackThread = threading.Thread(target=attacks.scan, args = (target))
    wakeThread = threading.Thread(target = wakeUp, args = ())
    wakeThread.start()
    attackTread.start()
    attackThread.join()
    wakeThread.join()
#end scanWakeUp()

"""
    House Party Scenarios
**********************************************************************************************************
"""
    

def houseParty():
    browser = AvacomControl.accessAvacomWebPortal()
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

    
#end houseParty

def scanHouseParty(target):
    #accepts the IP of the device to scan
    attackThread = threading.Thread(target=attacks.scan, args = (target))
    housePartyThread = threading.Thread(target = houseParty, args = ())
    houseParty.start()
    attackTread.start()
    attackThread.join()
    houseParty.join()

#end scanHouseParty()

def pingHouseParty(target, size, count):
    #accepts the IP of the device to ping
    attackThread = threading.Thread(target=attacks.ping, args = (target, size, count))
    housePartyThread = threading.Thread(target = houseParty, args = ())
    houseParty.start()
    attackTread.start()
    attackThread.join()
    houseParty.join()

#end pingHouseParty()
def DOSHouseParty(target):
    #accepts the IP of the device to DOS
    attackThread = threading.Thread(target=attacks.hPing3, args = (target, 5000, sudoPwd))
    housePartyThread = threading.Thread(target = houseParty, args = ())
    houseParty.start()
    attackTread.start()
    attackThread.join()
    houseParty.join()

#end DOSHouseParty()


"""
    Enterprise Normal Business Hours Scenarios
**********************************************************************************************************
"""

def enterpriseNormalHours():
    browser = AvacomControl.accessAvacomWebPortal(avacomIP)
    time.sleep(10)
    AvacomControl.avacomHorizPan(browser, 2)
    browser.close()

#end enterpriseNormalHours

def scanEntNH(target):
    #accepts the IP of the device to scan
    attackThread = threading.Thread(target=attacks.scan, args = (target))
    entNHThread = threading.Thread(target = enterpriseNormalHours, args = ())
    entNHThread.start()
    attackTread.start()
    attackThread.join()
    entNHThread.join()

#end scaneEntNH()

def pingEntNH(target, size, count):
    #accepts the IP of the device to scan
    attackThread = threading.Thread(target=attacks.ping, args = (target, size, count))
    entNHThread = threading.Thread(target = enterpriseNormalHours, args = ())
    entNHThread.start()
    attackTread.start()
    attackThread.join()
    entNHThread.join()

#end pingEntNH()
def DOSEntNH(target):
    #accepts the IP of the device to scan
    attackThread = threading.Thread(target=attacks.hPing3, args = (target, 5000, sudoPwd))
    entNHThread = threading.Thread(target = enterpriseNormalHours, args = ())
    entNHThread.start()
    attackTread.start()
    attackThread.join()
    entNHThread.join()

#end DOSEntNH()

"""
    Enterprise After Hours Scenarios
**********************************************************************************************************
"""

def enterpriseAfterHours():
    #Browser setup
    browser = AvacomControl.accessAvacomWebPortal(avacomIP)
    time.sleep(10)
    
    #cameraThread = threading.Thread(target = AvacomControl.avacomHorizPan, args = (avacomIP, 10))
    #cameraThread.start()
    lampControl.lightOff(tpLightIP)
    AvacomControl.avacomHorizPan(browser,5)    
    
    #cameraThread.join()
    browser.close()
    
#end enterpriseAfterHours

def scanEntAf(target):
    #accepts the IP of the device to scan
    attackThread = threading.Thread(target=attacks.scan, args = (target))
    entAfThread = threading.Thread(target = enterpriseAfterHours, args = ())
    entAfThread.start()
    attackTread.start()
    attackThread.join()
    entAfThread.join()


#end scanEntAf()

def pingEntAf(target, size, count):
    #accepts the IP of the device to scan
    attackThread = threading.Thread(target=attacks.ping, args = (target, size, count))
    entAfThread = threading.Thread(target = enterpriseAfterHours, args = ())
    entAfThread.start()
    attackTread.start()
    attackThread.join()
    entAfThread.join()

#end pingEntAf()
def DOSEntAf(target):
    #accepts the IP of the device to scan
    attackThread = threading.Thread(target=attacks.hPing3, args = (target, 5000, sudoPwd))
    entAfThread = threading.Thread(target = enterpriseAfterHours, args = ())
    entAfThread.start()
    attackTread.start()
    attackThread.join()
    entAfThread.join()

#end DOSEntAf()






