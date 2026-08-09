import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv("C:\EDA LAB\datasets\MOSFET_ID_VDS.csv")

fig,ax=plt.subplots(1,figsize=(3,3),dpi=300)
ax.plot(df["V_DS (2V)"],df["I_D (2mA)"],color="r",label = "V_GS = 2V",linewidth=1)
ax.plot(df["V_DS (3V)"],df["I_D (3mA)"],color="b",label = "V_GS = 3V",linewidth=1)
ax.plot(df["V_DS (4V)"],df["I_D (4mA)"],color="y",label = "V_GS = 4V",linewidth=1)
ax.plot(df["V_DS (5V)"],df["I_D (5mA)"],color="g",label = "V_GS = 5V",linewidth=1)
ax.set_xlabel("V_DS(V)")
ax.set_ylabel("I_D(mA)")
ax.set_title("I_D vs V_DS")
ax.legend(loc="upper left")

plt.show()
