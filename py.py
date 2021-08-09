import  csv
import plotly.express as px
import pandas as pd
import numpy as np

def plotfigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df, x = "Temperature", y = "Ice-cream Sales")
        fig.show()

def getdatasource(data_path):
    Ice_cream_Sales = []
    Cold_drink_sales = []
    with open(data_path) as csv_file:
        for row in csv_reader:
           Ice_cream_Sales.append(float(row["Temperature"]))
           Cold_drink_sales.append(float(row["Ice-cream Sales"]))
    return{"x": Ice_cream_Sales, "y": Cold_drink_sales}
def finedcognition(dataSource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])