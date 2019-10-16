"""
This program plays prerecorded .wav files for use with IoT home assistants.
"""

fileLocation = "/home/thomas/Documents/IoTCommanderWIP/VoiceRecordings/" #location of file of WAVs
import os

def setFileLocation(path):
     fileLocation = path
#end setFileLocation



def playAudio(fileName):
    #This function will accept the name of the file, with a .wav extension, and play it
    #It assumes that the .wav file exists in the file location specified above
    
    os.system("aplay " + fileLocation + fileName)
    
    
#end playAudio()

    
"""
Google Home Methods
    *all have the prefix gh in method name
"""

def ghYoutubeOpen():
    #instructs google home to launch youtube
    playAudio("Google_youtube.wav")
#end ghYoutubeOpen
    
def ghYoutubeClose():
    #instructs google home to close youtube
    playAudio("Google_close_youtube.wav")
#end ghYoutubeClose()
    
def ghWeather():
    #instructs google home to search the weather
    playAudio("google_weather.wav")
#end ghWeather

def ghOutletOn():
    #instructs google home to turn on smart outlet
    playAudio("Google_Outlet_on.wav")
#end ghOutletOn

def ghOutletOff():
    #instructs google home to turn off smart outlet
    playAudio("Google_outlet_off.wav")
#end ghOutlettOff()

def ghLightOn():
    #instructs google home to turn on smart light
    playAudio("Google_light_on")
#end ghLightOn()

def ghLightOff():
    #instructs google home to turn off smart light
    playAudio("google_light_off")
#end ghLightOff()


"""
Echo Dot Methods
    *all have the prefix dot
"""
def dotGreece():
    #instructs echo dot to seach Greece
    playAudio("echo_dot_greece.wav")
#end dotGreece()

def dotGift():
    #instructs echo dot to respond to gift
    playAudio("Echo_dot_gift.wav")
#end dotGift()

"""
Amazon Echo Methods
    *all have prefix of comp
"""

def compWeather():
    #instructs echo to querry weather
    playAudio("echo_comp_weather.wav")
#end compWeather()

def compMusicOff():
    #instructs echo to stop playing music
    playAudio("Echo_comp_stop_music.wav")
#end compMusicOff()

def compMusicOn():
    #instructs echo to start playing music
    playAudio("Echo_comp_play_music.wav")
#end compMusicOn()

compWeather()

