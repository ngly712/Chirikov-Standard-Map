# Analyzing the Chaotic Behavior of the Chirikov-Taylor Map
### By: Nguyen Ly, Enrique Lopez, Carlos Solis, and Hazel Moore.

# Table of Contents
A

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

To a layperson, chaos is a “state of utter confusion” where “chance is supreme” [1]. In mathematics, however, chaos encapsulates the sensitive nature of systems entirely determined by mathematical laws. Dr. Robert L. Devaney introduced three main traits of chaotic systems: their sensitivity to initial conditions, topological transitivity, and dense periodic orbits [2].

## Sensitivity to Initial Conditions

The term “sensitivity” denotes how even a slight change in the initial conditions would yield dramatically different behavior. The "double pendulum" below is a classic example of this.

<img src=https://upload.wikimedia.org/wikipedia/commons/c/c8/3-double-pendulums.gif alt="double-pendulum-different-IC" style="display:block; margin:0 auto; max-width:100%; height:auto;">

Sensitivity is numerically described by the Lyapunov exponents ($\lambda$), a set of parameters equal to the number of degrees of freedom in a dynamical system (the dimension of the phase space). The largest $\lambda$ of the spectrum denotes the dominant behavior of the system from a uniform perturbation of all $q_i$; a nonnegative value indicates chaos when the solution lies in a finite region as opposed to pure exponential growth.

Parallel to this definition is the Lyapunov time, the inverse of the largest Lyapunov exponent. This characteristic time scale denotes the minimum time before a system becomes chaotic [3].

## Topological Transivity

A system's “topological transitivity” refers to the impossibility of defining a clear boundary for the system's trajectory from a range of finite initial conditions. Formally, the mapping $f:X\to X$ is topologically transitive if, for any pair of non-empty open sets $U,V\in X$, there exists a positive $k$ such that $f^k(U)\cap V\neq \empty$. This means that any point in $U$ (assumed not to be in $V$) will eventually enter $V$ after being iterated upon by $f$ enough times. Therefore, defining any pair of separated open sets $U$ and $V$ is impossible [4].

<p align='center'>
<b>Topological mixing of the logistic map after six iterations</b> [7]
</p>
<img src=https://upload.wikimedia.org/wikipedia/commons/6/6a/LogisticTopMixing1-6.gif alt="logistic-set-mixing" style="display:block; margin:0 auto; max-width:30%; height:auto;">

## Dense Periodic Orbits

Finally, a system has “dense periodic orbits” if a periodic orbit approaches every point in the system’s range arbitrarily closely [4]. The italicized terms emphasize that no path ever traces itself more than once, but it may trace over nearby points to form regions of attraction.

<p align='center'>
<b>Animation of the Lorentz Attrator</b> [8]
</p>
<img src=https://upload.wikimedia.org/wikipedia/commons/1/1e/Lorenz_attractor_in_Julia.gif?20230817224607 alt="logistic-set-mixing" style="display:block; margin:0 auto; max-width:30%; height:auto;">

Sometimes, the presence of the last two traits implies sensitivity. A weaker sense of the definition uses only the first two traits to identify chaos in a system [5].

# The Standard Map

The Taylor-Greene-Chirikov Map, or Standard Map, is a two-dimensional discrete-time recurrence relation that exhibits chaotic behavior. The system is as follows [6]:

> <p align="center">
> $I_{n+1} = (I_n + K\sin\theta_n) \bmod 2\pi$
> </p>
> <p align="center">
> $\theta_{n+1} = (\theta_n + I_{n+1}) \bmod 2\pi$
> </p>

$I$ and $\theta$ are periodic real-valued variables within $[0, 2\pi)$, while $K$ is a nonnegative real number. The exact value of $K$ that results in chaotic behavior is not known, but several papers ([here](https://arxiv.org/pdf/2509.11593) and [here](https://pubs.aip.org/aip/jmp/article-abstract/20/6/1183/449401/A-method-for-determining-a-stochastic-transition?redirectedFrom=fulltext), for example) have attempted to identify a reasonable bound for the coefficient.

This chaotic mapping is surprisingly commonplace (hence the *Standard* moniker), appearing in:
- the dynamics of charged particles in mirror magnetic traps [9]
- the dynamics particle accelerators [10]
- the dynamics of Solar System comets [11]
- the microwave ionization of Rydberg atoms [12]
and much more.

## Properties

The Standard Map is an **area-preserving** map

# Current Code Structure (Updated 12/09/2025)
```
map/
└── standardMap.py
└── StandardMap README.md
plots/
└── mapEval.py
└── mapPlot.py
└── Plots README.md
results/
└── csvs/
    └── K-0.2-len-x.csv
    └── K-0.6-len-x.csv
    └── K-0.97-len-x.csv
    └── K-1.2-len-x.csv
    └── K-2.0-len-x.csv
└── plots/
    └── K0.2.png
    └── K0.6.png
    └── K0.97.png
    └── K1.2.png
    └── K2.0.png
└── presentation/
    └── Chirikov-Taylor Map.pdf
└── tests/
    └── test_mapEvaluator.py
    └── test_standardMap.py
LICENSE
README.md
setup.py
```

The `map` folder contains the Standard Map simulator and its instruction manual.
- `standardMap.py` is the class that houses the Standard Map.
- `StandardMap README.md` provides guidance on how to use the command-line interface features of the class.

The `plots` folder contains utility functions for plotting the results of the simulator and an accompanying instruction manual.
- `mapEval.py` is the class that processes the data from the Standard Map class.
- `mapPlot.py` holds the plotting functions for the phase space plots and I–K diagnostic diagrams.
- `Plots README.md` provides more examples for generating plots.

The `results` folder houses the main outputs of this README's code. This is split into three subfolders:
- The `plots` subfolder has PNGs of the various plots.
- The `csvs` subfolder stores the raw data produced by the Standard Map class.
- The `presentation` folder is where the in-class presentation is located.

The `tests` folder contains unit tests for all Python files. These tests use the [PyTest](https://docs.pytest.org/en/stable/) module.
- `test_standardMap.py` is for the unit tests associated with the Standard Map class.
- `test_mapEvaluator.py` is for the unit tests associated with the evaluator class.

# Future Directions
In regards to code improvement, several changes would be favorable:
- merging the two classes into one to reduce the number of redundant variables
- adding support for other file formats (.xlsx, .txt, .bin)
- merging runs with identical kick values and RNG seeds
As for theoretical exploration, the following ideas arise:
- expand to the classical [kicked rotator](https://www.sciencedirect.com/science/article/pii/S0960077905005485?via%3Dihub) system upon which the Standard Map is derived
- apply the Standard Map to the physical examples listed [above](#The-Standard-Map)
- study the [Kolmogorov-Sinai Entropy](https://mathworld.wolfram.com/KolmogorovEntropy.html) of the system

# References

1. Merriam-Webster, "Chaos," retrieved April 3, 2025, https://www.merriam-webster.com/dictionary/chaos
2. Hasselblatt, Boris, Katok, Anatole, *A First Course in Dynamics: With a Panorama of Recent Developments*, (Cambridge University Press, 2003)
3. Weisstein, Eric W., "Lyapunov Characteristic Exponent," retrieved April 3, 2025, https://mathworld.wolfram.com/LyapunovCharacteristicExponent.html
4. Devaney, Robert L., *An Introduction to Chaotic Dynamical Systems* (2nd ed.), (Westview Press, 2003)
5. Medio, Alfredo, Lines, Marji, *Nonlinear Dynamics: A Primer*, (Cambridge University Press, 2001), p. 165
6. Weisstein, Eric W. "Standard Map." From MathWorld &mdash; A Wolfram Resource. https://mathworld.wolfram.com/StandardMap.html
7. N3kromancer732, CC BY-SA 4.0, https://creativecommons.org/licenses/by-sa/4.0, via Wikimedia Commons
8. Fincho64, CC BY-SA 4.0, https://creativecommons.org/licenses/by-sa/4.0, via Wikimedia Commons
9. B.V.Chirikov, "Resonance processes in magnetic traps", At. Energ. 6: 630 (1959).
10. F.M.Izraelev, "Nearly linear mappings and their applications", Physica D 1(3): 243 (1980).
11. T.Y.Petrosky, "Chaos and cometary clouds in the solar system", Phys. Lett. A 117(7): 328 (1986).
12. G.Casati, I.Guarneri, D.L.Shepelyansky, "Hydrogen atom in monochromatic field: chaos and dynamical photonic localization", IEEE J. of Quant. Elect. 24: 1420 (1988).

# Credits
- Nguyen: `standardMap.py` class structure, utility functions, unit tests, front page README, and StandardMap README
    - helped with the in-class presentation
- Hazel: in-class presentation
- Enrique: `mapEval.py` class structure, utility functions, unit tests, and README plots
    - helped with the `mapPlot.py` script
- Carlos: `mapPlot.py` script
    - helped with the `mapEval.py` class structure

This started as a project for PHY 329 (Computational Physics) at UT Austin ([class website](https://www.wgilpin.com/cphy/)). The presentation we gave in-class on this repository is under `results/presentation`. Special thanks to Dr. William Gilpin (wgilpin@utexas.edu) for being an outstanding instructor and Alex Schmidt (alexcschmidt17@gmail.com) for being a supportive TA!