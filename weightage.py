from random import randint


weights = [.01,.07,.36,.56]
def alpha_a_weightage(population, alpha_a):
    hold = []
    n,l,m,s=0
    for _ in range(population):
        temp=randint(0,population)
        if(temp<.25*population):
            n+=1
        elif(temp<.5*population):
            l+=1
        elif(temp<.75*population):
            m+=1
        else:
            s+=1
    print(n*population)
    print(l*population)
    print(m*population)
    print(s*population)
