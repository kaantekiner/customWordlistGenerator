import itertools
import datetime
import time
import sys
from pip._vendor.distlib.compat import raw_input

print("\n")
print("Wellcome!")
print("\n")
print("Enter your most important keyword(just 1 preferred)- capital or non capital is ok")
mostImportantWord = raw_input("")
if mostImportantWord is "":
	print("please type something")
	sys.exit(0)
print("ok, lets move on.","\n")
OnemliKelimeList = [mostImportantWord.lower(), mostImportantWord.capitalize()]
print("Enter your other keywords - and split them with comma(,) please, capital or non capital is ok(and please no spaces)")
print("example >> key1,key2,Key3,keyy4")
otherWordsSentence = raw_input()
if otherWordsSentence is "":
	print("please type something")
	sys.exit(0)
anahtarkelimeler = otherWordsSentence.split(",")
for item in anahtarkelimeler:
	item.lower()
haveOddChar = False
for item in anahtarkelimeler:
	if item == "" or item == " " or item == "  " or item == "," or item == ",,":
		haveOddChar = True
if haveOddChar is True:
	print("please just use one(1) comma between your keywords(like key1,key2) not key1,key2, or key1,,key2")
	sys.exit(0)
haveMultiple = False
for item in anahtarkelimeler:
	if anahtarkelimeler.count(item) >= 2:
		haveMultiple = True
if haveMultiple is True:
	multipleContinue = input("you have multiples, dou you wanna continue anyway?[y/N]")
	if multipleContinue.lower() != "y":
		print("bye:)")
		sys.exit(0)
print("ok, keep going.","\n")
list1 = ["0","00","000","0000"]
list2 = [".","..","...,","...."]
list3 = ["!","!!","!!!","!!!!"]
list4 = [",",",,",",,,",",,,,"]
list5 = ["*","**","***","****"]
list6 = ["?","-","_","$"]
list7 = ["1","2","3","4","5","6","7","8","9"]
list8 = ["10","11","12","13","15","16","17","18","19","20","21","22","23","24"]
list9 = ["q","w","e","r","t","y","u","o","p","a","s","d","f","g","h","j","k","l","i","z","x","c","v","b","n","m"]
list10 = ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
list11 = ["qq","qw","qwe","qwer","qwert","qwerty","ytrewq","trewq","rewq","ewq","wq"]
list12 = ["asd","asdf","asdfg","asdfgh","asdfghj","asdfghjk","asdfghjkl","lkjhgfdsa","kjhgfdsa"]
list13 = ["jhgfdsa","hgfdsa","gfdsa","gfdsa","fdsa","dsa","sa"]
list14 = ["11","22","33","44","55","66","77","88","99","123","1234","123456","123456789","1234567890"]
list15 = ["99","999","9999","999999999"]
list16 = ["1990","1991","1992","1993","1994","1995","1996","1997","1998","1999"]
list17 = ["2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010"]
list18 = ["2011","2012","2013","2014","2015","2016","2017","2018","2019","2020"]
list19 = ["95","96","97","98","99","00","01","02","03","04","05","06","07","08","09"]
list20 = ["10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"]
list21 = ["34","06","35","34774","34775","34776"]
list = list1 + list2 + list3 + list4 + list5 + list6 + list7 + list8 + list9 + list10 + list11 + list12 + list13 + list14 + list15 + list16 + list17 + list18 + list19 + list20 + list21 + list20 + list19 + list14 + list10
n1 = 2
n2 = 3
anahtarkelimelerList = []
NumberLimitToAdd = 100
JustNumberLimitToAdd = 10000000
TotalWordGlobal = 0
writefile=open("wordList.txt","w")
print("At the end of the process, your generated file will be written to the file 'wordList.txt'")

def StartCode():
	global dateStart
	dateStart = datetime.datetime.now()

def SumSpecialAndGeneralToGeneralList():
	anahtarkelimeler.append(str(OnemliKelimeList[0].lower()))

def AddCapitalsToo():
	anahtarkelimelerLen = len(anahtarkelimeler)
	for i in range(anahtarkelimelerLen):
		anahtarkelimeler.append(anahtarkelimeler[i].capitalize())

def CombineKeywordList():
	for i in range(1,3):
		for kelime in itertools.product(anahtarkelimeler, repeat=i):
			eklenecek = "".join(kelime)
			anahtarkelimelerList.append(eklenecek)

def RemoveMultipleSortedKeywords():
	anahtarkelimelerListLower = []
	ListToRemove = []
	for item in anahtarkelimelerList:
		anahtarkelimelerListLower.append(item.lower())
	for item in anahtarkelimeler:
		for i in range(0,len(anahtarkelimelerListLower)):
			if (item * 2) == anahtarkelimelerListLower[i]:
				ListToRemove.append(anahtarkelimelerList[i])
	for item in ListToRemove:
		if item in anahtarkelimelerList:
			anahtarkelimelerList.remove(item)

def RemoveJustSpecialFromGeneralList():
	for item in OnemliKelimeList:
		anahtarkelimelerList.remove(item)

def ShowProcessWillBeMade():
	print("The keyword will be in use for generating password are;", "\n")
	for item in OnemliKelimeList:
		print(item)
	for item in anahtarkelimelerList:
		print(item)
	print("Total Keyword will be in use = ", len(anahtarkelimelerList) + len(OnemliKelimeList),"\n")
	areYouReady = raw_input("Press enter key when you are ready to go.")
	if areYouReady is not "":
		print("goodbye!")
		sys.exit(0)
	print("Okay, process will start in 5...")
	print("Start Time = ",dateStart, "(with the 5 second delay)")
	print("(You can quit operation with ctrl + c / cmd + c when you wanna!)")
	time.sleep(5)

def AddJustNumbers():
	global TotalWordGlobal
	TotalWordLocal = 0
	for i in range(0,JustNumberLimitToAdd):
		print("TotalWord = ",("{:,}".format(TotalWordLocal)))
		writefile.write(str(i))
		writefile.write("\n")
		TotalWordLocal += 1
	TotalWordGlobal = TotalWordLocal

def StartGeneralProcess():
	global TotalWordGlobal
	anahtarkelimelerListLocal = anahtarkelimelerList
	TotalWordLocal = TotalWordGlobal
	for anahtar in anahtarkelimelerListLocal:
		for i in range(0,n1):
			for kelime in itertools.product(list, repeat=i):
				print("TotalWord = ",("{:,}".format(TotalWordLocal)))
				ekle = "".join(kelime)
				writefile.write(ekle + anahtar)
				writefile.write("\n")
				writefile.write(anahtar + ekle)
				writefile.write("\n")
				writefile.write(ekle + anahtar + ekle)
				writefile.write("\n")
				TotalWordLocal += 3
	TotalWordGlobal = TotalWordLocal

def StartJustAddNumberToKeywordsEndProcess():
	global TotalWordGlobal
	anahtarkelimelerListLocal = anahtarkelimelerList
	TotalWordLocal = TotalWordGlobal
	for anahtar in anahtarkelimelerListLocal:
		for i in range(0,NumberLimitToAdd):
			print("TotalWord = ",("{:,}".format(TotalWordLocal)))
			writefile.write(anahtar + str(i))
			writefile.write("\n")
			TotalWordLocal += 1
	TotalWordGlobal = TotalWordLocal

def StartKeywordPlusSpecialAndNumberProcess():
	global TotalWordGlobal
	charlistLocal = list
	anahtarkelimelerListLocal = anahtarkelimelerList
	TotalWordLocal = TotalWordGlobal
	for anahtar in anahtarkelimelerListLocal:
		for char in charlistLocal:
			for i in range(0,NumberLimitToAdd):
				print("TotalWord = ",("{:,}".format(TotalWordLocal)))
				writefile.write(anahtar + str(i) + char)
				writefile.write("\n")
				writefile.write(anahtar + char + str(i))
				writefile.write("\n")
				TotalWordLocal += 2
	TotalWordGlobal = TotalWordLocal

def StartGeneralProcessForSpecialKeyword():
	global TotalWordGlobal
	anahtarkelimelerListLocal = OnemliKelimeList
	TotalWordLocal = TotalWordGlobal
	for anahtar in anahtarkelimelerListLocal:
		for i in range(0,n2):
			for kelime in itertools.product(list, repeat=i):
				print("TotalWord = ",("{:,}".format(TotalWordLocal)))
				ekle = "".join(kelime)
				writefile.write(ekle + anahtar)
				writefile.write("\n")
				writefile.write(anahtar + ekle)
				writefile.write("\n")
				writefile.write(ekle + anahtar + ekle)
				writefile.write("\n")
				TotalWordLocal += 3
	TotalWordGlobal = TotalWordLocal

def StartJustAddNumberToSpecialKeywordsEndProcess():
	global TotalWordGlobal
	anahtarkelimelerListLocal = OnemliKelimeList
	TotalWordLocal = TotalWordGlobal
	for anahtar in anahtarkelimelerListLocal:
		for i in range(0,NumberLimitToAdd):
			print("TotalWord = ",("{:,}".format(TotalWordLocal)))
			writefile.write(anahtar + str(i))
			writefile.write("\n")
			TotalWordLocal += 1
	TotalWordGlobal = TotalWordLocal

def StartSpecialKeywordPlusSpecialAndNumberProcess():
	global TotalWordGlobal
	charlistLocal = list
	anahtarkelimelerListLocal = OnemliKelimeList
	TotalWordLocal = TotalWordGlobal
	for anahtar in anahtarkelimelerListLocal:
		for char2 in charlistLocal:
			for char in charlistLocal:
				for i in range(0,NumberLimitToAdd):
					print("TotalWord = ",("{:,}".format(TotalWordLocal)))
					writefile.write(anahtar + str(i) + char)
					writefile.write("\n")
					writefile.write(anahtar + char + str(i))
					writefile.write("\n")
					writefile.write(char + anahtar + str(i) + char)
					writefile.write("\n")
					writefile.write(char + anahtar + char + str(i))
					writefile.write("\n")
					writefile.write(char + anahtar + str(i) + char + char2)
					writefile.write("\n")
					writefile.write(char + anahtar + str(i) + char2 + char2)
					writefile.write("\n")
					TotalWordLocal += 5
	TotalWordGlobal = TotalWordLocal

def StartToSortTextFile():
	writefile.close()
	print("Total word before sort & remove duplicates = ", "{:,}".format(TotalWordGlobal))
	#sort
	#print("Sorting & removing duplicates, PLEASE DO NOT TOUCH UNTIL process done!")
	#wc -l
	dateEnd = datetime.datetime.now()
	global dateStart
	print("Start Time = ", dateStart)
	print("End Time = ", dateEnd)
	print("Process done.", "\n")

#////////////////////
StartCode()
#////////////////////
SumSpecialAndGeneralToGeneralList()
AddCapitalsToo()
CombineKeywordList()
RemoveMultipleSortedKeywords()
RemoveJustSpecialFromGeneralList()
ShowProcessWillBeMade()
#////////////////////
AddJustNumbers()
StartGeneralProcess()
StartJustAddNumberToKeywordsEndProcess()
StartKeywordPlusSpecialAndNumberProcess()
#////////////////////
StartGeneralProcessForSpecialKeyword()
StartJustAddNumberToSpecialKeywordsEndProcess()
StartSpecialKeywordPlusSpecialAndNumberProcess()
#////////////////////
StartToSortTextFile()
#////////////////////
