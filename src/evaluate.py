import joblib
from sklearn.metrics import mean_absolute_error, r2_score
from data_preprocessing import load_and_preprocess

# Load data
X, y = load_and_preprocess("data/sales_data.csv")

# Load model
model = joblib.load("outputs/model.pkl")

# Predict
y_pred = model.predict(X)

print("MAE:", mean_absolute_error(y, y_pred))
print("R2 Score:", r2_score(y, y_pred))