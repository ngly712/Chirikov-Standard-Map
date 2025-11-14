# Unit tests using the pytest library
import numpy as np
from map import standardMap as sMap


# Planned tests:
# # Initialization:
# ## K
# ### default
# ### user
# ## nIters
# ### default
# ### user
# ## seed
# ### default
# ### user
# ## Check list properly initialized
def test_initialization_K():
    K = 0.75
    obj = sMap(K=K)
    assert obj.K == K
    K = 3
    obj = sMap(K=K)
    assert obj.K == K
    K = -1
    try:
        obj = sMap(K=K)
    except Exception:
        print("Not possible")
    else:
        raise Exception("K is invalid")


# # Simulate:
# ## I_0
# ### default
# ### user
# ## theta_0
# ### default
# ### user
# ## option - append vs replace
# ### list length check
# ### run parameters check

# # Getters and setters:
# ## K
# ### same as initialization
# ## nIters
# ### same as initialization
# ## seed
# ### same as initialization

# # Metadata:
# ## K range check
# ## list length check
# ## ind
# ### user, single
# ### user, double
# ## K
# ### user, single
# ### user, double

# # Clear:
# ##
