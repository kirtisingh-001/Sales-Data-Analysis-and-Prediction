import pandas as pd
import matplotlib.pyplot as plt
import os

# Load data
df = pd.read_csv("../sales_data.csv")

# Create graph (FIXED LINE)
df.groupby("Region")["Sales"].sum().plot(kind="bar")

plt.title("Sales by Region")

# Create folder if not exists
os.makedirs("../outputs/plots", exist_ok=True)

# Save graph
plt.savefig("../outputs/plots/sales_by_region.png")

# Show graph
plt.show()