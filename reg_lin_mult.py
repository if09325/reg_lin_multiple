# -*- coding: utf-8 -*-

import pandas as pd 
import matplotlib.pyplot as plt 
from statsmodels.regression.linear_model import OLS as ols

#loading data 
df = pd.read_csv("ds.csv")

#creation des Xs, Y 
Y_profit = df["Profit"] 

X_indepent_var = df[["R&D Spend", "Administration", "Marketing Spend"]]
#X_indepent_var = df[["R&D Spend", "Marketing Spend"]]
#X_indepent_var = df[["R&D Spend", "Administration"]]

ax = plt.axes(projection='3d')

ax.set_xlabel("R&D Spend")
ax.set_ylabel("Marketing Spend")
ax.set_zlabel("Profit ")
z_points = df["R&D Spend"]
x_points = df["Administration"]
y_points = df["Profit"]
ax.scatter3D(x_points, y_points, z_points, c=z_points);

plt.show()

res = ols(Y_profit,X_indepent_var).fit()

print(res.summary())
