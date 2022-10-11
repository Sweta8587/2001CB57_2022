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