#! /bin/python/python3

import sys
import nmap
from urllib.request import urlopen, hashlib
import os
import sstfServer
scanner = nmap.PortScanner()


ip = ("")

#test is the class to test compatibility with the import function in Python

def test():
	print("Works!")

#portscan function is a port scanner built off of nmap. Takes an IP as input, stores string in variable ip

def portscan():	
	ip = input("Ip address:")
	print("Nmap Ver. ", scanner.nmap_version())
	scanner.scan(ip, "1-1000", " -Pn")
	print("IP status: ", scanner[ip].state())
	print("Open TCP Ports: ", scanner[ip].all_tcp())
	print("Open UDP Ports: ", scanner[ip].all_udp())
	print("Open IP Ports: ", scanner[ip].all_ip())

#exit the framework

def exit():
	sys.exit()

#WhatIsSSTF function prints a string. Its and "about" message.

def WhatIsSSTF():
	print("SSTF or SkSweetToothFramework is a framework built for the CyberPatriot event. It includes a SHA1 Password cracker, Port Scanner, and ST_RAT(W.I.P.)")

#ServerActions is a defined function that will be built on in later versions. Prints WIP message.


def Passcrack():
#First, get the hash from the user to get the sha1 hash to crack

  sha1hash = input("Enter SHA1 Hash:.\nSSTF>")

#Second, we'll open a file full of password guesses

  LIST_OF_COMMON_PASSWORDS = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8')

#Third, we'll take a guess from the list of passwords we opened, and split it by line

  for guess in LIST_OF_COMMON_PASSWORDS.split('\n'):

#Fourth, we'll hash the guess we took from the password list so we can compare it to the hash the user gave us

    hashedGuess = hashlib.sha1(bytes(guess, 'utf-8')).hexdigest()

#Fifth, we'll compare the hash the user gave us to the hashed version of the password guess and determine if they are equal

    if hashedGuess == sha1hash:

#Sixth, we'll tell the program what to do if the password guess matches, which is to print the current guess and quit the program.
#We'll also tell the program what to do if the password guess don't match, which is to return to step 3 to get a new password from the list

        print("The password is ", str(guess))
        quit()
    elif hashedGuess != sha1hash:
        print(str(guess),", Nope.")

#In the seventh and final step, we'll tell the program what to do if we get all the way through the password list without finding a match.
  print("Password not in list.")

