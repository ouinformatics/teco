import sys
from numpy import *

def kalman(state, obs, oberror):
    "updates the forcast given the history and state matrix, observations, and observational error"

    oberror=matrix(oberror)
    state=matrix(state)

    X=state[:,-1]
    Z=matrix(obs).T
    Pf=cov(state)
    tmp=size(obs)
    H=matrix(zeros((tmp,size(X))))
    startdim=(shape(H)[1])-tmp
    for i in range(0,shape(H)[0]):
            H[i,i+startdim]=1
    R=oberror.T*oberror
    PHT=Pf*H.T
    D=(H*PHT)+R
    Dn=linalg.inv(D)
    K=(PHT)*Dn
    tmp=K*H
    Pu=(eye(shape(tmp)[0])-tmp)*Pf
    Xu=X+(K*(Z-(H*X)))

    return Xu
