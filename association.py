
# Global variables
numTransactions=0
stopProgram=0
likelyhood=0.0
itemVtid=dict()
itemVtid_copy=dict()
displayMenu="\n\n\tTHIS PROGRAM WILL COMPUTE ASSOCIATION RULES WITH 2 ITEMS ONLY.\n\t\t\t\t\tMENU\n\t\t1- Enter the likelihood thresh-hold value for the rules you want to see.\n\t\t2- Exit"
displayThreshhold="\n  Enter the likelihood thresh-hold value:"


def readDataFile():
	global numTransactions
	global itemVtid
	readDescriptor=open("market.data","r")
	readData=readDescriptor.read().split("\n")
	numTransactions=int(readData[0])
	for i in range(1,len(readData)):
		transaction=readData[i].split(",")
		transactionId=int(transaction[0].strip())
		numItems=int(transaction[1].strip())
		#print transaction ,numItems
		for j in range(numItems):
			item=transaction[2+j].strip()
			#print item
			if item not in itemVtid.keys():
				itemVtid[item]=[transactionId]
			else:
				itemVtid[item].append(transactionId)




def findSupport(tidList1,tidList2):
	global likelyhood
	tidIList=list(set(tidList1)&set(tidList2))
	if (len(tidIList)/float(numTransactions)>=likelyhood):
		return 1
	else:
		return 0



def findAssociations(likelyhood):	
	for item1 in itemVtid.keys():
		for item2 in itemVtid.keys():
			if ( findSupport(item1,item2) and  item1!=item2):
				print item1 + "===>"+ item2
	

	

def readInput():
	global stopProgram
	global likelyhood
	print displayMenu
	option=raw_input().strip()
	try:	
		option=int(option)	
		if (option==1):
			print displayThreshhold
			likelyhood=float(raw_input().strip())			
		elif(option==2):
			stopProgram=1
		else:
			readInput()
	except ValueError:
		readInput()



def main():	
	readDataFile()
	#print numTransactions
	while True:
		readInput()
		if (stopProgram==0):
			findAssociations(likelyhood)
			#print likelyhood
		else:
			print "\t \t === Program Terminated Successfully ==="
			break


if __name__=="__main__":
	main()



