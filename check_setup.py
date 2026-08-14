import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv("C:\EDA LAB\datasets\Diode_IV_Temperature.csv")

fig,ax=plt.subplots(1,figsize=(3,3),dpi=350)
ax.plot(df["V(0)"],df["I(mA)"],color="r",label = "T = 0C",linewidth=1)
ax.plot(df["V(25)"],df["I(25)"],color="b",label = "T = 25C",linewidth=1)
ax.plot(df["V(50)"],df["I(50)"],color="y",label = "T = 50C",linewidth=1)
ax.plot(df["V(75)"],df["I(75)"],color="g",label = "T = 75C",linewidth=1)
ax.grid(True,linestyle="--")
ax.set_xlabel("Voltage(V)")
ax.set_ylabel("current(mA)")
ax.set_title("I - V Graph at diff Temp")
ax.legend(loc="upper left")

plt.show()