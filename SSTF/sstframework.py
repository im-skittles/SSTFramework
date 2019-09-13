#! /bin/python/python3
import tools
import sys

print("________________________")
print("|SkSweetTooth Framework|")
print("|  Version 0.2 Alpha   |")
print("|Written in Python by: |")
print("|     Skittles_        |")
print("|______________________|")
print("")
print("")
print("")
print("")
print ("(1) Passcrack (2) Port scanner (3)About (exit)GTFO")

#Defining variable for selection choice

selection = input("Choose an option:")

#Selection code. If no option is picked, or a wrong input is recieved, #program stops.

if selection == "1":
	tools.Passcrack()

if selection == "2":
	tools.portscan()

if selection == "3":
	tools.WhatIsSSTF()

if selection == "exit":
	sys.exit()

if selection == "hiddentest":
	tools.test()

