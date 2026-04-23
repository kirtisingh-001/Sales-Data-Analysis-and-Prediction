import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/sales_data.csv")

# Create graph
df.groupby("Region")["Sales"].sum().plot(kind="bar")

plt.title("Sales by Region")

# SAVE GRAPH (IMPORTANT LINE)
plt.savefig("outputs/plots/sales_by_region.png")

# Show graph
plt.show()