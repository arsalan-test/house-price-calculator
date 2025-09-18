import pandas as pd
from sklearn.linear_model import LinearRegression
import sys

# Load sample data
data = pd.read_csv('sample_data.csv')
X = data[['area', 'bedrooms', 'age']]
y = data['price']

# Train model
model = LinearRegression()
model.fit(X, y)

def predict_price(area, bedrooms, age):
    features = [[area, bedrooms, age]]
    return model.predict(features)[0]

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python house_price_calculator.py <area> <bedrooms> <age>")
        sys.exit(1)
    area = float(sys.argv[1])
    bedrooms = int(sys.argv[2])
    age = int(sys.argv[3])
    price = predict_price(area, bedrooms, age)
    print(f"Predicted house price: ${price:,.2f}")
