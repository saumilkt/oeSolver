from random import *
from statistics import mean


weights = [.01,.07,.36,.56]
def alpha_a_weightage(population, alpha_a):
    hold = []
    n=0
    m=0
    l=0
    s=0

    for _ in range(population):
        temp=random()*population
        if(temp<.25*population):
            n+=1
        elif(temp<.5*population):
            l+=1
        elif(temp<.75*population):
            m+=1
        else:
            s+=1

    n0=n*weights[0]/population
    l0=l*weights[1]/population
    m0=m*weights[2]/population
    s0=s*weights[3]/population

    final_weightage = mean([n0,l0,m0,s0])*triangular(0,5)*randint(1,5)

    if(final_weightage<alpha_a):
        return final_weightage
    else:
        return mean([final_weightage,alpha_a])
