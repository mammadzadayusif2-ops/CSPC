"""
PW2 Lab B Part 3 -- fit a reaction's rate constant to measured data.

A first-order reaction decays as  C(t) = C0 * exp(-k*t).  You have noisy
concentration-vs-time measurements; find the k that best matches them.
Complete the TODOs. Run:  python kinetics.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# TODO 1: read kinetics.csv (columns time, concentration) into arrays t, C.
#         Set C0 = the first concentration.

t,C=np.loadtxt("kinetics.csv",delimiter=",",skiprows=1,unpack=True)
C0=C[0]

# TODO 2: write total_error(k) = sum of (measured - C0*exp(-k*t))^2.
#         This is the "how bad" number: small when the model matches the data.


def total_error(k):
    total=0
    for i in range(len(t)):
        total+=(C[i]-C0*np.exp(-k*t[i]))**2
    return total


# TODO 3: minimise total_error with scipy.optimize.minimize (method "SLSQP",
#         bounds [(0, 5)], start x0=0.5). Print the fitted k.

k=minimize(total_error,method="SLSQP",bounds=[(0,5)],x0=0.5)
print(k.x[0])



# TODO 4: plot the measured data (points) and your fitted curve (line) together.
#         Save as kinetics.png.
C_fitted = C0 * np.exp(-k.x[0] * t)

plt.scatter(t, C, label="Measured data")
plt.plot(t, C_fitted, label="Fitted curve")

plt.xlabel("Time")
plt.ylabel("Concentration")
plt.savefig("kinetics.png")
plt.show()

