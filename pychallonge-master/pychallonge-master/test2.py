# Carmen "Beanwolf" Condeluci
# 7/10/14

from __future__ import print_function
from shutil import move
import challonge
import sys
import time
import os

print("""This program pulls recently completed and/or upcoming matches from 
	your Challonge hosted tournament and outputs a summary of the match to 
	a text file. This can then be used with either OBS or XSplit's internal 
	text scrolling tools, or an HTML/Flash source that can process text from 
	and external file.\n""")

print("This file is saved as \"output.txt\" in the same directory as this program.")
print("It will not appear until after one iteration has completed.\n")

print("""The number of completed and upcoming matches that will fit on the 
	standard XSplit or OBS text scrolls is not too much. OBS, for example, 
	tops out after about 4 completed matchs and 2 upcoming matches with a 
	normal size font and some leading text. Keep this in consideration when 
	working with these utilities.\n""")

# Tell pychallonge about your [CHALLONGE! API credentials](http://api.challonge.com/v1).
challongeUsername = raw_input("Please enter your Challonge username: ")
challongeAPIKey = raw_input("Please enter your Challonge API Key: ")

challonge.set_credentials(challongeUsername, challongeAPIKey)

# Retrieve a tournament by its id (or its url).
tournamentURL = raw_input("Please enter the tournament's URL indentifier (\"challonge.com/xzr2pwvh\" would have a URL indentifier of \"xzr2pwvh\"): ")

tournament = challonge.tournaments.show(tournamentURL)

matchesToShow = int(raw_input("Enter the number of completed matches you would like to show: "))
upcomingToShow = int(raw_input("Enter the number of upcoming matches you would like to show: "))

leadingText = raw_input("Enter any leading text that you would like to have on your ticker: ")

# Tournaments, matches, and participants are all represented as normal Python dicts.

# Retrieve the participants for a given tournament.
participants = challonge.participants.index(tournament["id"])

print("The program will now start in 5 seconds. It will continue to update indefinitely every minute until manually stopped with Ctrl + C.")
time.sleep(5);

#Overall loop would begin here
while True:

	print("Starting an interation...")

	output = open('output.txt.tmp', 'w')

	output.write(leadingText)

	#shows user controlled amount of completed matches (higher rounds first)

	output.write("  <|>  Most Recent Completed Matches:  ")

	completedMatches = challonge.matches.index(tournament["id"], state="complete")
	comLength = len(completedMatches)

	# print(completedMatches)

	if matchesToShow > comLength:
		for x in range(comLength, 0, -1):
			if x != comLength:
				output.write(" | ")

			currentMatch = completedMatches[x-1]

			comRound = str(currentMatch["round"])
			if "-" not in comRound:
				comRoundString = "W" + comRound
			else:
				comRoundString = "L" + comRound[1:]

			p1 = challonge.participants.show(tournamentURL, currentMatch["player1-id"])["name"];
			p2 = challonge.participants.show(tournamentURL, currentMatch["player2-id"])["name"]
			output.write(comRoundString + ": " + p1 + " vs. " + p2 + ", " + currentMatch["scores-csv"])
	else:
		for x in range(comLength, (comLength - matchesToShow), -1):
			if x != comLength:
				output.write(" | ")

			currentMatch = completedMatches[x-1]

			comRound = str(currentMatch["round"])
			if "-" not in comRound:
				comRoundString = "W" + comRound
			else:
				comRoundString = "L" + comRound[1:]

			p1 = challonge.participants.show(tournamentURL, currentMatch["player1-id"])["name"];
			p2 = challonge.participants.show(tournamentURL, currentMatch["player2-id"])["name"]
			output.write(comRoundString + ": " + p1 + " vs. " + p2 + ", " + currentMatch["scores-csv"])

	#Shows upcoming matches

	output.write("  <|>  Upcoming Matches:  ")

	pendingMatches = challonge.matches.index(tournament["id"], state="open")
	pendLength = len(pendingMatches)

	# print(pendingMatches)

	if upcomingToShow > pendLength:
		for x in range(pendLength, 0, -1):
			if x != pendLength:
				output.write(" | ")

			pendingMatch = pendingMatches[x-1]

			penRound = str(pendingMatch["round"])
			if "-" not in penRound:
				penRoundString = "W" + penRound
			else:
				penRoundString = "L" + penRound[1:]

			p1 = challonge.participants.show(tournamentURL, pendingMatch["player1-id"])["name"];
			p2 = challonge.participants.show(tournamentURL, pendingMatch["player2-id"])["name"]
			output.write(penRoundString + ": " + p1 + " vs. " + p2)
	else:
		for x in range(pendLength, (pendLength - upcomingToShow), -1):
			if x != pendLength:
				output.write(" | ")

			pendingMatch = pendingMatches[x-1]

			penRound = str(pendingMatch["round"])
			if "-" not in penRound:
				penRoundString = "W" + penRound
			else:
				penRoundString = "L" + penRound[1:]

			p1 = challonge.participants.show(tournamentURL, pendingMatch["player1-id"])["name"];
			p2 = challonge.participants.show(tournamentURL, pendingMatch["player2-id"])["name"]
			output.write(penRoundString + ": " + p1 + " vs. " + p2)

	output.close();

	move('output.txt.tmp', 'output.txt')

	print("Finished an iteration!\n")

	time.sleep(60)
