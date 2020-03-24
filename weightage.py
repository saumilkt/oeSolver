from random import randint


weights = [.01,.07,.36,.56]
def alpha_a_weightage(population, alpha_a):
    hold = []
    n=0
    m=0
    l=0
    s=0
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
    print(n+' '+ weight*population +' ' + population)
    print(l+' '+ weight*population +' ' + population)
    print(m+' '+ weight*population +' ' + population)
    print(s+' '+ weight*population +' ' + population)
alpha_a_weightage(500,.1)
