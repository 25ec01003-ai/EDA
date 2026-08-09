import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
df=pd.read_csv("C:\EDA LAB\datasets\MOSFET_ID_VDS.csv")

g_2d = np.gradient(df["I_D (2mA)"],df["V_DS (2V)"])
g_3d = np.gradient(df["I_D (3mA)"],df["V_DS (3V)"])
g_4d = np.gradient(df["I_D (4mA)"],df["V_DS (4V)"])
g_5d = np.gradient(df["I_D (5mA)"],df["V_DS (5V)"])
g_2d = np.nan_to_num(g_2d, nan=0)
g_3d = np.nan_to_num(g_3d, nan=0)
g_4d = np.nan_to_num(g_4d, nan=0)
g_5d = np.nan_to_num(g_5d, nan=0)
r_0 = (1/(1000*g_5d))*1000
print(r_0)
fig,ax=plt.subplots(1,figsize=(3,3),dpi=300)
ax.plot(df["V_DS (2V)"],g_2d,color="r",label = "V_GS = 2V",linewidth=1,marker="s")
ax.plot(df["V_DS (3V)"],g_3d,color="b",label = "V_GS = 3V",linewidth=1,marker="s")
ax.plot(df["V_DS (4V)"],g_4d,color="y",label = "V_GS = 4V",linewidth=1,marker="s")
ax.plot(df["V_DS (5V)"],g_5d,color="g",label = "V_GS = 5V",linewidth=1,marker="s")
ax.set_xlabel("V_DS(V)")
ax.set_ylabel("g_d(mA/V)")
ax.set_title("g_d vs V_DS")
ax.legend(loc="upper right")
plt.show()