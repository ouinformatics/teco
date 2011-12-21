import sys
from numpy import *
from math import e

def resperation(params):
    "computes resperation given a vector of temp related parameters"

    vcmax=params[0]
    tl=params[1]
    tminv=params[2]
    tmaxv=params[3]
    topt=params[4]
    toptv=params[5]
    tmin=params[6]
    tmax=params[7]

    vcmaxt=((vcmax*(tl-tminv))/(topt-tminv))*(((tmaxv-tl)/(tmaxv-toptv))**((tmax-topt)/(topt-tmin)))
    rd=vcmaxt*.0089
    return rd


def csiupdate(params):
    "updates c_s,i based on temperature and list of parameters"
    k=.5
    sla=0.012
    dheat=2.15*10**-7
    patm=params[0]
    wleaf=params[1]
    wind=params[2]
    tleaf=params[3]
    a=params[4]
    tk=params[5]
    tair=params[6]
    leafc=params[7]
    r=params[8]
    co2a=params[9]

    bm=leafc/0.45
    gras=1.595*(10**8)*abs(tleaf-tair)*(wleaf**3) #tleaf has i subscript, but not used elsewhere, so can be called twice with different tleaf?
    windv0=min(1,wind)
    lai=bm*sla
    flai=multiply([.0469,.23075,.5,.7692,.9531],lai)
    windux=[]
    for i in range(size(flai)):
        windux.append(flai[i])

    gbhu=multiply(.003,sqrt(divide(windux,wleaf)))
    gbhf=(.5*dheat*gras**.25)/wleaf
    cmolar=patm/(r*tk)
    gbh=add(gbhu,gbhf)
    gbc=divide(multiply(cmolar,gbh),1.32)
    gbc=array(gbc)
    csi=co2a-a/gbc
    return csi
#    return gbc

def netphoto(params):
    "computes net photosynth from parameters and previous results"
    t=params[0]
    gamma=params[1]
    bmleaf=params[2]
    sla=params[3]
    laimin=params[4]
    jmax=params[5]
    i=params[6] #1=sun 2=shade

    if gamma==0:
        l0=2.8*(10**(-7))
        l1=.0509
        l2=.001
        dt=t-293.2
        lstar==l0*(1+l1+dt+l2+dt**2)
        gamms=lstar
    
    lai=bmleaf*sla
    return params
