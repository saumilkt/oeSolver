# OE Infection modeling
import weightage as weight
import migration as migrator
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
plt.ioff()
plt.ion()
plt.rcParams['figure.figsize'] = 10, 8

# initial conditions
N0 = 500. # initial population
y0 = [N0] # initial condition vector
t  = np.linspace(0, .05, 11) # time grid initialy 0 5. 1000
# @vars
a = 50.000  # birth rate
bi = 12.8000  # Desity-independent death percent (per day)
bd = 0.1000  # Desity-dependent death percent  (per day)
I = .12*N0  # resurect percent (per day)
v = 0.9000  # rate of maternal transmission
alpha_i_base = 0.2 # pre-adult virulence (standard) ***rename to alpha_i_base when parametric study in effect
alpha_a = 0.1 # adult virulence (standard) ***rename to alpha_a_base when parametric study in effect

"""# alpha_a_parametric
alpha_a = weight.alpha_a_weightage(int(I), alpha_a_base) # adult virulence (parametric)
alpha_a1 = weight.alpha_a_weightage(int(I), alpha_a_base) # adult virulence (parametric)
alpha_a2 = weight.alpha_a_weightage(int(I), alpha_a_base) # adult virulence (parametric)
"""
# alpha_i_parametrics
alpha_i = weight.alpha_a_weightage(int(I), alpha_i_base) # adult virulence (parametric)
alpha_i1 = weight.alpha_a_weightage(int(I), alpha_i_base) # adult virulence (parametric)
alpha_i2 = weight.alpha_a_weightage(int(I), alpha_i_base) # adult virulence (parametric)

# solve the system dy/dt = f(y, t)
def f(N, t):
     Ni = N[0]
     # the model equation (see Altizer et al. 2004)
     f0 = Ni*(a-bi-bd*Ni)-I*((1+a*(v*alpha_i-1))+alpha_a)
     print(f0)
     return [f0]

def f1(N, t):
     Ni = N[0]
     # the model equation (see Altizer et al. 2004)
     f0 = Ni*(a-bi-bd*Ni)-I*((1+a*(v*alpha_i1-1))+alpha_a)
     print(f0)
     return [f0]

def f2(N, t):
     Ni = N[0]
     # the model equation (see Altizer et al. 2004)
     f0 = Ni*(a-bi-bd*Ni)-I*((1+a*(v*alpha_i2-1))+alpha_a)
     print(f0)
     return [f0]

def fcontrol(N, t): # remove if not implementing parametric study
     Ni = N[0]
     # the model equation (see Altizer et al. 2004)
     f0 = Ni*(a-bi-bd*Ni)-I*((1+a*(v*alpha_i_base-1))+alpha_a)
     print(f0)
     return [f0]

# solve the DEs
soln = odeint(f, y0, t)
soln1 = odeint(f1, y0, t)
soln2 = odeint(f2, y0, t)
solnC = odeint(fcontrol, y0, t)
S = soln[:, 0]
S1 = soln1[:, 0]
S2 = soln2[:, 0]
SC = solnC[:, 0]



# plot results
plt.figure()
plt.plot(t, S, label='alpha_i= '+str(alpha_i))
plt.plot(t, S1, label='alpha_i= '+str(alpha_i1))
plt.plot(t, S2, label='alpha_i= '+str(alpha_i2))
plt.plot(t, SC, label='Control: alpha_i_base= '+str(alpha_i_base))
plt.xlabel('Timesteps')
plt.ylabel('Population')
plt.title('Effect of differring Virulence levels on Monarch Butterfly Population over Time')
plt.legend(loc='upper right')
plt.show()
plt.savefig('plot.png')
print(S)
for i in range(0,10):
     if(i%2==0):
          print(S[i])
print(S1)
print(S2)
print(SC)
migrator.ascertain_migration_data(S)
