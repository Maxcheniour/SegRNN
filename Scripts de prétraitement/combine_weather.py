import pandas as pd
import os

# Chemin du dossier contenant les fichiers CSV
folder_path = 'newdata'

# Liste des fichiers à combiner dans l'ordre
files = [f'weather{i}.csv' for i in range(1, 9)]

# Créer une liste vide pour stocker les DataFrames
dfs = []

# Lire chaque fichier CSV et l'ajouter à la liste
for file in files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_csv(file_path)
    dfs.append(df)

# Combiner tous les DataFrames
combined_df = pd.concat(dfs, ignore_index=True)

# Sauvegarder le DataFrame combiné dans un nouveau fichier CSV
output_path = os.path.join(folder_path, 'weather.csv')
combined_df.to_csv(output_path, index=False)

print(f"Les fichiers ont été combinés avec succès dans {output_path}")
print(f"Nombre total de lignes dans le fichier combiné : {len(combined_df)}") 