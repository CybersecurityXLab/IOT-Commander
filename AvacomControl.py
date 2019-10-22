"""
This program attempts to modularize IOTCommander into reusable modules for usage scenarios.  

Thomas Setzler
"""

import os,subprocess,random,time,datetime,sys,telnetlib
from selenium import webdriver
from playsound import playsound



"""  AVACOM Webcam Modules"""

def telnetIntoAvacom():
    #Code from IOT Commander
    #telnets into Avacom webcam
    #essential for any manipulation of the Avacom webcam    

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

def startWebcamCollection():
    #code from IOT Commander
    #collects lines from terminal during telnet session

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
    #code from IOT Commander
    #Removes colleted data from the camera
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
    #From IOT Commander
    #Download files from webcam

    username = 'admin'
    password = '1234'
    ip = '192.168.1.116'
    timestr = time.strftime("%Y-%m-%d_%H:%M:%S")

    print("Downloading Files")

    subprocess.call('wget -O ' + mainFolder + timestr + '_ps_data_webcam' + '.txt --user ' + username + ' --password ' + password + ' ' + ip + '/ps_data_webcam.txt', shell=True)
    time.sleep(1)
    subprocess.call('wget -O ' + mainFolder + timestr + '_top_data_webcam' + '.txt --user ' + username + ' --password ' + password + ' ' + ip + '/top_data_webcam.txt', shell=True)
    time.sleep(1)
    subprocess.call('wget -O ' + mainFolder + timestr + '_date_data_webcam' + '.txt --user ' + username + ' --password ' + password + ' ' + ip + '/date_data_webcam.txt', shell=True)
    time.sleep(1)
    subprocess.call('wget -O ' + mainFolder + timestr +'_netstat_data_webcam' + '.txt --user ' + username + ' --password ' + password + ' ' + ip + '/netstat_data_webcam.txt', shell=True)

def accessAvacomWebPortal():
    #From IOT Commander
    #Initates access to the Avacon portal for control of the webcam

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
    #From IOT Commander
    
    #Direct camera movement using directional buttons on website
    xpath = '//*[@title=' + direction + ']'
    button = driver.find_element_by_xpath(xpath)

    for clicks in range (numClicks):
        button.click()
    
    time.sleep(10)



