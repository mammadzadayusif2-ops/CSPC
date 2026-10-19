# CSPC - Computer Science for Physics and Chemistry

My coursework repository. Each practical is organized under its corresponding lab directory.

## Setup

Create the environment for PW1 Lab A:

```bash
conda env create -f "PW1/Lab A/environment.yml"
conda activate cspc
```

---

## PW1 - Lab A: Reproducible Foundations

**What I built:**

- Radioactive decay simulation using Python and NumPy.
- Tests for the simulation and a speed comparison between the two implementations.

**Speed comparison (loop vs NumPy):**

- Loop: 3.97 s
- NumPy: 0.000279 s
- Speed-up: approximately 14,213.65×

**Tests:** All passing.

**Conclusion:**

The simulation and tests worked. The NumPy implementation was much faster than the loop implementation. I also gained experience with Git, Conda, and pytest.

---

## PW1 - Lab B: Decay Analysis and Snakemake

**What I built:**

- Compared observed radioactive decay data with the analytical exponential decay law.
- Created a plot showing the observed data and the analytical prediction.
- Created a Snakemake pipeline to automate figure generation.

**What the data showed:**

The observed decay data decreased over time and generally followed the analytical exponential decay curve, with small differences between the observations and the prediction.

**Snakemake pipeline:**

The pipeline uses `decay_observed.csv` as input and runs `plot.py` to generate `figure.png`. This makes the plotting process reproducible and tracks the input and output files.

**Conclusion:**

Lab B extended the decay work from Lab A by comparing observed data with the analytical model and automating the analysis workflow using Snakemake.

---

## PW2 - Lab A: Motion from Tracking Data

**What I built:**

- Loaded noisy free-fall position measurements from `freefall.csv`.
- Calculated velocity by differentiating position with respect to time.
- Calculated acceleration by differentiating velocity with respect to time.
- Integrated acceleration to recover velocity and then integrated velocity to recover position.
- Compared the recovered velocity and position with the original values.
- Created a figure with three stacked panels sharing the time axis.

**What the data showed:**

The mean acceleration was compared with the expected gravitational acceleration of approximately −9.81 m/s². Individual acceleration estimates fluctuated considerably because of measurement noise.

The largest difference between the recovered and original values was **0.7845625**.

**Why acceleration was noisy:**

Differentiating noisy position measurements twice amplifies measurement noise, causing large fluctuations in the individual acceleration estimates even when the position data appears smooth.

**Conclusion:**

This practical demonstrated numerical differentiation and integration using NumPy and SciPy. Despite the noisy acceleration estimates, integrating acceleration back to velocity and position allowed comparison with the original data. The largest difference between the recovered and original values was approximately 0.785.

---

## PW2 - Lab B: Optimization in Chemistry

### Part 2: Three Routes to a Minimum

Compared gradient descent, Newton's method, and the SLSQP optimizer using two mathematical functions.

**Part 2A — Easy convex function**

Minimized the function

f(x) = (x − 3)² + 1

using all three methods, starting from x₀ = 0.

All three methods converged to approximately x = 3, the global minimum of the function.

**Part 2B — A harder landscape**

Minimized the function

g(x) = x⁴ − 3x² + x + 5

using the same three methods, starting from x₀ = 0 and x₀ = 2.

The function has multiple stationary points, so the methods do not necessarily converge to the same result. Gradient descent depends on the learning rate and starting point, while Newton's method can converge to either a minimum or a maximum. The second derivative was used to classify the stationary point found by Newton's method.

The results demonstrated that the starting point and optimization algorithm can affect convergence and the solution obtained.

### Part 3: Chemistry 1 — Fitting a Reaction Rate

**What I built:**

- Loaded time and concentration measurements from `kinetics.csv`.
- Used the first concentration measurement as the initial concentration C₀.
- Defined an error function comparing the measured concentrations with the first-order decay model.
- Used `scipy.optimize.minimize` with the SLSQP method and bounds of 0 to 5 to estimate the rate constant k.
- Plotted the measured data and the fitted exponential decay curve.

The concentration model is

C(t) = C₀e⁻ᵏᵗ

The fitted rate constant was expected to be close to **0.25**.

**Output:** `kinetics.png`

### Part 4: Chemistry 2 — Chemical Equilibrium

Considered the reversible reaction

H₂ + I₂ ⇌ 2HI

Starting with 1 mol each of H₂ and I₂, the amounts at reaction extent x are

- H₂ = 1 − x
- I₂ = 1 − x
- HI = 2x

For the equilibrium constant K = 15.6, the equilibrium condition is

K = (2x)² / ((1 − x)(1 − x))

**Methods used:**

- Newton's method (`scipy.optimize.newton`) to find the root of the equilibrium imbalance function.
- SLSQP minimization (`scipy.optimize.minimize`) to minimize the squared equilibrium imbalance.

Both methods gave approximately the same equilibrium extent:

**Equilibrium extent:** x ≈ 0.664 mol

**Equilibrium composition:**

| Substance | Amount at equilibrium |
|---|---:|
| H₂ | 0.336 mol |
| I₂ | 0.336 mol |
| HI | 1.328 mol |

The results show that the reactant amounts decrease as the reaction proceeds, while the amount of HI increases.

**Output:** `equilibrium.png`

### Part 5: Chemistry 3 — Titration Equivalence Point (Bonus)

**What I built:**

- Loaded the volume of base added and the corresponding pH measurements from `titration.csv`.
- Used `numpy.gradient` to estimate the slope of the pH curve with respect to volume.
- Used `numpy.argmax` to find the index at which the slope is largest.
- Identified the corresponding volume as the estimated equivalence point.
- Created two plots side by side: the titration curve and its slope.
- Marked the estimated equivalence point on both plots.

The equivalence point is estimated as the volume at which the pH changes most rapidly.

**Result:** The equivalence point was expected to be approximately **50 mL**, where the pH curve rises sharply and its slope reaches a maximum.

**Output:** `titration.png`

### Conclusion

This practical demonstrated how numerical optimization can be applied to mathematical functions and chemistry problems. Gradient descent, Newton's method, and SLSQP were compared to understand how optimization methods behave under different conditions.

The chemistry applications covered fitting a reaction rate, calculating chemical equilibrium, and estimating a titration's equivalence point using numerical differentiation. NumPy and SciPy provided the numerical tools, while Matplotlib was used to visualize the results.