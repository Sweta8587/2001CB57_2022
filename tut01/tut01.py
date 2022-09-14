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
        with open('octant_input.csv', 'r') as Ifile:
            freader=csv.reader(Ifile)

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

            # overall frequency of each octant
            fo={1:0, -1:0, 2:0, -2:0, 3:0, -3:0, 4:0, -4:0}

            # range wise frequency of each octant
            f={}

            for i in range (0,nr):
                f[i]={1:0, -1:0, 2:0, -2:0, 3:0, -3:0, 4:0, -4:0}

            for i in range (0,n):
                r=int(i/mod)
                o=get_octant(U_[i], V_[i], W_[i])
                f[r][o]+=1
                fo[o]+=1

            with open('octant_output.csv', 'w', newline='') as Ofile:

                # initialising field names
                fn=['Time', 'U','V', 'W' ,'U Avg','V Avg','W Avg',"U'=U - U avg","V'=V - V avg","W'=W - W avg", "Octant"," ","Octant ID", "+1","-1","+2","-2","+3","-3","+4","-4"]

                writer=csv.writer(Ofile)

                writer.writerow(fn)

                r1=[T[0], U[0], V[0], W[0], Uavg, Vavg, Wavg, U_[0], V_[0], W_[0], get_octant(U_[0], V_[0], W_[0]),'', 'Overall Count', fo[1], fo[-1], fo[2], fo[-2], fo[3], fo[-3], fo[4], fo[-4]]

                writer.writerow(r1)

                r2=[T[1], U[1], V[1], W[1], '','','',U_[1], V_[1], W_[1], get_octant(U_[1], V_[1], W_[1]), 'User Input','Mod '+str(mod)]

                writer.writerow(r2)

                # writing rows for each range consisting of octant frequencies 
                c=0; j=2
                for i in range(2,2+nr):
                    t=[T[i], U[i], V[i], W[i], '','','',U_[j], V_[j], W_[j], get_octant(U_[j], V_[j], W_[j]),'']
                    j+=1
                    if(c<nr):
                        if(c==nr-1):
                            t.extend([str(c*mod+1)+' - '+str(n), f[c][1], f[c][-1], f[c][2], f[c][-2], f[c][3], f[c][-3], f[c][4], f[c][-4]])
                        else:
                            t.extend([str(c*mod)+' - '+str((c+1)*mod-1), f[c][1], f[c][-1], f[c][2], f[c][-2], f[c][3], f[c][-3], f[c][4], f[c][-4]])
                        c+=1
                    else:
                        break

                    writer.writerow(t)

                    # writing remaining rows; (2+nr) rows have been written upto here
                for i in range(2+nr, n):
                    t=[T[i], U[i], V[i], W[i], '','','',U_[j], V_[j], W_[j], get_octant(U_[j], V_[j], W_[j]),'']
                    j+=1;
                    writer.writerow(t)

                # output file closed
                Ofile.close()
            
            # input file closed
            Ifile.close()

    except:
        print('File Not Found')

mod=5000
octact_identification(mod)