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

* Radioactive decay simulation using Python and NumPy.
* Tests for the simulation and a speed comparison between the two implementations.

**Speed comparison (loop vs NumPy):**

* Loop: 3.97 s
* NumPy: 0.000279 s
* Speed-up: approximately 14,213.65×

**Tests:** All passing.

**Conclusion:**

The simulation and tests worked. The NumPy implementation was much faster than the loop implementation. I also gained experience with Git, Conda, and pytest.

---

## PW1 - Lab B: Decay Analysis and Snakemake

**What I built:**

* Compared observed radioactive decay data with the analytical exponential decay law.
* Created a plot showing the observed data and the analytical prediction.
* Created a Snakemake pipeline to automate figure generation.

**What the data showed:**

The observed decay data decreased over time and generally followed the analytical exponential decay curve, with small differences between the observations and the prediction.

**Snakemake pipeline:**

The pipeline uses `decay_observed.csv` as input and runs `plot.py` to generate `figure.png`. This makes the plotting process reproducible and tracks the input and output files.

**Conclusion:**

Lab B extended the decay work from Lab A by comparing observed data with the analytical model and automating the analysis workflow using Snakemake.

---

## PW2 - Lab A: Motion from Tracking Data

**What I built:**

* Loaded noisy free-fall position measurements from `freefall.csv`.
* Calculated velocity by differentiating position with respect to time.
* Calculated acceleration by differentiating velocity with respect to time.
* Integrated acceleration to recover velocity and then integrated velocity to recover position.
* Compared the recovered velocity and position with the original values.

**What the data showed:**

The mean acceleration was close to the expected value of −9.81 m/s², but the individual acceleration estimates fluctuated considerably.

The largest difference between the recovered and original values was **0.7845625**.

**Why acceleration was noisy:**

Differentiating noisy position measurements twice amplifies measurement noise, causing large fluctuations in the individual acceleration estimates even when the position data appears smooth.

**Conclusion:**

This practical demonstrated numerical differentiation and integration using NumPy and SciPy. Despite the noisy acceleration estimates, integrating acceleration back to velocity and position allowed comparison with the original data. The largest difference between the recovered and original values was approximately 0.785.
