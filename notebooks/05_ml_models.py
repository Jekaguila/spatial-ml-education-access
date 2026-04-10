# Modelos Predictivos.

#Preparación
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.ensemble import RandomForestRegressor

#Entrenamiento 
X = df[["nearest_school_km", "school_density", "pobreza", "ruralidad"]]
y = df["accessibility_index"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestRegressor(n_estimators=300)
model.fit(X_train, y_train)

#Evaluación
preds = model.predict(X_test)
rmse = mean_squared_error(y_test, preds, squared=False)
mae = mean_absolute_error(y_test, preds)
rmse, mae

#Importancia de variables
importances = pd.Series(model.feature_importances_, index=X.columns)
importances.plot(kind="bar")
