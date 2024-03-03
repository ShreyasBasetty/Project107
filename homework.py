import pandas as pd
import csv
import plotly.graph_objects as go

student_df = pd.read_csv("Average Distance of Sports.csv")

print(student_df.groupby("level") ["attempt"].mean())

fig = go.Figure(go.Bar(
    x=student_df.groupby("level") ["attempt"].mean(),
    y=['Level 1', 'Level 2', 'Level 3', 'Level 4'],
    orientation='h'))
fig.show()      