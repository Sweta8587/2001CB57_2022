import csv
from math import ceil, floor

def get_octant(x, y, z):
    if(x>=0 and y>=0 and z>=0):
        return("octant is 1")
    elif(x>=0 and y>=0 and z<0):
        return("octant is -1")
    elif(x<0 and y>=0 and z>=0):
        return("octant is 2")
    elif(x<0 and y>=0 and z<0):
        return("octant is -2")
    elif(x<0 and y<0 and z>=0):
        return("octant is 3")
    elif(x<0 and y<0 and z<0):
        return("octant is -3")
    elif(x>=0 and y<0 and z>=0):
        return("octant is 4")
    else:
        return("octant is -4")

def octact_identification(mod=5000):
    
    # values of original
    T, U, V, W=[], [], [], []

    # processed values 
    U_, V_, W_=[], [], []

    # sum values 
    Uavg, Vavg, Wavg=0, 0, 0

    # count of values
    n=0  

    try:
        with open('octant_input.csv', 'r') as inputfile:
            freader=csv.reader(inputfile)

            # now skipping the heading row
            next(freader)

            for line in freader:
                Uavg+=float(line[1])
                U.append(float(line[1]))

                Vavg+=float(line[2])
                V.append(float(line[2]))

                Wavg+=float(line[3])
                W.append(float(line[3]))

                T.append(line[0])
                n+=1

            #  average values calculation
            Uavg=Uavg/n
            Vavg=Vavg/n
            Wavg=Wavg/n

            for i in range(0,n):
                x=U[i]-Uavg
                U_.append(x)

                y=V[i]-Vavg
                V_.append(y)
                
                z=W[i]-Wavg
                W_.append(z)

            nr=ceil(n/mod)        
