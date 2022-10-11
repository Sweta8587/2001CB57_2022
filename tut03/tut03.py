from math import ceil
import openpyxl
from openpyxl import Workbook
from datetime import datetime

start_time = datetime.now()

def get_octant(x, y, z):
    if(x>=0 and y>=0 and z>=0):
        return(1)
    elif(x>=0 and y>=0 and z<0):
        return(-1)
    elif(x<0 and y>=0 and z>=0):
        return(2)
    elif(x<0 and y>=0 and z<0):
        return(-2)
    elif(x<0 and y<0 and z>=0):
        return(3)
    elif(x<0 and y<0 and z<0):
        return(-3)
    elif(x>=0 and y<0 and z>=0):
        return(4)
    else:
        return(-4)


def octant_longest_subsequence_count():
    # processed values (to be used in program)
    ud, vd, wd, ov=[], [], [], []

    # sum values
    u_s, v_s, w_s=0, 0, 0

    # count of values
    n=0
    
    try:

        # input xlsx file 
        wb_input=openpyxl.load_workbook("input_octant_longest_subsequence.xlsx")
        input_sh=wb_input.active

        # getting number of rows
        nr=input_sh.max_row

        # n (no of values) = number of rows(nr) - header row(1)
        n=nr-1

        for i in range(2, nr+1):
            u_s+=input_sh.cell(i,2).value
            v_s+=input_sh.cell(i,3).value
            w_s+=input_sh.cell(i,4).value

        # calculating average values
        u_s/=n; v_s/=n; w_s/=n

        #reporting data upto 9 decimal places
        u_s=int(u_s*1000000000); u_s/=1000000000
        v_s=int(v_s*1000000000); v_s/=1000000000
        w_s=int(w_s*1000000000); w_s/=1000000000
