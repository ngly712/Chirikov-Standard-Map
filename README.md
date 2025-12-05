# Analyzing the Chaotic Behavior of the Chirikov Map
The [Taylor-Greene-Chirikov Map](https://mathworld.wolfram.com/StandardMap.html), or Standard Map, is a two-dimensional discrete-time recurrence relation that exhibits chaotic behavior. The system is as follows:

> <p align="center">
> $I_{n+1} = (I_n + K\sin\theta_n) \bmod 2\pi$
> </p>
> <p align="center">
> $\theta_{n+1} = (\theta_n + I_{n+1}) \bmod 2\pi$
> </p>

$I$ and $\theta$ are periodic real-valued variables within $[0, 2\pi)$, while $K$ is a nonnegative real number. The exact value of $K$ that results in chaotic behavior is not known, but several papers ([here](https://arxiv.org/pdf/2509.11593) and [here](https://pubs.aip.org/aip/jmp/article-abstract/20/6/1183/449401/A-method-for-determining-a-stochastic-transition?redirectedFrom=fulltext), for example) have attempted to identify a reasonable bound for the coefficient.

## Our Contributions
To experimentally determine the onset of chaos, we will implement a collection of data analysis scripts that act upon a Standard Map class instance to extract the value of $K$. These will produce Poincaré plots and phase space maps that demonstrate the formation of periodic islands littered in a dense mapping. We also generate an I–K diagnostic plot to visualize how the late-time momentum distribution changes with $K$. If time permits, we will expand the model to a classical [kicked rotator](https://www.sciencedirect.com/science/article/pii/S0960077905005485?via%3Dihub) system upon which the Standard Map is derived.

# Code Structure
`map` folder:
- `standardMap.py` will contain the class implementation of the standard map with a function to iterate from an initial condition

`plots` folder:
- `mapEval.py` will contain the class implementation for evaluating different aspects of the batch of standard map runs
- `mapPlot.py` will contain the plotting functions for the phase space plots and I–K diagnostic diagrams
- This folder will also contain plots for different values of $K$ in labeled subfolders.

`results` folder:
- These will store the raw arrays for different $K$ values as well as any miscellaneous data used in the plotting (subfolders expected).

`tests` folder:
- These will contain scripts to check the implementation of the Standard Map class. Useful for anyone who wants to modify it and see if their changes work.

`map.ipynb` will contain the top-level report on our results

# Planned Contributions
- Nguyen: writing the `standardMap.py` class structure, utility functions, and unit tests, helping with the final `map.ipynb` report
- Hazel: writing the final `map.ipynb` report, helping with the `standardMap.py` class structure
- Enrique: writing the `mapEval.py` class structure, utility functions, and unit tests, helping with the `mapPlot.py` script
- Carlos: writing the `mapPlot.py` script, helping with the `mapEval.py` class structure

## Timeline
1. Implement the `standardMap.py` class structure, utility functions, and unit tests
2. Implement the `mapEval.py` class structure, utility functions, and unit tests
3. Implement the `mapPlot.py` functions and generate the required plots
4. Generate the final report in `map.ipynb`.

Optional:

5. Implement the kicked rotator as a separate class and make the Standard Map a subclass of it.
6. Modify `mapEval.py` to account for additional variables like the kick strength and duration.
7. Perform a similar analysis of the chaotic behavior for the kicked rotator.
8. Add results to `map.ipynb`.

---

# Using the Code

This repository is organized into three main Python modules:

- `map/standardMap.py` — defines the `StandardMap` class, which runs simulations of the Chirikov standard map and stores results in a list of runs (`.runs`).
- `plots/mapEval.py` — defines the `MapEvaluator` class, which provides helper methods to extract data from `StandardMap.runs` for plotting (tails, phase space, I–K diagnostic samples).
- `plots/mapPlot.py` — contains plotting utilities for phase–space plots and \(IK\) diagnostic sweeps.

## Plotting Phase-Space Diagrams

### Import Relevant Modules

```python
from map.standardMap import StandardMap
from plots.mapPlot import plot_phase_generic
```

### Small K: Mostly Invariant Curves (KAM Tori)

```python
K = 0.2
n_iters = 5000
n_sim = 25

aMap = StandardMap(K=K, nIters=n_iters, seed=1)
aMap.simulate(ic=n_sim)
run = aMap.runs[-1]["run"]

plot_phase_generic(
    run=run,
    mode="phase",
    point_size=0.15,
    title=rf"Phase Space for $K = {K}$ ({n_sim} ICs)"
)
```

### Moderate K: Resonance Islands, Periodic Orbits, Cantori

```python
K = 0.7
n_sim = 50

aMap = StandardMap(K=K, nIters=n_iters, seed=1)
aMap.simulate(ic=n_sim)
run = aMap.runs[-1]["run"]

plot_phase_generic(
    run=run,
    mode="phase",
    point_size=0.15,
    title=rf"Phase Space for $K = {K}$ ({n_sim} ICs)"
)
```

### Large K: Mostly Chaotic Sea

```python
K = 2.0
n_sim = 100

aMap = StandardMap(K=K, nIters=n_iters, seed=1)
aMap.simulate(ic=n_sim)
run = aMap.runs[-1]["run"]

plot_phase_generic(
    run=run,
    mode="phase",
    point_size=0.15,
    title=rf"Phase Space for $K = {K}$ ({n_sim} ICs)"
)
```

## Plotting an $IK$ Diagnostic Sweep

### Import Relevant Modules + Adjust Display Settings

```python
# standard Python libraries
import numpy as np
import matplotlib.pyplot as plt
# project modules
from map.standardMap import StandardMap
from plots.mapEval import MapEvaluator
from plots.mapPlot import plot_IK_diagnostic

# matplotlib defaults (optional for nicer plots)
plt.rcParams["figure.dpi"] = 120
plt.rcParams["axes.grid"] = False
```

### Generate K Values

```python
# parameters for the IK diagnostic sweep
K_min = 0.0
K_max = 5.0
n_K   = 400            # number of K values
Ks    = np.linspace(K_min, K_max, n_K)
```

### Run Simulation

```python
n_sim   = 10          # number of ICs at each K (each set of ICs produces one orbit)
n_iters = 5000        # iterations per orbit
n_tail  = 300         # tail length for diagnostic plot
seed = 1              # seed used inside StandardMap

# generate runs via StandardMap
aMap = StandardMap(K=Ks[0], nIters=n_iters, seed=seed)

for K in Ks:
    aMap.K = K
    aMap.simulate(ic=n_sim)

# wrap runs in a MapEvaluator
evaluator = MapEvaluator(aMap.runs)

print(f"Completed {len(aMap.runs)} runs with K in [{K_min}, {K_max}].")
```

### Plot Diagnostic Sweep

```python
plot_IK_diagnostic(
    evaluator=evaluator,
    n_tail=n_tail,
    K_min=K_min,
    K_max=K_max,
    title="Standard Map I-K Diagnostic Plot",
    max_points=50_000,    # subsample for readability
    point_size=0.1,
    alpha=0.3,
)
```
