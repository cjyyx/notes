import numpy as np

alpha=1
pi_f=4
M_0=0.9
T_0=217
pi_c=20
T_t4=1670
C_p=1004
gamma=1.4
Delta_h_c=4.28e7

R=(gamma-1)/gamma*C_p
print(f"R={R}")

a_0=np.sqrt(gamma*R*T_0)
print(f"a_0={a_0}")

tau_r=1+(gamma-1)/2*M_0**2
print(f"tau_r={tau_r}")

tau_lambda=T_t4/T_0
print(f"tau_lambda={tau_lambda}")

tau_c=pi_c**((gamma-1)/(gamma))
print(f"tau_c={tau_c}")

tau_f=pi_f**((gamma-1)/(gamma))
print(f"tau_f={tau_f}")

tau_t=1-(tau_r/tau_lambda)*(tau_c-1+alpha*(tau_f-1))
print(f"tau_t={tau_t}")

u_9=a_0*np.sqrt(2/(gamma-1)*(tau_lambda/(tau_c*tau_r))*(tau_t*tau_c*tau_r-1))
print(f"u_9={u_9}")

u_19=a_0*np.sqrt(2/(gamma-1)*(tau_f*tau_r-1))
print(f"u_19={u_19}")

T_9=T_0*tau_lambda/(tau_r*tau_c)
print(f"T_9={T_9}")

T_19=T_0
print(f"T_19={T_19}")

Fpdotm=(a_0/(1+alpha))*(u_9/a_0-M_0+alpha*(u_19/a_0-M_0))
print(f"Fpdotm={Fpdotm}")

f=(C_p*T_0/(Delta_h_c))*(tau_lambda-tau_r*tau_c)
print(f"f={f}")

S=f/((1+alpha)*Fpdotm)
print(f"S={S}")