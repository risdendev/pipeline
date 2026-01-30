from sklearn.linear_model import LinearRegression
def test_linear_model_determiniistic():
    model = LinearRegression()
    X = [[1], [2], [3]]
    y = [2, 4, 6]
    model.fit(X, y)

    assert round(model.coef_[0], 2) == 2.0