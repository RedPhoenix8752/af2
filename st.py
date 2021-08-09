import csv
import pandas as pd
import plotly.graph_objects as po
df = pd.read_csv("st.csv")
print(df.groupby("numofdayscleaned")["garbagesize"].mean())
fig = po.Figure(po.Bar(x = df.groupby("numofdayscleaned")["garbagesize"].mean(), y = ['day 1', 'day 2', 'day 3', 'day 4', 'day 5', 'day 6', 'day 7', 'day 8', 'day 9', 'day 10'], orientation = 'h'))
fig.show()