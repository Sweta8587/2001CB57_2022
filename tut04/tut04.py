# #Help https://youtu.be/H37f_x4wAC0
# def octant_longest_subsequence_count_with_range():
# ###Code

# from platform import python_version
# ver = python_version()

# if ver == "3.8.10":
#     print("Correct Version Installed")
# else:
#     print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")


# octant_longest_subsequence_count_with_range()

import pandas as pd # importing pandas library
df = pd.read_excel(r"C:\Users\ASUS\Documents\GitHub\2001CB57_2022\tut04\input_octant_longest_subsequence_with_range.xlsx")
x = df.shape[0]
df.head()
 #finding average of U, V and W using mean function
U_avg = df['U'].mean()
V_avg = df['V'].mean()
W_avg = df['W'].mean()

#creating columns(name = U Avg, V Avg, W Avg) to store U_avg  ,V_avg and W_avg values
df['U Avg']=U_avg
df['V Avg']=V_avg
df['W Avg']=W_avg

#taking head(1) means U Avg , V Avg and W Avg will print only one time(at a place)
df['U Avg']=df['U Avg'].head(1)
df['V Avg']=df['V Avg'].head(1)
df['W Avg']=df['W Avg'].head(1)
df.head()
 #defining a,b,c where a=U' , b=V' , c=W'
a = df['U'] - U_avg
b = df['V'] - V_avg
c = df['W'] - W_avg

# creating colums named U', V' and W' to store the a,b and c values resp
df["U'=U - U_avg"] = a
df["V'=V - V_avg"] = b
df["W'=W - W_avg"] = c

df.to_excel('output_octant_longest_subsequence_with_range.xlsx')
df.head()
 #creating the column to store the octant value
df.insert(10, column="Octant", value="")


#using loop
for i in range(0,x):
    X= df["U'=U - U_avg"][i]
    Y= df["V'=V - V_avg"][i]
    Z= df["W'=W - W_avg"][i]
    
    
    if X>0 and Y>0 and Z>0:
        print(1)
        df["Octant"][i] = 1
    elif X>0 and Y>0 and Z<0:
        print(-1)
        df["Octant"][i] =-1
    elif X<0 and Y>0 and Z>0:
        print(2)
        df["Octant"][i] =2
    elif X<0 and Y>0 and Z<0:
        print(-2)
        df["Octant"][i] =-2
    elif X<0 and Y<0 and Z>0:
        print(3)
        df["Octant"][i] =3
    elif X<0 and Y<0 and Z<0:
        print(-3)
        df["Octant"][i] =-3
    elif X>0 and Y<0 and Z>0:
        print(4)
        df["Octant"][i] =4
    elif X>0 and Y<0 and Z<0:
        print(-4)
        df["Octant"][i] =-4
df.to_excel('output_octant_longest_subsequence_with_range.xlsx')
df.head()

df.insert(11, column="  ", value="")
#creating the column to store the count value as column name count_1
df.insert(12, column="Count_1", value="")
#creating the column to store the Longest Subsquence Length value
df.insert(13, column="Longest Subsquence Length", value="")
#creating the column to store the total count value as column name final_count
df.insert(14, column="final_count", value="")

 # storing the for count_1(count column name taken as count_1) column in a list
list=[1,-1, 2, -2, 3,-3, 4,-4]
y=len(list) #finding the list size
# printing the values in the count_1
for i in range (0,y):
    df.at[i,'Count_1'] = list[i]
df.head(10)

# calculating the longest subsequence length value by defining a funtion name longest_sequence with the parameter n(list value)
def longest_sequence(n):
    lsc_p1_i=0
    lsc_p1=0
    for i in range(0,x):
        if(df["Octant"][i]==n):
            lsc_p1=lsc_p1+1
        if(df["Octant"][i]!=n or i==x-1):
            if(lsc_p1>lsc_p1_i):
                lsc_p1_i=lsc_p1
                lsc_p1=0
            else:
                lsc_p1_i=lsc_p1_i
                lsc_p1=0
    return lsc_p1_i

# creating a array(arr_longest_subs_length)to store the longest sequence length of the count_1 value
arr_longest_subs_length = [0] * y
# using a loop in which we are calling the longest_sequence function. with the help of this function we are printing the values directly in the output file
for i in range(0,y):
    arr_longest_subs_length[i]=longest_sequence(list[i])
    df.at[i,'Longest Subsquence Length'] = arr_longest_subs_length[i]

# calculating the count value by defining a funciton name final_count_no with two paramater m and n which is (longest sequence length value, count_1 value)
def final_count_no(m,n):
    cp1=0
    cp1i=0
    for i in range(0,x):
        if(df["Octant"][i]==n):
            cp1i=cp1i+1
        if(cp1i==m):
            cp1=cp1+1
            cp1i=0  
        if(df["Octant"][i]!=n):
            cp1i=0
    return cp1

# creating a array(name arr_longest_subs_length_count) to store the no. of sequence count value(final_count column) 
arr_longest_subs_length_count = [0] * y
# using a loop in which we are calling the final_count_no function. with the help of this function we are printing the values directly to the final_count column
for i in range(0,y):
    arr_longest_subs_length_count[i]=final_count_no(arr_longest_subs_length[i],list[i])
    df.at[i,'final_count'] = arr_longest_subs_length_count[i]

    

