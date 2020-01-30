#!/usr/bin/python
#telnet code based from example on https://docs.python.org/2/library/telnetlib.html

import os,subprocess,random,time,datetime,sys,telnetlib
from selenium import webdriver
from playsound import playsound

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

    subprocess.call('wget -O ' + mainFolder + timestr + '_ps_data_webcam' + '.txt --user ' + username + ' --password ' + password + ' ' + ip + '/ps_data_webcam.txt', shell=True)
    time.sleep(1)
    subprocess.call('wget -O ' + mainFolder + timestr + '_top_data_webcam' + '.txt --user ' + username + ' --password ' + password + ' ' + ip + '/top_data_webcam.txt', shell=True)
    time.sleep(1)
    subprocess.call('wget -O ' + mainFolder + timestr + '_date_data_webcam' + '.txt --user ' + username + ' --password ' + password + ' ' + ip + '/date_data_webcam.txt', shell=True)
    time.sleep(1)
    subprocess.call('wget -O ' + mainFolder + timestr +'_netstat_data_webcam' + '.txt --user ' + username + ' --password ' + password + ' ' + ip + '/netstat_data_webcam.txt', shell=True)

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
    time.sleep(10)

    #Access website, go to show live video
    currentDT = datetime.datetime.now()
    f.write(str(currentDT) + " - Enterprise Diligent: Accessing Web Portal\n" )
    browser = accessAvacomWebPortal()

    #Wait 60 seconds
    time.sleep (10)

    #Direct Movement, each direction takes 10 seconds
    currentDT = datetime.datetime.now()
    #f= open("enterpriseDiligent_" + str(currentDT) + ".txt","w+")
    f.write(str(currentDT) + " - Enterprise Diligent: Moving camera now\n" )

    clickAvacomDirectionalButton(browser,"\"Left\"", 50)
    clickAvacomDirectionalButton(browser,"\"Right\"", 50)
    clickAvacomDirectionalButton(browser,"\"Up\"", 50)
    clickAvacomDirectionalButton(browser,"\"Down\"", 50)
    clickAvacomDirectionalButton(browser,"\"Left\"", 50)
    clickAvacomDirectionalButton(browser,"\"Right\"", 50)
    currentDT = datetime.datetime.now()
    f.write(str(currentDT) + " - Enterprise Diligent: End camera movement\n")

    #Wait 30 seconds
    time.sleep(10)

    browser.close()
    
def enterpriseLazy():
    print("Starting Enterprise Lazy Scenario")
    currentDT = datetime.datetime.now()
    print (str(currentDT))

    #Sleep for 2 minutes
    time.sleep(120)

    #Access website, go to show live video
    currentDT = datetime.datetime.now()
    f.write(str(currentDT) + " - Enterprise Lazy: Accessing Web Portal\n" )
    browser = accessAvacomWebPortal()

    #Wait 10 seconds 
    time.sleep (10) 

    #Direct Movement for 10 seconds
    currentDT = datetime.datetime.now()
    f.write(str(currentDT) + " - Enterprise Lazy: Moving camera now\n" )
    clickAvacomDirectionalButton(browser,"\"Left\"", 25)
    clickAvacomDirectionalButton(browser,"\"Right\"", 25)
    currentDT = datetime.datetime.now()
    f.write(str(currentDT) + " - Enterprise Lazy: End camera movement\n")


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
    currentDT = datetime.datetime.now()
    f.write(str(currentDT) + " - Enterprise Normal: Accessing Web Portal\n" )
    browser = accessAvacomWebPortal()

    #Wait 30 seconds 
    time.sleep (30) 

    #Direct Movement for 15 seconds
    currentDT = datetime.datetime.now()
    f.write(str(currentDT) + " - Enterprise Normal: Moving camera now\n" )
    clickAvacomDirectionalButton(browser,"\"Left\"", 25)
    clickAvacomDirectionalButton(browser,"\"Right\"", 25)
    clickAvacomDirectionalButton(browser,"\"Left\"", 25) 
    currentDT = datetime.datetime.now()
    f.write(str(currentDT) + " - Enterprise Normal: End Camera MOvement\n" )

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
        currentDT = datetime.datetime.now()
        f.write(str(currentDT) + " - Home Vacation: Accessing Web Portal\n" )
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
        currentDT = datetime.datetime.now()
        f.write(str(currentDT) + " - Home Weekday: Accessing Web Portal\n" )
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
    currentDT = datetime.datetime.now()
    f.write(str(currentDT) + " - Home Weekend: Accessing Web Portal\n" )
    browser = accessAvacomWebPortal()

    #Wait 10 seconds 
    time.sleep (10) 


    browser.close()
   
def infrastructure():
    print("Starting Infrastructure Scenario")
    currentDT = datetime.datetime.now()
    print (str(currentDT))

    for i in range (2):
        #Access website, go to show live video
        currentDT = datetime.datetime.now()
        f.write(str(currentDT) + " - Infrastructure: Accessing Web Portal\n" )
        browser = accessAvacomWebPortal()

        if i == 0:
            time.sleep (8)  
        else:
            time.sleep (7) 

        browser.close()

        if i == 0:
            time.sleep (52)


def hPing3():
    print("Starting Hping3 Attack Scenario")
    currentDT = datetime.datetime.now()
    print (str(currentDT))

    time.sleep(150)
    currentDT = datetime.datetime.now()
    f.write(str(currentDT) + " - hPing3: Accessing Web Portal\n" )
    browser = accessAvacomWebPortal()

    time.sleep(30)
    currentDT = datetime.datetime.now()
    f.write(str(currentDT) + " - hPing3: Starting Attack\n" )
    sudoPassword = '&cyberXL@b2019' #password used to sign into computer being used to run IOTCommander.py
    command = 'hping3 -S -c 1000000 --faster 192.168.1.116'
    os.system('echo %s|sudo -S %s' % (sudoPassword, command))
    currentDT = datetime.datetime.now()
    f.write(str(currentDT) + " - hPing3: Attack Done\n" )

    time.sleep(60)

    browser.close()

def large_Ping():
    print("Starting Large_Ping Attack Scenario")
    currentDT = datetime.datetime.now()
    print (str(currentDT))

    time.sleep(150)
    currentDT = datetime.datetime.now()
    f.write(str(currentDT) + " - Large Ping: Accessing Web Portal\n" )
    browser = accessAvacomWebPortal()

    time.sleep(30)
    currentDT = datetime.datetime.now()
    f.write(str(currentDT) + " - Large Ping: Starting Attack\n" )
    os.system('ping -s 65507 -c 1 192.168.1.116')
    currentDT = datetime.datetime.now()
    f.write(str(currentDT) + " - Large Ping: Attack Done\n" )

    time.sleep(60)

    browser.close()

def ping_flood():
    print("Starting Ping_Flood Attack Scenario")
    currentDT = datetime.datetime.now()
    print (str(currentDT))

    time.sleep(150)
    currentDT = datetime.datetime.now()
    f.write(str(currentDT) + " - Ping Flood: Accessing Web Portal\n" )
    browser = accessAvacomWebPortal()

    time.sleep(30)
    currentDT = datetime.datetime.now()
    f.write(str(currentDT) + " - Ping Flood: Starting Attack\n" )
    os.system('ping -s 100 -c 50 192.168.1.116')
    currentDT = datetime.datetime.now()
    f.write(str(currentDT) + " - Ping Flood: Attack Done\n" )

    time.sleep(160)

    browser.close()

def scanning():
    print("Starting Scanning Attack Scenario")
    currentDT = datetime.datetime.now()
    print (str(currentDT))

    time.sleep(150)
    currentDT = datetime.datetime.now()
    f.write(str(currentDT) + " - Scanning Attack: Accessing Web Portal\n" )
    browser = accessAvacomWebPortal()

    time.sleep(30)
    currentDT = datetime.datetime.now()
    f.write(str(currentDT) + " - Scanning Attack: Starting Attack\n" )
    os.system('nmap -vv 192.168.1.116')
    currentDT = datetime.datetime.now()
    f.write(str(currentDT) + " - Scanning Attack: Attack Done\n" )

    time.sleep(60)

    browser.close()

def brute_force():
    print("Starting Brute_Force Attack Scenario")
    currentDT = datetime.datetime.now()
    print (str(currentDT))

    time.sleep(150)
    currentDT = datetime.datetime.now()
    f.write(str(currentDT) + " - Brute Force Attack: Accessing Web Portal\n" )
    browser = accessAvacomWebPortal()

    currentDT = datetime.datetime.now()
    f.write(str(currentDT) + " - Brute Force Attack: Starting Attack\n" )
    browser = accessAvacomWebPortal()
    sudoPassword = '&cyberXL@b2019' #password used to sign into computer being used to run IOTCommander.py
    command = 'hydra -l root -P rockyou.txt telnet://192.168.1.116'
    os.system('echo %s|sudo -S %s' % (sudoPassword, command))
    currentDT = datetime.datetime.now()
    f.write(str(currentDT) + " - Brute Force Attack: Attack Done\n" )

    time.sleep(60)
    browser.close()

def scenario1():
    enterpriseDiligent()
    playsound('VoiceRecordings/echo_comp_weather.wav')

    time.sleep(10)

    playsound('VoiceRecordings/echo_dot_greece.wav')

    time.sleep(9)

    playsound('VoiceRecordings/Google_youtube.wav')
    brute_force()

    time.sleep(50)

    playsound('VoiceRecordings/Google_light_on.wav')

    time.sleep(21)

    playsound('VoiceRecordings/Echo_comp_play_music.wav')

    time.sleep(15)

    playsound('VoiceRecordings/google_light_off.wav')

    time.sleep(60)

    enterpriseLazy()

    playsound('VoiceRecordings/Echo_comp_stop_music.wav')

    time.sleep(1)

    playsound('VoiceRecordings/Google_Outlet_on.wav')

    time.sleep(19)

    playsound('VoiceRecordings/Echo_dot_gift.wav')

    large_Ping()

    playsound('VoiceRecordings/Google_outlet_off.wav')



def main():
    global f #file for writing timestamps and actions into
    
    currentDT = datetime.datetime.now()
    f = open(str(currentDT) + "_Labels.txt","w+")
    


    for i in range (2):
        #clear system buffer
        os.system('clear')

        #location where webcam text files will be saved
        directory = "~/Documents/WebcamTest/"


        #ping router (used to show start and stop in packet capture)
        pingRouter()

        #start tcpdump on rasberry pi
        startTCPDumpOnPi()

        #start collection.sh script on webcam
        startWebcamCollectionOriginal()

        currentDT = datetime.datetime.now()

   
        scenario1()
        #randomly executes scenarios
        #scenarios = [enterpriseDiligent, enterpriseLazy, enterpriseNormal,homeVacation, homeWeekday, homeWeekend, infrastructure, hPing3, large_Ping, ping_flood, scanning, brute_force]
        #random.choice(scenarios)()

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

    
    #currentDT = datetime.datetime.now()
    #f.write(str(currentDT) + " - scenarios done\n" )
main()


