import numpy as np
from sklearn import linear_model
import sklearn.metrics as sm
from sklearn.preprocessing import  PolynomialFeatures

# Input file containing data
input_file = 'data_multivar_regr.txt'

# Load  data from file
data = np.loadtxt(input_file, delimiter=',')
X, y = data[:, :-1], data[:, -1]


# Load the data into training and testing
num_training = int(0.8 * len(X))
num_test = len(X) - num_training

# Training data
X_train, y_train = X[:num_training], y[:num_training]

# Test data
X_test, y_test = X[num_training:], y[num_training:]

# Create the linear regressor model
linear_regressor = linear_model.LinearRegression()

# Train the model using the training set
linear_regressor.fit(X_train, y_train)

# Predict the output
y_test_pred = linear_regressor.predict(X_test)

# Measure performance
print('Linear regressor performance:')
print('Mean absolute error =', round(sm.mean_absolute_error(y_test, y_test_pred), 2))
print('Mean squared error =', round(sm.mean_squared_error(y_test, y_test_pred), 2))
print('Median absollute error =', round(sm.median_absolute_error(y_test, y_test_pred), 2))
print('Explained variance score =', round(sm.explained_variance_score(y_test, y_test_pred), 2))

# Polynomial regression
polynomial = PolynomialFeatures(degree=10)
X_train_transformed = polynomial.fit_transform(X_train)
datapoint = [[7.75,6.35,5.56]]
poly_datapoint = polynomial.fit_transform(datapoint)
print(X_train_transformed.shape, poly_datapoint.shape)

poly_linear_model = linear_model.LinearRegression()
poly_linear_model.fit(X_train_transformed, y_train)
print("\nLinear regression:\n", linear_regressor.predict(datapoint))
print("\nPolynomial regression:\n", poly_linear_model.predict(poly_datapoint))
