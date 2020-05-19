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
