import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as seabornInstance
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

def readCSV():
    dataSet = pd.read_csv("MultivariateInput.csv")
    return dataSet

def main():
    dataSet = readCSV()

    print(dataSet.describe())

    X = dataSet[['year', 'month', 'day', 'hour', 'minute','Celsius', 'precipIntensity', 'precipProbability', 'apparentTemperature', 'dewPoint', 'humidity', 'pressure', 'windSpeed', 'windGust', 'windBearing', 'cloudCover', 'uvIndex', 'visibility', 'ozone', 'PAH-24']].values
    y = dataSet['PAH'].values

    selFeat = ['year', 'month', 'day', 'hour', 'minute','Celsius', 'precipIntensity', 'precipProbability', 'apparentTemperature', 'dewPoint', 'humidity', 'pressure', 'windSpeed', 'windGust', 'windBearing', 'cloudCover', 'uvIndex', 'visibility', 'ozone', 'PAH-24']

    # plt.figure(figsize=(15, 10))
    # plt.tight_layout()
    # seabornInstance.distplot(dataSet['PAH'])
    #plt.show()

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    regressorpoly3 = make_pipeline(PolynomialFeatures(3), Ridge())
    regressorpoly3.fit(X_train, y_train)

    #coefficient values for each feature in attributes
    #coeff_df = pd.DataFrame({'Coeff':regressorpoly2.coef_, "feature":selFeat})
    #print(coeff_df)

    y_pred = regressorpoly3.predict(X_test)

    df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
    df1 = df.head(25)
    print(df1)

    df1.plot(kind='bar', figsize=(10, 8))
    plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
    plt.show()

    print('Confidence: ', regressorpoly3.score(X_test, y_test))
    print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
    print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
    print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

if __name__ == "__main__":
    main()