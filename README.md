# CSPC - Computer Science for Physics and Chemistry

My coursework repository. Each practical is under `PW1/Lab A/` and `PW1/Lab B/`.

## Setup

Create the environment for Lab A:

```bash
conda env create -f "PW1/Lab A/environment.yml"

conda activate cspc
```

---

## PW1 - Lab A: Reproducible Foundations

Computer Science for Physics and Chemistry PW1 – Lab A

**What I built:**

* Radioactive decay simulation using Python and NumPy.
* Tests for the simulation and a speed comparison between the two versions.

**Speed comparison (loop vs NumPy):**

* loop: 3.97 s
* numpy: 0.000279 s
* speed-up: 14213.65 x faster

**Tests:** all passing? yes

**Conclusion:**

The simulation and tests worked. The NumPy version was much faster than the loop version. I also got more familiar with using Git, Conda and pytest.

---

## PW1 - Lab B: Decay Analysis and Snakemake

**What I built:**

* Compared observed radioactive decay data with the analytical exponential decay law.
* Created a plot showing the observed data and the analytical prediction.
* Created a Snakemake pipeline to automate the generation of the figure.

**What the data showed:**

The observed decay data showed the expected decrease over time. The observed data generally matched the analytical exponential decay law, with small differences between the observations and the analytical curve.

**Snakemake pipeline:**

The Snakemake pipeline uses `decay_observed.csv` as the input and runs `plot.py` to generate `figure.png`. This makes the plotting process reproducible and automatically tracks the input and output files.

**Conclusion:**

Lab B extended the decay simulation from Lab A by comparing simulated analytical behaviour with observed data and using Snakemake to automate the analysis workflow.
