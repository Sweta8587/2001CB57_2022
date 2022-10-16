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