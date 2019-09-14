#! /bin/python/python3
import tools
import sys
import sstfServer
import os

def Menu():
	print("________________________")
	print("|SkSweetTooth Framework|")
	print("|  Version 1.0  Beta   |")
	print("|Written in Python by: |")
	print("|     Skittles_        |")
	print("|______________________|")
	print("")
	print("")
	print("")
	print("   __________________,.................,")    
	print("   /_/_/_/_/_/_/_/_/,-' ,   ,.  -,-,--/|")
	print("  /_/_/_/_/_/_/_/,-' / /   /-|  / /--/ /")
	print(" /_/_/_/_/_/_/,-' `-' /__ /  \ / /__/ / ")
	print("/_/_/_/_/_/_,:...................../ /")
	print("|________,'________________________|/ ")
	print("")
	print("")
	print("")
	print("")
	print("")
	print("")
	print ("(1) Passcrack (2) Port scanner (3)Start Server (4)About (exit)GTFO")

#Defining variable for selection choice

	selection = input("Choose an option:")

#Selection code. If no option is picked, or a wrong input is recieved, program stops.

	if selection == "1":
		tools.Passcrack()

	if selection == "2":
		tools.portscan()

	if selection == "4":
		tools.WhatIsSSTF()

	if selection == "3":
		sstfServer.Server()

	if selection == "exit":
		sys.exit()

	if selection == "hiddentest":
		tools.test()
	else:
		os.system('cls' if os.name == 'nt' else 'clear')
		Menu()
Menu()
