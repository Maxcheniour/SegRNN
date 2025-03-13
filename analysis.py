import pandas as pd

# Charger ton fichier d'origine
df = pd.read_csv('dataset/weather.csv')

# Suppression de la colonne 'time'
df = df.drop(columns=['time'])

# Vérification du format de la date (optionnel, pour être sûr)
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d %H:%M:%S')

# Réordonner les colonnes si nécessaire (ex: mettre 'date' en première colonne)
cols = list(df.columns)
cols.insert(0, cols.pop(cols.index('date')))  # Met 'date' en premier
df = df[cols]

# Sauvegarder le nouveau CSV corrigé
df.to_csv('fichier_corrige.csv', index=False)
