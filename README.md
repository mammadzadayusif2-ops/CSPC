# CSPC - Computer Science for Physics and Chemistry

My coursework repository. Each practical is under `PW<n>/Lab <X>/`.

## Setup

Create the environment for a given lab:

```bash
conda env create -f PW<n>/Lab\ <X>/environment.yml
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
