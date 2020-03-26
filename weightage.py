from random import *
from statistics import mean


weights = [.01,.07,.36,.56] #derived from Transition markov chain; 5th iteration

def alpha_a_weightage(population, alpha_a):
    n=0 # Uninfected
    l=0 # Light
    m=0 # Medium
    s=0 # Severe

# Assign random health states to population
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

# Determine Individual Aggregate Weights
    n0=n*weights[0]/population
    l0=l*weights[1]/population
    m0=m*weights[2]/population
    s0=s*weights[3]/population

# Determine Aggregate Weight
    final_weightage = mean([n0,l0,m0,s0])*triangular(0,5)*randint(1,5) # jesus christ why does python not have a generic avg fxn...

# Determine Final Weight
    if(final_weightage<alpha_a):
        return final_weightage
    else:
        return mean([final_weightage,alpha_a])
