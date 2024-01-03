import requests
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# API endpoint and parameters
url = 'https://samples.openweathermap.org/data/2.5/forecast?id=524901&appid=b1b15e88fa797225412429c1c50c122a1'

# Make API request
response = requests.get(url)

# Extract relevant weather data from response
weather_data = response.json()
print(weather_data)
temperature = weather_data['main']['temperature']
humidity = weather_data['main']['humidity']
wind_speed = weather_data['main']['pressure']

# Create pandas DataFrame with weather data
df = pd.DataFrame({'Temperature': [temperature], 'Humidity': [humidity], 'Wind Speed': [wind_speed]})

# Preprocess the data
df.fillna(df.mean(), inplace=True)
if len(df)<2:
    raise ValueError("iinsufficient")

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df.drop('Temperature', axis=1), df['Temperature'], test_size=0.2, random_state=42)

# Train a linear regression model
lr = LinearRegression()
lr.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = lr.predict(X_test)

# Evaluate the accuracy of the model using mean squared error
mse = mean_squared_error(y_test, y_pred)
print('Mean Squared Error:', mse)

# Use the model to make predictions for future weather conditions
future_weather = pd.DataFrame({'Humidity': [50], 'Wind Speed': [10]})
future_temperature = lr.predict(future_weather)
print('Predicted Temperature:', future_temperature[0])

# Visualize the data and predictions
plt.scatter(X_test['Humidity'], y_test, color='blue')
plt.plot(X_test['Humidity'], y_pred, color='red')
plt.xlabel('Humidity')
plt.ylabel('Temperature')
plt.title('Linear Regression Model for Weather Data')
plt.show()
