# Using the Code
This repository is organized into three main Python modules:

- `map/standardMap.py` — defines the `StandardMap` class, which runs simulations of the Chirikov standard map and stores results in a list of runs (`runs`).
- `plots/mapEval.py` — defines the `MapEvaluator` class, which provides helper methods to extract data from `StandardMap.runs` for plotting (tails, phase space, I–K diagnostic samples).
- `plots/mapPlot.py` — contains plotting utilities for phase–space plots and \(IK\) diagnostic sweeps.

Scripts should be run from the repository root so that imports (e.g., `from map.standardMap import StandardMap`) resolve correctly.

## Getting Started

See [this section](README.md) on setting up your environment. Step 6 can be done directly from the Python shell; the examples below build upon each other and assume that this was the case.

## Using `StandardMap` from the Command Line Interface

### Creating a New Run and Saving It

```python
aMap = sMap(K=2.5, nIters=1000) # Initialize the object

aMap.simulate(ic=5) # Simulate 5 random initial conditions

print(aMap) # Show summary of runs

aMap.write(name="my_first_run") # Save results to CSV
```

### Changing the Current State

```python
# Change the parameters of the next run
aMap.K = 0.8
aMap.nIters = 500
aMap.seed = 42

aMap.simulate(ic=3) # Simulate 3 random initial conditions

print(aMap) # Show summary of runs

aMap.write(run=-1) # Save most recent run to CSV
```

### Resetting the Slate

```python
aMap.clearRuns() # Remove all runs

print(aMap) # Still remembers the current K, nIters, and seed

aMap.read("my_first_run.csv") # Read in the saved run from earlier

print(aMap) # Show summary of runs
```

