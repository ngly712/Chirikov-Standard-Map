# Using the Code
This repository is organized into three main Python modules:

- `map/standardMap.py` — defines the `StandardMap` class, which runs simulations of the Chirikov standard map and stores results in a list of runs (`.runs`).
- `plots/mapEval.py` — defines the `MapEvaluator` class, which provides helper methods to extract data from `StandardMap.runs` for plotting (tails, phase space, I–K diagnostic samples).
- `plots/mapPlot.py` — contains plotting utilities for phase–space plots and \(IK\) diagnostic sweeps.

Scripts should be run from the repository root so that imports (e.g., `from map.standardMap import StandardMap`) resolve correctly.

## Getting Started

Follow these steps to set up your environment and install the required packages (NumPy, MatplotLib).

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

## Using `StandardMap` from the Command Line

