import sys
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
print("Python :", sys.version.split()[0])
print("numpy :", np. version )


# a one-line smoke test of the plotting back-end
plt.plot([0, 3, 2, 5], [0, 9, 4, 25], marker="s",color="r")
plt.title("Diagram")
plt.xlabel("x numbers"); plt.ylabel("x^^2 squared")
plt.grid(True)
plt.show()