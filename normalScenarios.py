"""
This program uses the modules to run scenarios.
Dependencies:
    All modules imported below are required.  All required modules can be located on the same gitHub as the scenarios

"""




import audioPlayer, lampControl, utilities,AvacomControl  #required modules
import time # needed to sleep between commands
import threading # needed to operate lamp with other devices
tpLightIP = "192.168.1.104"
timeFile = "../Data/scenarioTimestamps.txt"
sudoPwd = "N@chos4life"
avacomIP= "10.0.0.13"

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
    
#end wakeUp


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


def enterpriseNormalHours():
    browser = AvacomControl.accessAvacomWebPortal(avacomIP)
    time.sleep(10)
    #AvacomControl.avacomHorizPan(browser, 2)
    AvacomControl.avacomVertPan(browser,5)
    browser.close()
    



    







