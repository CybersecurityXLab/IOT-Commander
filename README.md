# IOT-Commander
CyberX Lab
College of Charleston

Carson Smart
Chase Myers
Thomas Setzler

Files:
	CoffeeCode/coffee: code for controlling the smart coffee pot from the creator's github
	AvacomControl.py:  modules to connect to, move, and otherwise control the avacom camera.  Methods are commented with instructions for use
	IOTCommander.py: refactored IOTCommander code of prior students to be more readable and useable.
	IOTCommanderOriginal.py: Original IOTCommander code
	Scenarios.py: module of every scenario, including attacks on scenarios.
	attacks.py: moudle of attacks used to attack devices.  Use instructions included in code comments
	audioPlayer.py: module for playing recorded instructions for the home assistants.  
	commander.py: antiquated version of IOTCommander
	lampControl.py: modules for controling TPLink lamp.  Instructions included in comments
	normalScenarios.py: antiquated version of Scenarios.py
	utilities.py: support functions for scenarios, instructions in comments

Scenarios:
	Wakeup(): turns light on, uses voice commands to get weather, open youtube, and turn on music
	houseParty(): connects and turns the webcam, plays music, connects to youtube, and strobes the light
	EnterpriseNormalHours(): connects and turns webcam, will be expanded with more voice commands
	EnterpriseAfterHours(): connects and turns webcam, turns off light, will later deploy home assistant

Attack Scenarios:
Each scenario has an attack scenario created for it.  The attack scenarios utilize multithreading to perform the attacks simultaniously with the scenarios.
	DOS: performs a denial of service attack on a specified IP
	Scan: scans the specified IP
	ping: launches a customizeable ping at specified IP

Current Issues:
Currently trying to connect to the avacom camera in quick succession will cause the connection to be refused.
