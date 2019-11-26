"""
This program is compilation of various utiliy functions that will be used by the scenarios for gathering data.
"""
import datetime

def timeKeeper(moduleName,textFile, mode):
    #This functions accepts the name of the module, the name of the text file to write to, and whether the method started or ended and adds the start and end timestamps to a textfile for logging

    currentTime = datetime.datetime.now()
    #print(currentTime)    
    #O = open(textFile, "a+")
    output = str(moduleName) + " " + mode + " " + str(currentTime) + "\n"
    O.write(str(output))
    #O.close()
#end timeKeeper




