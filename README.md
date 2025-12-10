# Analyzing the Chaotic Behavior of the Chirikov-Taylor Map
### Created by Nguyen Ly, Enrique Lopez, Carlos Solis, and Hazel Moore.

# Getting Started

Follow these steps to set up your environment and install the required packages (NumPy, Matplotlib).

### 1. Clone the Repository

Open a terminal and run:
```bash
git clone https://github.com/ngly712/PHY329-Final-Project.git
cd PHY329-Final-Project
```

### 2. Create a new virtual environment

**Using venv:**
```bash
python3 -m venv map
source map/bin/activate  # On Windows use: map\Scripts\activate
```

**Or using conda:**
```bash
conda create -n map
conda activate map
```

### 3. Upgrade pip (recommended)
```bash
pip install --upgrade pip
```

### 4. Install Packages
```bash
pip install numpy
pip install matplotlib
```

### 5. Install the Project in Editable Mode (optional)

This repository comes with a `setup.py` file.

If you plan to modify the code and want changes to take effect immediately, run:
```bash
pip install -e .
```
This step is optional but recommended for development.


### 6. Import Relevant Modules

```python
import numpy as np
from map.standardMap import StandardMap
```

# Introduction

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

# Credits
- Nguyen: `standardMap.py` class structure, utility functions, unit tests, front page README, and StandardMap README
    - assisted with the in-class presentation
- Hazel: in-class presentation
- Enrique: `mapEval.py` class structure, utility functions, unit tests, and README plots
    - helped with the `mapPlot.py` script
- Carlos: `mapPlot.py` script
    - helping with the `mapEval.py` class structure

This started as a project for PHY 329 (Computational Physics) at UT Austin ([class website](https://www.wgilpin.com/cphy/)). The presentation we gave in-class on this repository is under `results/presentation`. Special thanks to Dr. William Gilpin (wgilpin@utexas.edu) for being an outstanding instructor and Alex Schmidt (alexcschmidt17@gmail.com) for being a supportive TA!