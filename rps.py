#!/usr/bin/env python

print("""
-------------------------------------------------

Ultimate Rock-Paper-Scissors
by
*   *  *****  *   *  *****  *****
*   *  *   *  ** **  *      *   *
*****  *   *  * * *  ***    *****
*   *  *   *  *   *  *      * *
*   *  *****  *   *  *****  *   *

--------------------------------------------------

Are you ready to take on the Rock, Paper, Scissors (RPS) jedi master?

""")
x = input("Enter your name, young padawan.\n ")

import random
import os
import re

os.system('cls' if os.name == 'nt' else 'clear')

while(1 < 2):
	print("\nRock, Paper, Scissors ... SHOOT!")
	userPick = input("Pick your lightsaber: (R)ock -- (P)aper -- (S)cissors: ")
	if not re.match("[SsRrPp]", userPick):
		print("Pick (R) for Rock, (P) for Paper, and (S) for Scissors.")
		continue
	
	print("You picked " + userPick)
	
	opponent = ['R', 'P', 'S']
	opponentPick = random.choice(opponent)
	print("RPS Jedi Master picks " + opponentPick)
	
	if opponentPick == str.upper(userPick):
		print("Tie Round!")
	elif opponentPick == "R" and userPick.upper() == "S":
		print("Rock crushes scissors. RPS Jedi Master wins!")
	elif opponentPick == "R" and userPick.upper() == "P":
		print("Paper covers rock. You win this time, young padawan.")
	elif opponentPick == "P" and userPick.upper() == "S":
		print("Scissors cut paper. Strong in the force, you are.")
	elif opponentPick == "P" and userPick.upper() == "R":
		print("Paper covers rock. Maybe next time, " + x + ".")
	elif opponentPick == "S" and userPick.upper() == "P":
		print("Scissors cut paper. You need more training, " +x + ".")
	else:
		print("Rock crushes scissors. Well played.")
		
