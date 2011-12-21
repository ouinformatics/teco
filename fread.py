import sys
from numpy import *
def readobs(filename,headlen=2):
    "Read the observational file for the TECO model"
    obs=loadtxt(filename,skiprows=headlen)
    return obs

def readinit(filename,headlen=0):
    "Read initial conditions for TECO model"
    initcon=loadtxt(filename,skiprows=headlen)
    return initcon

def fout(filename,data,header):
    "Output array of data with header from TECO model"
    data=array_str(data)
    savetxt(filename,data,fmt='%9.6f', delimiter='    ',header=header)
