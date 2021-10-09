#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2021 garglemonster <garglemonster@garglemonster>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from random import randint
import linecache
import os

filepath = "/home/garglemonster/Desktop/Python Projs/hangman/words.txt"
guesses = 6

top = "   ________      "
rope = "     |"
heads = "     O"
arms = "     ~"
sternum = "     |"
legs = "     ^"
pole = "   |"
bottom = "___|_____________"

def count_vowels(s):
	s = s.casefold()
	return sum(s.count(vowel) for vowel in 'aeiou')
	
def letsplay():
	drawgallows(0)
	word = getrandomword()
	wordlength = len(word)
	
	tempword = ""
	for i in range(wordlength):
		tempword += "_ "
	
	print(tempword)	
	vowels = count_vowels(word)
	print("The word has " + str(vowels) + " vowels")
	
#	os.system("cls||clear")
	
def drawgallows(num):
	imagestr = top + "\n" + pole + rope + "\n"
	if num == 1:
		imagestr += pole + heads + "\n"
		imagestr += (pole + "\n") * 4
	elif num == 2:
		imagestr += pole + heads + "\n"
		imagestr += pole + arms + "\n"
		imagestr += (pole + "\n") * 3
	elif num == 3:
		imagestr += pole + heads + "\n"
		imagestr += pole + arms + "\n"
		imagestr += pole + sternum + "\n"
		imagestr += (pole + "\n") * 2
	elif num == 4:
		imagestr += pole + heads + "\n"
		imagestr += pole + arms + "\n"
		imagestr += pole + sternum + "\n"
		imagestr += pole + legs + "\n"
		imagestr += pole + "\n"
	else: 
		imagestr += (pole + "\n") * 5
	
	imagestr += bottom
	print(imagestr)
	
def getrandomword():
	count = len(open(filepath).readlines( ))
	value = randint(1, count)
	w = linecache.getline(filepath, value)
	linecache.clearcache()
	return w
			
def hangman():
	yes = "y"
	no = "n"
	
	while(True):
		response = input("Do you want to play hangman (y/n)?")
		if response.strip().isdigit():
			print("No numbers, only y or n.")
		elif response.strip() == yes:
			print("Let's play!")
			letsplay()
			break
		elif response.strip() == no:
			print("Goodbye!")
			break
		else:
			print(f"This was your input {response}")

def main(args):
	hangman()
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
