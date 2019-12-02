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

#CAN I FORMAT WITH ,000,000,0000 AND KEEP IT NUMERIC?
#df["airbnb_potential_revenue"] = df["airbnb_potential_revenue"].map('{:,.2f}'.format)
#df["proposed_dwelling_units"] = df["proposed_dwelling_units"].map('{:,.2f}'.format)
print(df)

df.plot(kind='bar',grid=False,subplots=True,sharex=True)
plt.show()
plt.savefig("C:/Users/erikh/Desktop/Pratt/Programming/finalproject/chart.png")