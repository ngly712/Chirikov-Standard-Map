# Using the Code
This repository is organized into three main Python modules:

- `map/standardMap.py` — defines the `StandardMap` class, which runs simulations of the Chirikov standard map and stores results in a list of runs (`.runs`).
- `plots/mapEval.py` — defines the `MapEvaluator` class, which provides helper methods to extract data from `StandardMap.runs` for plotting (tails, phase space, I–K diagnostic samples).
- `plots/mapPlot.py` — contains plotting utilities for phase–space plots and \(IK\) diagnostic sweeps.

Scripts should be run from the repository root so that imports (e.g., `from map.standardMap import StandardMap`) resolve correctly.

## Getting Started

See [this section](README.md) on setting up your environment. The examples below assume that step 6 is complete.

## Plotting Phase-Space Diagrams

### Import Plotter Function

```python
from plots.mapPlot import plot_phase_generic as pltPhase
```

### Small K: Mostly Invariant Curves (KAM Tori)

```python
K = 0.2
n_iters = 5000
n_sim = 25

aMap = sMap(K=K, nIters=n_iters, seed=1)
aMap.simulate(ic=n_sim)
run = aMap.runs[-1]["run"]

pltPhase(
    run=run,
    mode="phase",
    point_size=0.15,
    title=rf"Phase Space for $K = {K}$ ({n_sim} ICs)"
)
```

### Moderate K: Resonance Islands, Periodic Orbits, Cantori

```python
aMap.K = 0.7
n_sim = 50

aMap.simulate(ic=n_sim)
run = aMap.runs[-1]["run"]

pltPhase(
    run=run,
    mode="phase",
    point_size=0.15,
    title=rf"Phase Space for $K = {K}$ ({n_sim} ICs)"
)
```

### Large K: Mostly Chaotic Sea

```python
aMap.K = 2.0
n_sim = 100

aMap.simulate(ic=n_sim)
run = aMap.runs[-1]["run"]

pltPhase(
    run=run,
    mode="phase",
    point_size=0.15,
    title=rf"Phase Space for $K = {K}$ ({n_sim} ICs)"
)
```

## Plotting an $IK$ Diagnostic Sweep

### Import Plotting Function + Adjust Display Settings

```python
from plots.mapPlot import plot_IK_diagnostic as plotDiag
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
aMap = sMap(K=Ks[0], nIters=n_iters, seed=seed)

for K in Ks:
    aMap.K = K
    aMap.simulate(ic=n_sim)

# wrap runs in a MapEvaluator
evaluator = mEval(aMap.runs)

print(f"Completed {len(aMap.runs)} runs with K in [{K_min}, {K_max}].")
```

### Plot Diagnostic Sweep

```python
plotDiagS(
    evaluator=evaluator,
    n_tail=n_tail,
    K_min=K_min,
    K_max=K_max,
    title="Standard Map I-K Diagnostic Plot",
    max_points=50000,    # subsample for readability
    point_size=0.1,
    alpha=0.3,
)
```
