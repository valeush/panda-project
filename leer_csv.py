import pandas as pd

# Asegurate de que el nombre del archivo sea correcto
df = pd.read_csv("global_street_food.csv")

#print(df.head())  # Muestra las primeras 5 filas del CSV
print(df["Country"].value_counts())
