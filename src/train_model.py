from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from data_preprocessing import load_and_preprocess
import joblib

# Load data
X, y = load_and_preprocess("data/sales_data.csv")

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "outputs/model.pkl")

print("Model trained successfully!")