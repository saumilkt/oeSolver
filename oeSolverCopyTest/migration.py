def ascertain_migration_data(s):
	S=[]
	for i in range(0,10):
		if(i%2==0):
			S.append(s[i])
	spring(S)
	summer(S)
	fall(S)
	winter(S)

def spring(S):
	print("Spring: ")
	for i in range(1,5):
		lPop= (3/11)*S[i]
		mPop= (5/11)*S[i]
		mPopLast=(5/11)*S[i-1]
		dL = 0.1598*mPopLast - (0.03571+0.1150)*lPop # alpha_1*M_i_minus_1 - (gamma+mu_1)*L_i
		dM = 0.03571*lPop - 0.07143*mPop# gamma*L - mu_2*M_i
		print("dLi/dt: "+str(dL))
		print("dMi/dt: "+str(dM))
		print(" ")

def summer(S):
	print("Summer: ")
	for i in range(1,5):
		lPop= (3/11)*S[i]
		mPop= (5/11)*S[i]
		dL = -(0.03571+0.1150)*lPop # -(gamma+u_1)*L_in
		dM = 0.03571*lPop -0.005*mPop # gamma*L_in - mu_3*M_in
		print("dLin/dt: "+str(dL))
		print("dMin/dt: "+str(dM))
		print(" ")

def fall(S):
	print("Fall: ")
	for i in range(1,5):
		mPop= (5/11)*S[i]
		dM = 0.0056*mPop # -mu_fin*M_fin
		print("dMfin/dt: "+str(dM))
		print(" ")

def winter(S):
	print("Winter: ")
	for i in range(1,5):
		mPop= (5/11)*S[i]
		dM = 0.0042*mPop # -mu_w*M_w
		print("dMw/dt: "+str(dM))
		print(" ")


"""
Spring Migration (Part One):
dLidt= 1Mi-1 - ( + 1)Li 
dMidt= Li-2Mi

Li = population of larvae in the ith generation
Mi= population of monarch adults in the ith generation
1 = 0.1598 = growth rate of larvae
 = 0.03571= maturation rate of larvae
1= 0.1150 = death rate of larvae
2= 0.07143= death rate of adult monarchs
"""
"""
Summer Stay (Part Two):
dLindt= -( + 1)Lin 
dMindt= Lin-2Min
dLsdt= 2Min - ( + 1)Ls 
dMsdt= Ls-3Ms

Lin = population of larvae in the last generation of Part One
Min= population of monarch butterflies in the last generation of Part One
Ls = population of larvae in reproductive diapause
Ms= population of monarch adults in reproductive diapause
2 = 2.600 = growth rate of larvae with monarchs
 = 0.03571= maturation rate of larvae
1= 0.1150 = death rate of larvae
2= 0.07143= death rate of later monarchs
3= 0.005= death rate of non-reproductive monarchs
"""
"""
Fall Migration (Part Three):
dMfindt= -finMfin

Mfin= population of migrant monarch adults
fin= 0.0056= death rate of migrant monarch adults
"""
"""
Winter Hibernation (Part Four):
dMwdt= -wMw

Mw= population of overwintering monarch adults
w= 0.0042= death rate of overwintering monarch adults
"""