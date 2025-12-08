import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("./sales_data.csv")

# sb.histplot(df["Price (INR)"])
# sb.boxplot(x=df["Price (INR)"])
sb.countplot(x=df["Price (INR)"])

plt.show()
