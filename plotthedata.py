import pandas as pd
import plotly_express as px
df = pd.read_csv("line_chart.csv")
fig = px.line(df, x = "Year", y = "Per capita income", color = "Country", title = 'Per capita income')
fig.show()