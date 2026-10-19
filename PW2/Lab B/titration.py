"""
PW2 Lab B Part 5 (bonus) -- find a titration's equivalence point.

titration.csv holds a titration curve: pH versus the volume of base added.
The equivalence point is the volume where the pH changes fastest (the steep
jump). Numerically, that is where the SLOPE of the pH curve is largest.
Run:  python titration.py
"""
import numpy as np
import matplotlib.pyplot as plt

# TODO 1: read titration.csv (columns volume_base, pH) into arrays V, pH.

v,ph=np.loadtxt("titration.csv",skiprows=1,delimiter=",",unpack=True)



# TODO 2: compute the slope of the pH curve with np.gradient(pH, V), and find
#         the volume where that slope is largest (np.argmax). That is the
#         equivalence point. Print it.

slope=np.gradient(ph,v)
ind=np.argmax(slope)
print("Equivalence point:",v[ind])





# TODO 3: make two plots side by side: (left) pH vs volume with a line at the
#         equivalence point; (right) the slope vs volume, showing it peaks
#         at the equivalence point. Save as titration.png.

fig,ax=plt.subplots(1,2)


ax[0].plot(v,ph)
ax[0].axvline(v[ind], linestyle="--", color="red")
ax[0].set_xlabel("PH")
ax[0].set_ylabel("Volume")
ax[0].set_title("Titration")

ax[1].plot(v, slope)
ax[1].axvline(v[ind], linestyle="--", color="red")
ax[1].set_xlabel("Volume")
ax[1].set_ylabel("Slope")
ax[1].set_title("Slope of Titration")

plt.savefig("titration.png")