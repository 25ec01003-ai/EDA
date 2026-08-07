import sys
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
print("Python :", sys.version.split()[0])
print("numpy :", np. version )


# a one-line smoke test of the plotting back-end
plt.plot([0, 1, 2, 5], [0, 3, 4, 15], marker="s",color="r")
plt.title("diagram")
plt.xlabel("x"); plt.ylabel("x squared")
plt.grid(True)
plt.show()