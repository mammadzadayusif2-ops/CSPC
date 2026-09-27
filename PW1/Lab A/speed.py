import time 
from decay import simulate,simulate_loop
N0=200000
lam=0.4
dt=0.05
steps=200
seed=0

firstime_pyton=time.perf_counter()
simulate_loop(N0,lam,dt,steps,seed)
secondtime_python=time.perf_counter()

python_time=secondtime_python-firstime_pyton

firsttime_numpy=time.perf_counter()
simulate(N0,lam,dt,steps,seed)
secondtime_numpy=time.perf_counter()
numpy_time=secondtime_numpy-firsttime_numpy

print("Python:",python_time,"seconds")
print("NumPy:",numpy_time,"seconds")
print("NumPy is",python_time/numpy_time,"times faster")