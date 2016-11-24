import re
import requests

file_ips = [] 
uniqueIps = []
subNets = []
uniqueSubNets = []

logfile = open('access.log', 'r')
log = logfile.read()
file_ips = re.findall(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', log)

for ip in file_ips:
	if ip not in uniqueIps:
		uniqueIps.append(ip)

for ip in uniqueIps:
	subNets.append(re.findall(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}',ip))
    
for ip in subNets:
	if ip not in uniqueSubNets:
		uniqueSubNets.append(ip)

for subip in uniqueSubNets:
	print ("Subnet: ", subip)
	ipCount = 0
	print("Addresses:")
	for ip in uniqueIps:
		if re.findall(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', ip) == subip:
			print(ip)
			ipCount = ipCount + 1
	print('Count: ' + str(ipCount) + '\r\n')