# -*- coding: utf-8 -*-

import pandas as pd 
#pour le graph
import matplotlib.pyplot as plt 
#pour le résultat détaillé sur les différentes valeur R² - P-Value ...etc
from statsmodels.regression.linear_model import OLS as ols

#chargement des données 
df = pd.read_csv("ds.csv")

#creation des variables (dép | indép)
Y_profit = df["Profit"] 
X_indepent_var = df[["R&D Spend", "Administration", "Marketing Spend"]]
#X_indepent_var = df[["R&D Spend", "Marketing Spend"]]
#X_indepent_var = df[["R&D Spend", "Administration"]]

#Dessiner le graphe en 3D
ax = plt.axes(projection='3d')
ax.set_xlabel("R&D Spend")
ax.set_ylabel("Marketing Spend")
ax.set_zlabel("Profit ")
z_points = df["R&D Spend"]
x_points = df["Administration"]
y_points = df["Profit"]
ax.scatter3D(x_points, y_points, z_points, c=z_points);
plt.show()

#Détailler les résultats statistiques 
res = ols(Y_profit,X_indepent_var).fit()
print(res.summary())
