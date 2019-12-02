import matplotlib.pyplot as plt
import pandas as pd

const1 = pd.read_csv("C:/Users/erikh/Desktop/Pratt/Programming/finalproject/const1.csv")

for col in const1:
    print(col)

#total revenue per borough
potential_revenue_borough = const1.groupby("borough")["airbnb_potential_revenue"].sum()
dwelling_units_borough = const1.groupby("borough")["proposed_dwelling_units"].sum()

df1 = pd.DataFrame(potential_revenue_borough)
df2 = pd.DataFrame(dwelling_units_borough)
df = pd.concat([df1, df2], axis=1, sort=True)
print(df)

df.plot(kind='bar',grid=False,subplots=True,sharex=True,figsize=(6, 6))
plt.tight_layout()
plt.show()
#plt.savefig("chart.png")