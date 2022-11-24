import pandas as pd
import re 
text= open("pak_inns1.txt","r").read() #reading 1st innings input file into 'text'

send=[]

for row in text.split("\n"):
	send.append(row)         #making a list for each line of the commentary


ball=re.findall(r'([0-9][.][1-6]|[1-2][0-9][.][1-6])',text) #finding no of valid ball numbers


while("" in send):
    send.remove("") #removing empty characters in 'send' list


for i in range(62):

		send[i]=send[i][:3]+","+send[i][3:]

for i in range(62,123):                      #adding extra comma after every ball number
	
		send[i]=send[i][:4]+","+send[i][4:]



l=len(send)  # finding lenght of the list

line=[]

list1=[]

for i in range(l):
	list1=send[i].split(',')
	line.append(list1)        # splitting each line of commentary @ ','

lx=len(line)
batsman=[]
bowlers=[]

for i in range(lx):
	players=line[i][1].split('to')	            
	bowlers.append(players[0])     #appending all batsman and bowler names into respective lists
	batsman.append(players[1])
batsman=list(dict.fromkeys(batsman))   #removing duplicates
bowlers=list(dict.fromkeys(bowlers))

mybatsman=pd.DataFrame(0,batsman,['status','R','B','4s','6s','SR']) #creating a dataframe 'mybatsman' with required column and row names and initializing with 0's

mybatsman['status']='not out' #initializing staus column with 'not out'

mybowlers=pd.DataFrame(0,bowlers,['O','M','R','W','NB','WD','EC','B']) #creating a dataframe 'mybatsman' with required column and row names and initializing with 0's

extra=0
wide=0
score=0
wickets=0
noball=0
b=0
lb=0
fall=''

content=[]