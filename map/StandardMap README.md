# Using the Code
This repository is organized into three main Python modules:

- `map/standardMap.py` — defines the `StandardMap` class, which runs simulations of the Chirikov standard map and stores results in a list of runs (`runs`).
- `plots/mapEval.py` — defines the `MapEvaluator` class, which provides helper methods to extract data from `StandardMap.runs` for plotting (tails, phase space, I–K diagnostic samples).
- `plots/mapPlot.py` — contains plotting utilities for phase–space plots and \(IK\) diagnostic sweeps.

Scripts should be run from the repository root so that imports (e.g., `from map.standardMap import StandardMap`) resolve correctly.

## Getting Started

See [this section](README.md) on setting up your environment.

## Using `StandardMap` from the Command Line

