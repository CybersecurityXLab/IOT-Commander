from scapy.all import *
import os

#Global Variables
homeRange = "192.168.1.100"


"""
testPacket = rdpcap("../IOT-Commander/Depricated/testJan28.pcap")
TCPcount = 0
UDPcount = 0

for packet in testPacket:
	if (packet.haslayer(IP)):
		source = packet.getlayer(IP).src
		dest = packet.getlayer(IP).dst
		print(source + " " + dest)
	if (packet.haslayer(TCP)):
		sp = packet.sport
		dp  = packet.dport
		TCPcount += 1

		print(str(sp) + " " + str(dp))
	if(TCPcount == 5):
		break


print (str(TCPcount) + " tcp packets")
print (str(UDPcount) + " udp packets")
"""

def ipRangeCheck(ip):
	"""
	This function accepts an IP address and tests if it is in the range of your local network
	"""
	
	periodCT = 0
	inhome = False
	for i in range(len(ip)):
		if (periodCT == 3):
			inhome = True
			break
		elif (str(ip[i]) == "."):
			periodCT += 1
		elif (homeRange[i] != str(ip[i])):
			inhome == False
			break
	return inhome

def ConnectionCounter(capture):
	"""
	This function returns the total number of inbound, outbound, and local TCP connections in a pcap
	"""
	outboundTCP = 0
	inboundTCP = 0
	localTCP = 0
	outboundUDP = 0
	inboundUDP = 0
	localUDP = 0
	for packet in capture:
		if (packet.haslayer(IP) and packet.haslayer(TCP)):
			source = packet.getlayer(IP).src
			dest = packet.getlayer(IP).dst
			sourceIn = ipRangeCheck(source)
			destIn = ipRangeCheck(dest)
			if (sourceIn and destIn):
				localTCP += 1
			elif (sourceIn):
				outboundTCP +=1
			elif (destIn):
				inboundTCP += 1
		elif (packet.haslayer(IP) and packet.haslayer(UDP)):
			source = packet.getlayer(IP).src
			dest = packet.getlayer(IP).dst
			sourceIn = ipRangeCheck(source)
			destIn = ipRangeCheck(dest)
			if (sourceIn and destIn):
				localUDP += 1
			elif (sourceIn):
				outboundUDP +=1
			elif (destIn):
				inboundUDP += 1


	return inboundTCP, outboundTCP, localTCP, inboundUDP, outboundUDP, localUDP


def main():
	packet = rdpcap("../IOT-Commander/Depricated/testJan28.pcap")
	inboundTCP, outboundTCP, localTCP, inboundUDP, outboundUDP, localUDP = ConnectionCounter(packet)
	print("inbound TCP: " + str(inboundTCP))
	print("outbound TCP: " + str(outboundTCP))
	print("local TCP: " + str(localTCP))
	print("inbound UDP: " + str(inboundUDP))
	print("outbound UDP: " + str(outboundUDP))
	print("local UDP: " + str(localUDP))
				


main()





