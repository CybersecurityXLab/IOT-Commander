# IOT-Commander
CyberX Lab
College of Charleston

Carson Smart
Chase Myers
Thomas Setzler

## Files:
* CoffeeCode/coffee: code for controlling the smart coffee pot from the creator's github
* AvacomControl.py:  modules to connect to, move, and otherwise control the avacom camera.  Methods are commented with instructions for use
* Scenarios.py: current module of every scenario, including attacks on scenarios.
* attacks.py: moudle of attacks used to attack devices.  Use instructions included in code comments
* audioPlayer.py: module for playing recorded instructions for the home assistants.  
* lampControl.py: modules for controling TPLink lamp.  Instructions included in comments
* packets.py: code to parse packet captures for tcp/udp connections using scapy
* portScanner.py: function to scan all ports in a provided list of IPs and output it to a single file


###### Depreciated Files:
* IOTCommander.py: refactored IOTCommander code of prior students to be more readable and useable.
* IOTCommanderOriginal.py: Original IOTCommander code
* commander.py: antiquated version of IOTCommander
* normalScenarios.py: antiquated version of Scenarios.py
* utilities.py: support functions for scenarios, instructions in comments

## Scenarios:
* Wakeup(): turns light on, uses voice commands to get weather, open youtube, and turn on music
* houseParty(): connects and turns the webcam, plays music, connects to youtube, and strobes the light
* EnterpriseNormalHours(): connects and turns webcam, will be expanded with more voice commands
* EnterpriseAfterHours(): connects and turns webcam, turns off light, will later deploy home assistant

## Attack Scenarios:
Each scenario has an attack scenario created for it.  The attack scenarios utilize multithreading to perform the attacks simultaniously with the scenarios.
* DOS: performs a denial of service attack on a specified IP
* Scan: scans the specified IP
* ping: launches a customizeable ping at specified IP
* avacomPing: launches a ping attack from the avacom camera to a target
* bruteforce: launches a password cracking attempt via hydra and a specified passwords file

## Known Issues:
Trying to connect to the avacom camera in rapid succession will cause the connection to be refused.
