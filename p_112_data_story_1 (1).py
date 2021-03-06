# -*- coding: utf-8 -*-
"""P-112 Data Story - 1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E1adPHv-Nyk6lvS-lLxAg3QJzfC-j-hY
"""

import csv
import plotly.express as px
import pandas as pd
import statistics
import plotly.graph_objects as go
import numpy as np

df = pd.read_csv("data.csv")
print(df)

fig = px.scatter(df, y= "quant_saved", color = "female")
fig.show()

with open("data.csv", newline = "") as f:
   reader = csv.reader(f)
   savings_data = list(reader)

savings_data.pop(0)
print(savings_data)

# find the total number of males and females
total_entries = len(savings_data)
females = 0

for i in savings_data:
   if int(i[1]) == 1:
      females += 1


fig = go.Figure(go.Bar(x = ["Females", "Males"], y = [females, total_entries - females]))
fig.show()

females = []
males = []

for i in savings_data: 
   if int(i[1]) == 1:
      females.append(float(i[0]))
   else:
      males.append(float(i[0]))

print(f"Mean of the total females- {statistics.mean(females)}")
print(f"Mode of the total females- {statistics.mode(females)}")
print(f"Median of the total females- {statistics.median(females)}")
print()
print(f"Mean of the total males- {statistics.mean(males)}")
print(f"Mode of the total males- {statistics.mode(males)}")
print(f"Median of the total males- {statistics.median(males)}")

print(f"Standard deviation of the entire data- {statistics.stdev(all_savings)}")
print(f"Standard deviation for females- {statistics.stdev(females)}")
print(f"Standard deviation for males- {statistics.stdev(males)}")

gender = []
savings = []
for i in savings_data:
   if float(i[1]) != 0:
      gender.append(float(i[1]))
      savings.append(float(i[0]))

correlation_for_data = np.corrcoef(gender, savings)

print(f"Correlation between the person's gender and savings{correlation_for_data[1,0]}")