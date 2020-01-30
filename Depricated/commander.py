#!/usr/bin/python
import os,subprocess,random,time, datetime

global username
global password
global switch
global ctrl
global monitor
global option
global layer1
global layer2
global attacker
global victim
global trafficgenerator
global expROC

version = "R7"
username = "MvTYGvuzpW2QTnY"
password = "E5Yf6m5FpVuwNFA"
commanderIP = "172.17.12.9"
switch = {'1':'172.17.12.16','2':'172.17.3.9','3':'172.17.11.11','B':'172.17.12.1'}
ctrl = {'1':'172.17.12.6','2':'172.17.3.2','3':'172.17.11.1','B':'172.17.12.9'}
monitor = {'1':'172.17.12.10','2':'172.17.3.3','3':'172.17.11.3','B':'172.17.12.11'}
node = {'N11':'172.17.12.12','N12':'172.17.12.13','N13':'172.17.12.14','N14':'172.17.11.4','N15':'172.17.12.15','N21':'172.17.3.4','N22':'172.17.3.5','N23':'172.17.3.6','N24':'172.17.3.7','N25':'172.17.3.8','N31':'172.17.11.5','N32':'172.17.11.6','N33':'172.17.11.8','N34':'172.17.11.9','N35':'172.17.11.10'}
attacker = []
victim = "No Victim Selected"
trafficgenerator = []
maxDuration = "0"
minDuration = "0"
maxNormDuration = "0"
minNormDuration = "0"
maxDurationExp = "0"
numBurst = "0"
expROC = "N"

def root():	
	option = 'A'
	os.system('clear')
	print("Welcome to Commander.py\nVersion: " + version + "\nPlease select an option below to start.\n")
	while option != 'Q':
		print("\n(1) Configure Network\n(2) Run Experiment\n(3) Update Topology Scripts\n(Q) Quit\n")
		option = raw_input("> Enter Option: ")
		option = option.upper().strip()
				
		if option == '1':
			layer1()
		elif option == '2':
			experiment_L1()
		elif option == '3':
			updater()
		elif option =='417':
			for x in node:
				print (x)
				subprocess.call('sshpass -p \'' + password + '\' ssh ' + username + '@' + node[x] + ' \'echo ' + password + ' | sudo -S apt-get install screen -y\' > /dev/null',shell=True)
		elif option == 'Q':
			print("Good Bye...")
			break
		else:
			next

def layer1():
	layer1 = 'A'
	while layer1 != 'Q':		
		layer1 = raw_input("\n>> Select Network (1,2,3,B), (A)ll, or (Q)uit: ")
		layer1 = layer1.upper()		
		if layer1 == 'Q':
			next
		elif layer1 == '1' or layer1 == '2' or layer1 == '3' or layer1 == 'A' or layer1 == 'B':
			layer2(layer1)
		else:
			next
def layer2(fromLayer1):
	layer2 = 'A'
	while layer2 != 'Q':
		print("\n(1) Start Network Services\n(2) Stop Network Services\n(3) Restart Network Services\n(Q) Quit")
		layer2 = raw_input(">>N-" + str(fromLayer1) + "> Select Option: ")
		layer2 = layer2.upper()
		if layer2 == '1':
			if fromLayer1 == 'A':
				for x in range(1,4):
					network_enable(str(x))
				# network_enable("B")
			else:
				network_enable(fromLayer1)
		elif layer2 == '2':
			if fromLayer1 == 'A':
				for x in range(1,4):
					network_disable(str(x))
				# network_disable("B")
			else:
				network_disable(fromLayer1)			
		elif layer2 == '3':
			if fromLayer1 == 'A':			
				for x in range(1,4):
					network_restart(str(x))
				# network_restart("B")
			else:
				network_restart(fromLayer1)
		else:
			next			
def network_enable(netid):
#Controller	
	# Enable Pox Controller
	subprocess.call('sshpass -p \'' + password + '\' ssh ' + username + '@' + ctrl[netid] + ' \'cd /opt/pox; screen -d -m python pox.py --verbose forwarding.l2_learning > /dev/null\'', shell=True)
	print("Pox Started...")
#Monitor
	# Enable snortStart and Experiment_1 Script
	#subprocess.call('sshpass -p \'' + password + '\' ssh ' + username + '@' + monitor[netid] + ' \'cd /opt/; echo ' + password + ' | sudo -S screen -d -m ./snortStart\'', shell=True)		
	# Changed snort to run via service command 27-DEC-2014 TC
	subprocess.call('sshpass -p \'' + password + '\' ssh ' + username + '@' + monitor[netid] + ' \'echo ' + password + ' | sudo -S service snort start > /dev/null\'', shell=True)
	print("Snort Started...")
	subprocess.call('sshpass -p \'' + password + '\' ssh ' + username + '@' + monitor[netid] + ' \'cd /opt/; echo ' + password + ' | sudo -S screen -d -m ./experiment_1.sh > /dev/null\'', shell=True)		
	print("Experiment_1 Started...")
#Switch
	# Enable Experiment_2 Script
	subprocess.call('sshpass -p \'' + password + '\' ssh ' + username + '@' + switch[netid] + ' \'echo ' + password + ' | sudo -S service openvswitch-switch start > /dev/null\'', shell=True)
	subprocess.call('sshpass -p \'' + password + '\' ssh ' + username + '@' + switch[netid] + ' \'cd /opt/; echo ' + password + ' | sudo -S screen -d -m bash experiment_2.sh > /dev/null\'', shell=True)	
	print("Experiment_2 Started...")
#Controller	
	# Enable Python_2 Script
	subprocess.call('sshpass -p \'' + password + '\' ssh ' + username + '@' + ctrl[netid] + ' \'cd /opt; echo ' + password + ' | sudo -S screen -d -m python python_2_first.py > /dev/null\'', shell=True)	
	print("Python_2 Started...")
#Monitor
	# Enable Python_1 Script
	subprocess.call('sshpass -p \'' + password + '\' ssh ' + username + '@' + monitor[netid] + ' \'cd /opt/; echo ' + password + ' | sudo -S screen -d -m python python_1.py > /dev/null\'', shell=True)	
	print("Python_1 Started...")

def network_disable(netid):
#Controller
	# Kill Previous Pox Controller
	subprocess.call('sshpass -p \'' + password + '\' ssh ' + username + '@' + ctrl[netid] + ' \'echo ' + password + ' | sudo -S killall python; echo ' + password + ' | sudo -S killall screen > /dev/null\'', shell=True)
	print("Killing Controller Services...")
#Monitor	
	# Kill bash script and python
	subprocess.call('sshpass -p \'' + password + '\' ssh ' + username + '@' + monitor[netid] + ' \'echo ' + password + ' | sudo -S killall python; echo ' + password + ' | sudo -S killall /bin/sh; echo ' + password + ' | sudo -S killall screen > /dev/null\'', shell=True)	
	subprocess.call('sshpass -p \'' + password + '\' ssh ' + username + '@' + monitor[netid] + ' \'echo ' + password + ' | sudo -S service snort stop > /dev/null\'', shell=True)
	print("Killing Monitor Services...")
#Switch
	# Kill all bash scripts and ovs services	
	subprocess.call('sshpass -p \'' + password + '\' ssh ' + username + '@' + switch[netid] + ' \'echo ' + password + ' | sudo -S service openvswitch-switch stop > /dev/null\'', shell=True)
	subprocess.call('sshpass -p \'' + password + '\' ssh ' + username + '@' + switch[netid] + ' \'echo ' + password + ' | sudo -S killall /bin/sh; echo ' + password + ' | sudo -S killall -r ovs*; echo ' + password + ' | sudo -S killall screen > /dev/null\'', shell=True)
	print("Killing Switch Services...")	
	#for x in node:
	#	subprocess.call('sshpass -p \'' + password + '\' ssh ' + username + '@' + node[x] + ' \'echo ' + password + ' | sudo -S killall screen > /dev/null; echo ' + password + ' | sudo -S killall iperf > /dev/null; echo ' + password + ' | sudo -S ifconfig eth1 down; echo ' + password + ' | sudo -S ifconfig eth1 up;\'', shell=True)
def network_restart(netid):
	network_disable(netid)
	network_enable(netid)
def experiment_L1():
	expL1 = 'A'
	while expL1 != 'Q':
		print("\n(1) Set Attacker\n(2) Set Victim\n(3) Set Traffic Generator\n(P) Display Experiment Configuration\n(C) Configure Experiment Duration\n(S) Enable Special Experiment Features\n(R) Execute Experiment\n(D) Deterministic Experiment\n(Q) Quit\n")	
		expL1 = raw_input(">> Enter Option: ")
		expL1 = expL1.upper().strip()
		if expL1 == '1':
			confAtk()
		elif expL1 == '2':
			confVic()
		elif expL1 == '3':
			confTraf()
		elif expL1 == 'C':
			configExp()
		elif expL1 == 'P':
			expPrint()
		elif expL1 == 'R':
			runExp()
		elif expL1 == 'S':
			runSet()
		elif expL1 == 'D':
			determExp()
		elif expL1 == 'Q':
			break
		else:
			next

def expPrint():
	print("Attacker: ")
	for x in attacker:
		print("\t" + x)
	print("Victim: " + victim)
	print("Traffic Generator: ")
	for x in trafficgenerator:
		print("\t" + x)
	print("\nExperiment Configuration:")
	print("Max Bust/Attack Traffic: " + maxDuration + " Seconds")
	print("Min Bust/Attack Traffic: " + minDuration + " Seconds")
	print("Max Normal Traffic: " + maxNormDuration + " Seconds")
	print("Min Normal Traffic: " + minNormDuration + " Seconds")
	print("Experiment Duration: " + maxDurationExp + " Seconds")
	print("Number of Burst/Attack Traffic: " + str(numBurst))
	
def updater():
	#for network in ctrl:
	#	network_disable(network)
	#print("Network Disabled...")
	os.system("service apache2 restart")		
	for ip in monitor:
		subprocess.call('sshpass -p \'' + password + '\' ssh ' + username + '@' + monitor[ip] + ' \'cd /opt; echo ' + password + ' | sudo -S wget -N http://' + commanderIP + '/experiment_1.sh > /dev/null\'', shell=True)		
		subprocess.call('sshpass -p \'' + password + '\' ssh ' + username + '@' + monitor[ip] + ' \'cd /opt; echo ' + password + ' | sudo -S wget -N http://' + commanderIP + '/python_1.py > /dev/null\'', shell=True)
		subprocess.call('sshpass -p \'' + password + '\' ssh ' + username + '@' + monitor[ip] + ' \'cd /opt; echo ' + password + ' | sudo -S wget -N http://' + commanderIP + '/snortStart > /dev/null\'', shell=True)
		print("Monitor " + ip + "...Updated!")
	for ip in ctrl:
		subprocess.call('sshpass -p \'' + password + '\' ssh ' + username + '@' + ctrl[ip] + ' \'cd /opt; echo ' + password + ' | sudo -S wget -N http://' + commanderIP + '/python_2_first.py > /dev/null\'', shell=True)
		print("Controller " + ip + "...Updated!")		
	for ip in switch:	
		subprocess.call('sshpass -p \'' + password + '\' ssh ' + username + '@' + switch[ip] + ' \'cd /opt; echo ' + password + ' | sudo -S wget -N http://' + commanderIP + '/experiment_2.sh > /dev/null\'', shell=True)
		print("Switch " + ip + "...Updated!")
	#for network in ctrl:
	#	network_enable(network)	
	print("")
def clientPtr():
		n = 1
		print("\nClients:\n")
		for x in range(1,4):
			print("N" + str(x) + str(y) + " : " + node["N" + str(x) + str(y)] + "\t"),
			n = n + 1
		print("")
def confAtk():
	clientPtr()
	print("\nAttackers:\n")
	for x in attacker:
		print(x + "\t")
	option = raw_input(">> Enter Attackers by Name Separated by Space (e.g. N11 N12 N13), (C)lear or (Q)uit: ")
	option = option.upper().strip()
	if option == "C":
		del attacker[:]
	elif option == "Q":
		return		
	else:
		for x in option.split():
			if x not in attacker and x not in trafficgenerator and x != victim and x in node:
				attacker.append(x)
			else:
				if x in attacker:
					print("\nNode " + str(x) + " Already Configured as an Attacker")
				elif x in trafficgenerator:
					print("\nNode " + str(x) + " Already Configured as a Traffic Generator")
				elif x == victim:
					print("\nNode " + str(x) + " Already Configured as a Victim")
				if x not in node:
					print("Invalid Node Entry " + str(x))
def confVic():
	clientPtr()
	print("\nVictim:\n")
	print(victim + "\n")
	option = raw_input(">> Enter Victim by Name (e.g. N11) or (Q)uit: ")	
	option = option.upper().strip()
	if option == "Q":
		return
	elif option not in attacker and option not in trafficgenerator and option in node:
		print (option)
		global victim
		victim = option
	else:
		if option in attacker:
			print("Node " + option + " Currently Set as an Attacker")
		elif option in trafficgenerator:
			print("Node " + option + " Currently Set as a Traffic Generator")
		else:
			print("Invalid Node Selection")		
def confTraf():
	clientPtr()
	print("\nTraffic Generator:\n")
	for x in trafficgenerator:
		print(x + "\t")
	option = raw_input(">> Enter Traffic Generator by Name Separated by Space (e.g. N11 N12 N13), (C)lear, or (Q)uit: ")
	option = option.upper().strip()
	if option == "C":
		del trafficgenerator[:]
	elif option == "Q":
		return
	else:
		for x in option.split():
			if x not in trafficgenerator and x in node and x not in attacker and x != victim:
				trafficgenerator.append(x)
			else:
				if x in attacker:
					print("\nNode " + str(x) + " Already Configured as an Attacker")
				elif x in trafficgenerator:
					print("\nNode " + str(x) + " Already Configured as a Traffic Generator")
				elif x == victim:
					print("\nNode " + str(x) + " Already Configured as a Victim")
				else:
					print("Invalid Node Entry " + str(x))
def configExp():
	global maxDuration
	global minDuration
	global maxNormDuration
	global minNormDuration
	global maxDurationExp
	global numBurst
	option = 'A'
	while option != 'Y':
		maxDuration = raw_input(">> Enter Maximum Duration in Seconds for Burst/Attack Traffic (int): ")
		minDuration = raw_input(">> Enter Minimal Duration in Seconds for Burst/Attack Traffic (int): ")
		maxNormDuration = raw_input(">> Enter Maximum Duration in Seconds for Normal Traffic (int): ")
		minNormDuration = raw_input(">> Enter Minimal Duration in Seconds for Normal Traffic (int): ")
		maxDurationExp = raw_input(">> Enter Duration of Entire Experiment in Seconds (int): ")
		numBurst = raw_input(">> Enter Number of Burst/Attack Traffic in Experiment (int): ")
		if int(minDuration) > int(maxDuration):
			print("Validating Configuration...Failed!")
			print("Incorrect Configuration, Min Burst/Traffic Duration Larger than Max")
			next
		elif int(minNormDuration) > int(maxNormDuration):
			print("Validating Configuration...Failed!")		
			print("Incorrect Configuration, Min Normal Duration Larger than Max")
			next
		else:
			print("Validating Configuration...Passed")		
			print("\nMax Burst/Attack Traffic: " + maxDuration + " Seconds")
			print("Min Burst/Attack Traffic: " + minDuration + " Seconds")
			print("Max Normal Traffic: " + maxNormDuration + " Seconds")
			print("Min Normal Traffic: " + minNormDuration + " Seconds")
			print("Experiment Duration: " + maxDurationExp + " Seconds")
			print("Number of Burst/Attack Traffic: " + numBurst)
			while option != 'Y' and option != 'N':
				option = raw_input(">> Is the Above Configuration Correct? (Y/N): ")
				option = option.upper().strip()
				if option != 'N' and option != 'Y':
					print("Invalid Option " + option)
				if option == 'Y':
					break
				if option == 'N':
					option = 'A'
					break
def runSet():
	key_entry = 0
	while key_entry != 1:
		print("Special Experiment Status:\nROC: " + expROC + "\n")
		expROC = raw_input(">> Enable ROC Experiment(Y/N): ")
		if expROC == "Y" or expROC == "N":
			key_entry = 1
		else:
			print("Invalid Input")
	key_entry = 0
	
def expROC():
	for x in trafficgenerator:
		subprocess.call('sshpass -p ' + password + ' ssh ' + username + '@' + node[x] + ' > /dev/null \'echo ' + password + ' | sudo -S screen -d -m ping -c 1' + victim + '\'', shell=True)
		
	for x in attacker:
		subprocess.call('sshpass -p ' + password + ' ssh ' + username + '@' + node[x] + ' > /dev/null \'echo ' + password + ' | sudo -S screen -d -m ping -c 1' + victim + '\'', shell=True)
		
def runExp():
	for x in range(1,4):
		network_restart(str(x))
	print("Running Experiments...")
	# Victim
	subprocess.call('sshpass -p ' + password + ' ssh ' + username + '@' + node[victim] + ' > /dev/null \'echo ' + password + ' | sudo -S screen -d -m iperf -s\'', shell=True)
	expTime = 0
	burst = 0
	global numBurst
	global maxDurationExp
	while int(expTime) < int(maxDurationExp):
		randNormDuration = random.randint(int(minNormDuration),int(maxNormDuration))
		# Normal Traffic
		for x in trafficgenerator:
			subprocess.call('sshpass -p ' + password + ' ssh ' + username + '@' + node[x] + ' > /dev/null \'echo ' + password + ' | sudo -S screen -d -m iperf -c ' + victim + ' -P 10 -t ' + str(randNormDuration) + ' -i 1 -f m\'', shell=True)
		#username = "MvTYGvuzpW2QTnY"
		#password = "E5Yf6m5FpVuwNFA"
		randDuration = random.randint(int(minDuration),int(maxDuration))
		if random.randint(1,2) == 1 and burst < numBurst:
			print("\033[1m" + "Sending Attack Traffic")
			#Attack			
			for x in attacker:
				subprocess.call('sshpass -p ' + password + ' ssh ' + username + '@' + node[x] + ' > /dev/null \'echo ' + password + ' | sudo -S screen -d -m timeout -sHUP ' + str(randDuration) + 's hping3 -i u1 -S --flood --rand-source -p 80 ' + victim + '\'', shell=True)
			time.sleep(randDuration)
		else:
			print("\033[1m" + "Sending Burst Traffic")
			for x in trafficgenerator:
				subprocess.call('sshpass -p ' + password + ' ssh ' + username + '@' + node[x] + ' > /dev/null \'echo ' + password + ' | sudo -S screen -d -m iperf -c ' + victim + ' -P 10 -t ' + str(randNormDuration) + ' -i 1 -f m\'', shell=True)
			time.sleep(randNormDuration)
		numBurst = int(numBurst) + 1
		expTime = expTime + randNormDuration + randDuration
		print("\033[1m" + "Current Experiment Time: " +  str(expTime) + "/" + str(maxDurationExp))
def determExp():
	for x in range(1,4):
		network_restart(str(x))
	# network_restart("B")
	i = 0
	atkDur = 120
	normDur = 120
	delay = 60
	minWaitDuration = 60
	maxWaitDuration = 180
	# after network restart need to add a delay so that mirroring starts working 30 - 60 secs
	time.sleep(delay)
	f = open('/opt/attacks_bursts.txt', 'a')
	while i < 38:
		# Attack Traffic
		attackNum = i + 100
		i = i + 1
		for x in attacker:
			print("Sending Burst Traffic..." + str(attackNum))
			f.write(str(attackNum) + '	' + str(datetime.datetime.now()) + '\n')
			# attack traffic
			#subprocess.call('sshpass -p ' + password + ' ssh ' + username + '@' + node[x] + ' > /dev/null \'echo ' + password + ' | sudo -S screen -d -m timeout -sHUP ' + str(atkDur) + 's hping3 -i u1 -S --flood --rand-source -p 80 ' + victim + ' -M ' + str(attackNum) + ' > /dev/null\'', shell=True)
			# burst traffic
			subprocess.call('sshpass -p ' + password + ' ssh ' + username + '@' + node[x] + ' > /dev/null \'echo ' + password + ' | sudo -S screen -d -m iperf -c ' + victim + ' -P 100 -t ' + str(normDur) + ' -i 1 -f m > /dev/null\'', shell=True)
			#Normal Traffic
			for x in trafficgenerator:
				subprocess.call('sshpass -p ' + password + ' ssh ' + username + '@' + node[x] + ' > /dev/null \'echo ' + password + ' | sudo -S screen -d -m iperf -c ' + victim + ' -P 10 -t ' + str(normDur) + ' -i 1 -f m > /dev/null\'', shell=True)
				print("Sending Normal Traffic...")
		randWaitDuration = random.randint(int(minWaitDuration),int(maxWaitDuration))
		time.sleep(randWaitDuration)
		
		for x in range(1,4):
			network_restart(str(x))
		randWaitDuration = random.randint(int(minWaitDuration),int(maxWaitDuration))
		time.sleep(randWaitDuration)
		
		# Burst Traffic
		#for x in trafficgenerator:
		#	subprocess.call('sshpass -p ' + password + ' ssh ' + username + '@' + node[x] + ' > /dev/null \'echo ' + password + ' | sudo -S screen -d -m ab -c 400 -n 400 http://' + victim + '/', shell=True)	
		#print("Iteration: " + str(i))
	f.close()
root()
