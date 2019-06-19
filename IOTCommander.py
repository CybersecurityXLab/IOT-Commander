#!/usr/bin/python
#telnet code based from example on https://docs.python.org/2/library/telnetlib.html

import os,subprocess,random,time,datetime,sys,telnetlib
from selenium import webdriver

def pingRouter():
    print ('Pinging Router')
    
    ip = '192.168.1.1'

    #pings router 5 times
    cmd = 'ping -c 5 ' + ip 
    subprocess.call(cmd, shell=True)

def startTCPDumpOnPi():
    print ('Starting SSH')
    
    username = 'pi'
    password = 'pinkbanana55'
    ip = '192.168.1.1'

    #Executes tcpDump_5Min.py on RPI wireless interface for 5 mins and saves pcap in the Documents/Packet_Captures directory
    cmd = 'python Documents/Code/tcpDump_5Min.py'
    subprocess.call('sshpass -p '+ password + ' ssh ' + username + '@' + ip + ' ' + cmd, shell=True)


def telnetIntoAvacom():
    print ('Starting Telnet')
    currentDT = datetime.datetime.now()
    print (str(currentDT))

    user = 'root'
    password = 'hslwificam'
    host = '192.168.1.116'

    #start telnet connection
    tn = telnetlib.Telnet(host)
    tn.read_until(b"login:")
    tn.write(user.encode("ascii")+ b"\n")

    if password:
        tn.read_until(b"Password:") 
        tn.write(password.encode("ascii")+b"\n")

    return tn


def startWebcamCollectionOriginal():

    tnet = telnetIntoAvacom()

    print ("Starting Collection Script")
    tnet.write(b"cd system \n")
    tnet.write(b"sh collection.sh & \n")
    tnet.write(b"exit\n")
    print("Collection Script Started")

    lines_to_read = 8 #lines to read from telnet session (equal to the number of commands + 5)
    for i in range(lines_to_read):
        line = tnet.read_until("\n")
        print(line)


def removeWebcamData():

    tnet = telnetIntoAvacom()

    print ("Removing Webcam Data")
    tnet.write(b"cd system/www \n")
    tnet.write(b"rm *webcam* \n")
    tnet.write(b"exit\n")
    print("Collection Script Started")

    lines_to_read = 8 #lines to read from telnet session (equal to the number of commands + 5)
    for i in range(lines_to_read):
        line = tnet.read_until("\n")
        print(line)
    

def downloadAvacomFiles(mainFolder):
    #Download files from webcam

    username = 'admin'
    password = '1234'
    ip = '192.168.1.116'
    timestr = time.strftime("%Y-%m-%d_%H:%M:%S")

    print("Downloading Files")

    subprocess.call('wget -O ' + mainFolder + 'ps_data_webcam_'+ timestr + '.txt --user ' + username + ' --password ' + password + ' ' + ip + '/ps_data_webcam.txt', shell=True)
    time.sleep(1)
    subprocess.call('wget -O ' + mainFolder + 'top_data_webcam_'+ timestr + '.txt --user ' + username + ' --password ' + password + ' ' + ip + '/top_data_webcam.txt', shell=True)
    time.sleep(1)
    subprocess.call('wget -O ' + mainFolder + 'date_data_webcam_'+ timestr + '.txt --user ' + username + ' --password ' + password + ' ' + ip + '/date_data_webcam.txt', shell=True)
    time.sleep(1)
    subprocess.call('wget -O ' + mainFolder + 'netstat_data_webcam_'+ timestr + '.txt --user ' + username + ' --password ' + password + ' ' + ip + '/netstat_data_webcam.txt', shell=True)

def accessAvacomWebPortal():
    #start web browser
    browser = webdriver.Chrome('/home/carson/Documents/Commander/IOT-Commander/chromedriver')

    #maximize window
    browser.maximize_window()

    #go to camera url
    browser.get('http://admin:1234@192.168.1.116/')
    time.sleep(1)

    #go to frame where buttons are located
    frame = browser.find_element_by_xpath('//*[@id="mainUrl"]')
    browser.switch_to_frame(frame)

    #the last 3 options have class 'cs5'
    cs5list = browser.find_elements_by_class_name('cs5')

    #pick the 2nd option which allows to view webcam without a plugin
    cs5list[2].click()
    return browser


def clickAvacomDirectionalButton(driver, direction, numClicks):

    #Direct camera movement using directional buttons on website
    xpath = '//*[@title=' + direction + ']'
    button = driver.find_element_by_xpath(xpath)

    for clicks in range (numClicks):
        button.click()
    
    time.sleep(10)


## SCENARIOS
def enterpriseDiligent():
    print("Starting Enterprise Diligent Scenario")
    currentDT = datetime.datetime.now()
    print (str(currentDT))

    #Sleep for 2 minutes
    time.sleep(120)

    #Access website, go to show live video
    browser = accessAvacomWebPortal()

    #Wait 60 seconds 
    time.sleep (60) 

    #Direct Movement, each direction takes 10 seconds
    clickAvacomDirectionalButton(browser,"\"Left\"", 50)
    clickAvacomDirectionalButton(browser,"\"Right\"", 50)
    clickAvacomDirectionalButton(browser,"\"Up\"", 50) 
    clickAvacomDirectionalButton(browser,"\"Down\"", 50)
    clickAvacomDirectionalButton(browser,"\"Left\"", 50)
    clickAvacomDirectionalButton(browser,"\"Right\"", 50)

    #Wait 30 seconds
    time.sleep(30)

    browser.close()
    
def enterpriseLazy():
    print("Starting Enterprise Lazy Scenario")
    currentDT = datetime.datetime.now()
    print (str(currentDT))

    #Sleep for 2 minutes
    time.sleep(120)

    #Access website, go to show live video
    browser = accessAvacomWebPortal()

    #Wait 10 seconds 
    time.sleep (10) 

    #Direct Movement for 10 seconds
    clickAvacomDirectionalButton(browser,"\"Left\"", 25)
    clickAvacomDirectionalButton(browser,"\"Right\"", 25)
  

    #Wait 10 seconds
    time.sleep(10)

    browser.close()

def enterpriseNormal():
    print("Starting Enterprise Normal Scenario")
    currentDT = datetime.datetime.now()
    print (str(currentDT))

    #Sleep for 2 minutes
    time.sleep(120)

    #Access website, go to show live video
    browser = accessAvacomWebPortal()

    #Wait 30 seconds 
    time.sleep (30) 

    #Direct Movement for 15 seconds
    clickAvacomDirectionalButton(browser,"\"Left\"", 25)
    clickAvacomDirectionalButton(browser,"\"Right\"", 25)
    clickAvacomDirectionalButton(browser,"\"Left\"", 25) 

    #Wait 15 seconds
    time.sleep(15)

    browser.close()

def homeVacation():
    print("Starting Home Vacation Scenario")
    currentDT = datetime.datetime.now()
    print (str(currentDT))

    #Sleep for 1 minute
    time.sleep(60)

    for i in range (3):
        #Access website, go to show live video
        browser = accessAvacomWebPortal()

        #Wait 15 seconds 
        time.sleep (15) 

        browser.close()

        #keeps browser open for speicifed times
        if i == 0:
            time.sleep (45)
        elif i == 1:
            time.sleep (105)

def homeWeekday():
    print("Starting Home Weekday Scenario")
    currentDT = datetime.datetime.now()
    print (str(currentDT))

    #Sleep for 1 minute
    time.sleep(60)

    for i in range (2):
        #Access website, go to show live video
        browser = accessAvacomWebPortal()

        #Wait 30 seconds 
        time.sleep (30) 

        browser.close()

        if i == 0:
            time.sleep (90)

def homeWeekend():
    print("Starting Home Weekend Scenario")
    currentDT = datetime.datetime.now()
    print (str(currentDT))

    #Sleep for 2 minutes
    time.sleep(120)

    
    #Access website, go to show live video
    browser = accessAvacomWebPortal()

    #Wait 10 seconds 
    time.sleep (10) 

    browser.close()

def infrastructure():
    print("Starting Infrastructure Scenario")
    currentDT = datetime.datetime.now()
    print (str(currentDT))

    #Sleep for 2 minutes
    time.sleep(120)

    
    for i in range (2):
        #Access website, go to show live video
        browser = accessAvacomWebPortal()

        if i == 0:
            time.sleep (8)  
        else:
            time.sleep (7) 

        browser.close()

        if i == 0:
            time.sleep (52)

def main():

    for i in range (20):    
        #clear system buffer
        os.system('clear')

        #location where webcam text files will be saved
        directory = '~/Documents/WebcamTest/'

#FIX ME
#Add time stamp method to log file to record start at stop

        #ping router (used to show start and stop in packet capture)
        pingRouter()

        #start collection.sh script on webcam
        startWebcamCollectionOriginal()
 
        #randomly executes scenarios
        scenarios = [enterpriseDiligent, enterpriseLazy, enterpriseNormal,homeVacation, homeWeekday, homeWeekend, infrastructure]
        random.choice(scenarios)()

        #executes twice to so that wget does not likely fail (it would be nice if there was a way to have wget retry if it fails automatically)
        downloadAvacomFiles(directory)
        downloadAvacomFiles(directory)

        #ping router (used to show start and stop in packet capture)
        pingRouter()

        #remove any webcam collection results from webcam
        removeWebcamData()
        print("Completed Round")

        #Waiting one minute before starting next scenario (should be changed once scenarios are programmed)
        time.sleep(60)       

    print("Experiment Completed")


main()


