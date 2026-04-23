import pandas as pd

def load_and_preprocess(path):
    df = pd.read_csv(path)

    # Convert categorical → numeric
    df = pd.get_dummies(df, columns=["Product", "Region"], drop_first=True)

    X = df.drop(["Sales", "OrderID"], axis=1)
    y = df["Sales"]

    return X, y