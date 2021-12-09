#This code and the hostname txt file need to be in the same directory for this to work.
#python grabIPs.py

import socket
import os

def grabIP():

    #Counts the Number of Total Hostnames Inputted & Offline Hosts
    offline = 0
    count = 0
    
    #Opens the Input File & Creates an Output File
    file = open("hostnames.txt", "r") 
    output = open("IPs.txt", "w")
    off = open("offlineHosts.txt", "w")
    lines = file.readlines()
    
    #Reads each line and strips out the unnecessary extra lines between Hostnames
    for line in lines:
        line = line.strip()
        if line=='' or line=="/n":
            pass
        else:
            #Attemps to grab the IP address
            try:
                x = socket.gethostbyname(line)
                if count > 0:
                    output.write(", " + x)
                    count += 1
                else:
                    output.write(x)
                    count += 1
            #If the grab is unsuccessful, it will add to the offline counter as well as write it to the off.txt file
            except:
                off.write(line)
                offline += 1
                count += 1
    
    print("Total Number of Hosts Inputted = " + str(count))
    print("Number of Offline = " + str(offline))	
    print("IPs are located in IPs.txt file")
    print("Offline Hosts are located in the offlineHosts.txt")
    
    #Close each file used
    file.close()
    output.close()
    off.close()
	
grabIP()