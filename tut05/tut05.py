

# from datetime import datetime
# start_time = datetime.now()

# #Help https://youtu.be/N6PBd4XdnEw
# def octant_range_names(mod=5000):

    
#     octant_name_id_mapping = {"1":"Internal outward interaction", "-1":"External outward interaction", "2":"External Ejection", "-2":"Internal Ejection", "3":"External inward interaction", "-3":"Internal inward interaction", "4":"Internal sweep", "-4":"External sweep"}

# ###Code

# from platform import python_version
# ver = python_version()

# if ver == "3.8.10":
#     print("Correct Version Installed")
# else:
#     print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")


# mod=5000 
# octant_range_names(mod)



# #This shall be the last lines of the code.
# end_time = datetime.now()
# print('Duration of Program Execution: {}'.format(end_time - start_time))
try:
    import pandas as pd
    import math
    def octant_range_names(mod=5000):
     try:
        df = pd.read_excel("octant_input.xlsx")  # reading the input file
        df.head()
        df["U_Average"] = df["U"].mean()     #Creating average for coloumns U,V,W 
        df["V_Average"] = df["V"].mean()
        df["W_Average"] = df["W"].mean()
        df["U1"] = df["U"]-df["U_Average"]  # Creating new columns for U1,V2,W3 
        df["V2"] = df["V"]-df["V_Average"] 
        df["W3"] = df["W"]-df["W_Average"] 
        
        df.loc[((df.U1 > 0) & (df.V2 > 0) & (df.W3 >0)), "Octant"] = "+1" 
        df.loc[((df.U1 > 0) &(df.V2 > 0) & (df.W3 <0)), "Octant" ] = "-1"
        df.loc[((df.U1 < 0) &(df.V2 > 0) & (df.W3 >0)), "Octant" ] = "+2"
        df.loc[((df.U1 < 0) &(df.V2 > 0) & (df.W3 <0)), "Octant" ] = "-2"    #creating octant column,   assigning integers for each octant 
        df.loc[((df.U1 < 0) &(df.V2 < 0) & (df.W3 >0)), "Octant" ] = "+3"
        df.loc[((df.U1 < 0) &(df.V2 < 0) & (df.W3 <0)), "Octant" ] = "-3"
        df.loc[((df.U1 > 0) &(df.V2 < 0) & (df.W3 >0)), "Octant" ] = "+4"
        df.loc[((df.U1 > 0) &(df.V2 < 0) & (df.W3 <0)), "Octant" ] = "-4"
        
        x =df['Octant'].value_counts() # total count of number of values for each octant

        df.loc[0,"octant id"]="overall count"  # creating octant id column and assigning octant count under that.
        df.loc[0,"+1"]=x["+1"]      # assigning octant count under all octants(+1,-1,+2,-2,+3,-3,+4,-4)             
        df.loc[0,"-1"]=x["-1"]
        df.loc[0,"+2"]=x["+2"] 
        df.loc[0,"-2"]=x["-2"]
        df.loc[0,"+3"]=x["+3"]
        df.loc[0,"-3"]=x["-3"]
        df.loc[0,"+4"]=x["+4"]
        df.loc[0,"-4"]=x["-4"]
        y=str(mod)
        df.loc[1,"octant id"]="mod"+" "+y # assigning input label based on the user
        try: 
          d=math.ceil(29745/mod) # greatest integer function for identifing 
          l=0000
          m=mod-1
          a=str(l)
          b=str(m)
          for j in range(d) :
             if int(b)>=29744:
                df.loc[j+2,"octant id"]= a+"-"+"29744"
                l=m+1
                m=m+mod
                a=str(l)
                b=str(m)
             else:
                df.loc[j+2,"octant id"]= a+"-"+b
                l=m+1
                m=m+mod
                a=str(l)
                b=str(m)
