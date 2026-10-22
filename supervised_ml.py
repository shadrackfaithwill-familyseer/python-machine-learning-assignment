from sklearn.linear_model import LinearRegression
x = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
y = [30, 40, 45, 55, 65, 70, 80, 85, 90, 95]
model = LinearRegression()
model.fit(x, y)
hours = float(input("Enter hours studied: "))
prediction = model.predict([[hours]])
print(f"predicted exam score: {prediction[0]:.2f}")