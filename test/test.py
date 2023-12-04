import pandas as pd
import numpy
import matplotlib

# Charger un fichier Excel (XLS ou XLSX)
df_excel = pd.read_excel('titanic.xls')  # ou pd.read_excel('votre_fichier.xlsx')

# Afficher les premières lignes du DataFrame
print(df_excel.head())