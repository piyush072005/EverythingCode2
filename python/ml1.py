import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 1. Generate synthetic data
# Create a simple linear relationship with some noise
X = np.random.rand(100, 1) * 10  # 100 data points, 1 feature
y = 2 * X + 1 + np.random.randn(100, 1) * 2  # y = 2x + 1 + noise

# 2. Split data into training and testing sets
# 80% for training, 20% for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Train a Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# 4. Make predictions on the test data
y_pred = model.predict(X_test)

# 5. Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")
print(f"Model coefficients: {model.coef_[0][0]:.2f}")
print(f"Model intercept: {model.intercept_[0]:.2f}")