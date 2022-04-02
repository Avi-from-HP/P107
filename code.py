import pandas as pd
import csv
import plotly.express as px
df = pd.read_csv('C:/Users/avigh/Desktop/ /Python codes/Projects/data-analysis-through-visualisation-master/data-analysis-through-visualisation-master/data.csv')
mean = df.groupby(["student_id", "level"], as_index=False)["attempt"].mean()
fig = px.scatter(mean, x="student_id", y="level", size="attempt", color="attempt")
fig.show()
