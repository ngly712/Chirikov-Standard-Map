Here is the code used to create the plots in the `results/plots` folder.

```python
import numpy as np
from map.standardMap import StandardMap
from plots.mapEval import MapEvaluator
from plots.mapPlot import plot_phase_tail

K_values = [0.2, 0.6, 0.97, 1.2, 2.0]

n_iters = 3500     # Iterations per orbit
n_orbits  = 200    # Number of orbits per K (initial conditions)

# Create a StandardMap object
aMap = StandardMap(nIters = n_iters)  # K will be set in the loop

for K in K_values:
    aMap.K = K
    aMap.simulate(ic = n_orbits) # Append a run with this K to aMap.runs

mEval = MapEvaluator(aMap.runs)  # Create a MapEvaluator object

n_tail = 1000                    # Number of late-time points per orbit to plot

for idx, K in enumerate(K_values):
    title = rf"Standard Map Phase Space, $K = {K}$"

    plot_phase_tail(
        evaluator = mEval,
        run_idx = idx,
        n_tail = n_tail,
        point_size = 0.1,
        title = title,
    )
```