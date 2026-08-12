import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv("C:\EDA LAB\datasets\MOSFET_ID_VGS.csv")
fig,ax=plt.subplots(1,2,figsize=(3,3),dpi=300)
ax[0].plot(df["V_GS (0.1V)"],df["I_D (0.1V)"],color="r",label = "V_DS = 0.1V",linewidth=1)
ax[0].plot(df["V_GS (1V)"],df["I_D (1V)"],color="b",label = "V_DS = 1V",linewidth=1)
ax[0].plot(df["V_GS (3V)"],df["I_D (3V)"],color="y",label = "V_DS = 3V",linewidth=1)
ax[0].plot(df["V_GS (5V)"],df["I_D (5V)"],color="g",label = "V_DS = 5V",linewidth=1)
ax[0].set_xlabel("V_GS(V)")
ax[0].set_ylabel("I_D(mA)")
ax[0].set_title("I_D vs V_GS")
ax[0].legend(loc="upper left")
plt.show()