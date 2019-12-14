#CS2705
#IPv4 Address Manipulation
#Kyler Hansen

import ipaddress


#Question 1
ipInterface = ipaddress.ip_interface('192.168.2.76/28')
ipNetwork = ipInterface.network
print("1. Network address= {}".format(ipaddress.ip_network(ipNetwork).network_address))
print("1. The first usable address= {}".format((ipaddress.ip_network(ipNetwork).network_address)+1)) # +1 because you can't count the broadcast address.

print()

#Question 2
ipInterface = ipaddress.ip_interface('192.168.2.76/9')
ipNetwork = ipInterface.network
print("2. Network address= {}".format(ipaddress.ip_network(ipNetwork).network_address))
print("2. The first usable address= {}".format((ipaddress.ip_network(ipNetwork).network_address)+1)) 

print()

#Question 3
ipInterface = ipaddress.ip_interface('192.168.2.137/27')
ipNetwork = ipInterface.network
print("3. Network address= {}".format(ipaddress.ip_network(ipNetwork).network_address))
print("3. The first usable address= {}".format((ipaddress.ip_network(ipNetwork).network_address)+1)) 

print()

#Question 4
ipInterface = ipaddress.ip_interface('101.10.2.8/15')
ipNetwork = ipInterface.network
print("4. Total addresses= {}".format(ipaddress.ip_network(ipNetwork).num_addresses))
print("4. Usable addresses= {}".format((ipaddress.ip_network(ipNetwork).num_addresses)-2))

print()

#Question 5
ipInterface = ipaddress.ip_interface('101.10.2.8/29')
ipNetwork = ipInterface.network
print("5. Total addresses= {}".format(ipaddress.ip_network(ipNetwork).num_addresses))
print("5. Usable addresses= {}".format((ipaddress.ip_network(ipNetwork).num_addresses)-2))

print()

#Question 6
ipInterface = ipaddress.ip_interface('192.168.2.137/27')
ipNetwork = ipInterface.network
print("6. Broadcast address= {}".format(ipaddress.ip_network(ipNetwork).broadcast_address))
print("6. Last usable address= {}".format((ipaddress.ip_network(ipNetwork).broadcast_address)-1))

print()

#Question 7
ipInterface = ipaddress.ip_interface('110.10.2.55/30')
ipNetwork = ipInterface.network
print("7. Broadcast address= {}".format(ipaddress.ip_network(ipNetwork).broadcast_address))
print("7. Last usable address= {}".format((ipaddress.ip_network(ipNetwork).broadcast_address)-1))

print()

#Question 8
print("8. The subnet prefix length will need to be set to 4 because 2^4 = 16 and that would accomidate the needed 12 subnets plus 2 additional ones for broadcasting and network address.")

print()

#Question 9
ipInterface = ipaddress.ip_interface('110.10.10.64/25')
ipNetwork = ipInterface.network
print("9. ",2**28," subnets with {} addresses in each subnet".format(ipaddress.ip_network(ipNetwork).num_addresses)) #if the prefix length is 28 then its 2^28 subnets

print()

#Question 10
ipInterface = ipaddress.ip_interface('156.78.51.24/25')
ipNetwork = ipInterface.network
print("10. Total address= {}".format(ipaddress.ip_network(ipNetwork).num_addresses))

print()

#Question 11
ipInterface = ipaddress.ip_interface('156.78.51.24/30')
ipNetwork = ipInterface.network
print("11. Total address= {}".format(ipaddress.ip_network(ipNetwork).num_addresses))

print()

#Question 12
ipInterface = ipaddress.ip_interface('166.25.132.0/3')
ipNetwork = ipInterface.network
print("12. Total address= {}".format(ipaddress.ip_network(ipNetwork).num_addresses))

print()
