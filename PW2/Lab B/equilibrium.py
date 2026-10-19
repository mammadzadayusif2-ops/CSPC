"""
PW2 Lab B Part 4 -- chemical equilibrium via the equilibrium constant K.

Reaction  H2 + I2 <=> 2 HI, starting from 1 mol H2 and 1 mol I2.
As the reaction proceeds by an extent x:  H2 = 1-x,  I2 = 1-x,  HI = 2x.
At equilibrium the composition satisfies the equilibrium constant
        K = [HI]^2 / ([H2][I2]) = (2x)^2 / ((1-x)(1-x)).
Given K, find the extent x. Solve it TWO ways and compare.
Run:  python equilibrium.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize

K = 15.6
a = b = 1.0

# TODO 1: write k_imbalance(x) = (2x)^2/((a-x)(b-x)) - K.
#         It equals zero exactly at equilibrium.

def k_imbalance(x):
    return (2*x)**2/((a-x)*(b-x))-K


# TODO 2 (method 1): use scipy.optimize.newton to find the root of k_imbalance
#         (start x0=0.5). This is root-finding.

xnew=newton(k_imbalance,x0=0.5)

# TODO 3 (method 2): use scipy.optimize.minimize to minimise k_imbalance(x)**2
#         (method "SLSQP", bounds [(0, 0.999)], x0=[0.5]). Print both answers
#         and confirm they agree.

def method2(x):
    return k_imbalance(x[0])**2

x=minimize(method2,method="SLSQP",bounds=[(0,0.999)],x0=[0.5])
xmin=x.x[0]

print("Newton's method:", xnew)
print("Minimization:", xmin)

# TODO 4: report the equilibrium amounts (H2, I2, HI), and plot how the three
#         amounts change with the extent x, marking the equilibrium. Save
#         equilibrium.png.

H2 = a - xnew
I2 = b - xnew
HI = 2 * xnew

print("H2:", H2)
print("I2:", I2)
print("HI:", HI)


extent = np.linspace(0, 0.999, 500)

H2_values = a - extent
I2_values = b - extent
HI_values = 2 * extent

plt.plot(extent, H2_values, label="H2")
plt.plot(extent, I2_values, label="I2")
plt.plot(extent, HI_values, label="HI")

plt.axvline(xnew, color="black", linestyle="--", label="Equilibrium")

plt.xlabel("Reaction extent x (mol)")
plt.ylabel("Amount (mol)")
plt.title("Chemical Equilibrium")


plt.savefig("equilibrium.png")
