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


for i in range(lx): #iterating through every ball 
  ball_no=line[i][0]
  players=line[i][1].split('to') 
  batsname=players[1]            #finding batsamn and bowler names for every deliery
  bowlername=players[0]

  line[i][2]=line[i][2].lower()  #converting the verdict of the delivery into lower case

  if line[i][2]==" wide":  #if the delivery is wide
   wide=wide+1             #adding +1 to wide variable
   score=score+1
   mybowlers.loc[bowlername,'R']=mybowlers.loc[bowlername,'R']+1  #adding 1 run to the particular bowler's runs
   mybowlers.loc[bowlername,'WD']=mybowlers.loc[bowlername,'WD']+1 # increaing count of wide by +1

  elif line[i][2]==" four" or line[i][2]==' 4' or line[i][2]==' 4 runs': #if the verdict of the delivery if '4'
   mybatsman.loc[batsname,'R']=mybatsman.loc[batsname,'R']+4  
   mybatsman.loc[batsname,'4s']=mybatsman.loc[batsname,'4s']+1
   mybatsman.loc[batsname,'B']=mybatsman.loc[batsname,'B']+1
   mybowlers.loc[bowlername,'B']=mybowlers.loc[bowlername,'B']+1
   mybowlers.loc[bowlername,'R']=mybowlers.loc[bowlername,'R']+4
   score=score+4

  elif line[i][2] == ' six' or line[i][2] == ' 6' or line[i][2] == ' 6 runs': #if the verdict of the ball is '6'
   mybatsman.loc[batsname,'6s'] = mybatsman.loc[batsname,'6s'] + 1
   mybatsman.loc[batsname,'R'] = mybatsman.loc[batsname,'R'] + 6
   mybatsman.loc[batsname,'B'] = mybatsman.loc[batsname,'B'] + 1

   mybowlers.loc[bowlername,'B'] = mybowlers.loc[bowlername,'B'] + 1
   mybowlers.loc[bowlername,'R'] = mybowlers.loc[bowlername,'R'] + 6
   score = score +6
   
  elif line[i][2] == ' 1 run' or line[i][2] == ' 1': #if the verdict of the ball is'1' run
        mybatsman.loc[batsname,'R'] = mybatsman.loc[batsname,'R'] + 1   
        mybatsman.loc[batsname,'B'] = mybatsman.loc[batsname,'B'] + 1
        
        mybowlers.loc[bowlername,'B'] = mybowlers.loc[bowlername,'B'] + 1
        mybowlers.loc[bowlername,'R'] = mybowlers.loc[bowlername,'R'] + 1
        score = score +1
    
    
  elif line[i][2] == ' 2 runs' or line[i][2] == ' 2 run' or line[i][2] == ' 2': #it the verdict of the ball is '2' runs
        mybatsman.loc[batsname,'R'] = mybatsman.loc[batsname,'R'] + 2 
        mybatsman.loc[batsname,'B'] = mybatsman.loc[batsname,'B'] + 1
        
        mybowlers.loc[bowlername,'B'] = mybowlers.loc[bowlername,'B'] + 1
        mybowlers.loc[bowlername,'R'] = mybowlers.loc[bowlername,'R'] + 2
        score = score +2
    
   
  elif line[i][2] == ' 3 runs' or line[i][2] == ' 3 run' or line[i][2] == ' 3': #it the verdict of the ball is '3' runs
        mybatsman.loc[batsname,'R'] = mybatsman.loc[batsname,'R'] + 3
        mybatsman.loc[batsname,'B'] = mybatsman.loc[batsname,'B'] + 1
        
        mybowlers.loc[bowlername,'B'] = mybowlers.loc[bowlername,'B'] + 1
        mybowlers.loc[bowlername,'R'] = mybowlers.loc[bowlername,'R'] + 3
        score = score +3
  elif line[i][2] == ' no run' or line[i][2] == ' no': #if delivery is a dot and legal
        mybatsman.loc[batsname,'B'] = mybatsman.loc[batsname,'B'] + 1 
        mybowlers.loc[bowlername,'B'] = mybowlers.loc[bowlername,'B'] + 1
    
   
  elif line[i][2] == ' leg byes' : #if delivery verdict is leg byes
        mybatsman.loc[batsname,'B'] = mybatsman.loc[batsname,'B'] + 1        
        mybowlers.loc[bowlername,'B'] = mybowlers.loc[bowlername,'B'] + 1
                        
        if line[i][3] == ' four' or line[i][3] == ' 4' or line[i][3] == ' 4 runs':#for 4 leg byes
            lb = lb + 4
            score = score +4

        if line[i][3] == ' 1 run' or line[i][3] == ' 1': #for 1leg bye
            lb = lb + 1
            score = score +1

  elif line[i][2] == ' byes': #if delivery verdict is bye
        mybatsman.loc[batsname,'B'] = mybatsman.loc[batsname,'B'] + 1
        mybowlers.loc[bowlername,'B'] = mybowlers.loc[bowlername,'B'] + 1
                
        if line[i][3] == ' 1 run' or line[i][3] == ' 1': #for 1bye
            b = b + 1
            score = score +1
  else:   #if the verdict of the delivery is a wicket 
        mybatsman.loc[batsname,'B'] = mybatsman.loc[batsname,'B'] + 1
        mybowlers.loc[bowlername,'B'] = mybowlers.loc[bowlername,'B'] + 1
        wickets = wickets +1   #increasing wicket count
        add = str(score) + '-' + str(wickets) + '('+ batsname + ',' + ball_no + ')'#adding to the the fall of wickets string
        fall=fall+add
        fall=fall+" "
        
        content = line[i][2].split('!')  #spltting @ '!'
        
        if content[0] == ' out bowled': #if the mode of wicket is 'bowled'
            mybatsman.loc[batsname,'status'] = 'b ' + bowlername 
            mybowlers.loc[bowlername,'W'] = mybowlers.loc[bowlername,'W'] + 1
        elif content[0]==' out lbw':   #if the mode of wicket is 'lbw'
         mybatsman.loc[batsname,'status'] = 'lbw ' + bowlername 
         mybowlers.loc[bowlername,'W'] = mybowlers.loc[bowlername,'W'] + 1
        else: #if the mode of wicket is 'caught out'
            content2 = content[0].split('by')
            mybatsman.loc[batsname,'status'] = 'c ' + content2[1] + ' b ' + bowlername #updating status of the batsman
            mybowlers.loc[bowlername,'W'] = mybowlers.loc[bowlername,'W'] + 1
         
  mybatsman.loc[batsname,'SR'] = int((mybatsman.loc[batsname,'R'] / mybatsman.loc[batsname,'B']) * 100) #updating strike rate of the batsman
  mybowlers.loc[bowlername,'O'] = (mybowlers.loc[bowlername,'B']//6)+((mybowlers.loc[bowlername,'B']%6)*0.1)#overs bowled by the bowler

  mybowlers.loc[bowlername,'EC'] = mybowlers.loc[bowlername,'R']/(mybowlers.loc[bowlername,'B']/6)#economy of the bowler


extra =lb + b  + wide #calculating total extra's of the innings

print('SCORECARD')
print(mybatsman)
print('\nExtras\t\t'+ str(extra) + '(b ' + str(b) +', lb '+ str(lb) +', w '+ str(wide) +', nb '+ str(noball) + ')')
print('\nTotal\t\t'+ str(score) + ' ('+ str(wickets)+ ' wkts, '+ str(mybowlers['O'].sum()) +' Ov)\n' )
print('fall of wickets\n')
print(fall)
print('\n')
print(mybowlers.iloc[:,:-1])

with open('Scorecard.txt', 'a') as f: #writing the scorecard of the first innings into scorecard.txt file
    f.write('SCORECARD')
    f.write('\n')
    f.write('Pakistan innings')
    f.write('\n')
    dfAsString = mybatsman.to_string(header=True,index=True)
    f.write(dfAsString)
    f.write('\nExtras\t\t'+ str(extra) + '(b ' + str(b) +', lb '+ str(lb) +', w '+ str(wide) +', nb '+ str(noball) + ')')
    f.write('\n')
    f.write('\nTotal\t\t'+ str(score) + ' ('+ str(wickets)+ ' wkts, '+ str(mybowlers['O'].sum()) +' Ov)\n')
    f.write('\n')
    f.write('fall of wickets')
    f.write('\n')
    f.write(fall)
    f.write('\n')
    f.write('bowler')
    f.write('\n')
    dfAsSt = mybowlers.to_string(header=True,index=True)
    f.write(dfAsSt)
    f.write('\n')

         ####  SIMILARLY FOR THE SECOND INNINGS  #### 

         
text2=open("india_inns2.txt","r").read() #reading 2nd innings input file into 'text2'

sent2=[]

for row in text2.split("\n"):
	sent2.append(row)      

ball=re.findall(r'([0-9][.][1-6]|[1-2][0-9][.][1-6])',text)


while("" in sent2):
    sent2.remove("")


for i in range(61):

		sent2[i]=sent2[i][:3]+","+sent2[i][3:]

for i in range(61,124):
	
		sent2[i]=sent2[i][:4]+","+sent2[i][4:]



l=len(sent2)

line2=[]

list12=[]

for i in range(l):
	list12=sent2[i].split(',')
	line2.append(list12)

lx=len(line2)
batsman2=[]
bowlers2=[]
cnt=0

for i in range(lx):
	players2=line2[i][1].split('to')	
	# print(players)
	# print("\n")
	bowlers2.append(players2[0])
	batsman2.append(players2[1])
batsman2=list(dict.fromkeys(batsman2))
bowlers2=list(dict.fromkeys(bowlers2))

mybatsman2=pd.DataFrame(0,batsman2,['status','R','B','4s','6s','SR'])

mybatsman2['status']='not out'

mybowlers2=pd.DataFrame(0,bowlers2,['O','M','R','W','NB','WD','EC','B'])

extra2=0
wide2=0
score2=0
wickets2=0
noball2=0
b2=0
lb=0
fall2=''

content3=[]