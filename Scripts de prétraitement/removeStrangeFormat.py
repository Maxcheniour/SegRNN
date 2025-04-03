import pandas as pd

# Fichiers
input_file = "newdata/output_filtered.csv"
output_file = "newdata/weather1.csv"

# Lire le CSV normalement
df = pd.read_csv(input_file)


#Renommer datetime en date
df = df.rename(columns={'datetime': 'date'})

# Convertir la colonne 'date' en datetime avec fuseau horaire géré
df['date'] = pd.to_datetime(df['date'], errors='coerce', utc=True)

# Enlever le fuseau horaire → devient naive (sans timezone)
df['date'] = df['date'].dt.tz_convert(None)

# Sauvegarder le fichier nettoyé
df.to_csv(output_file, index=False)

print("✅ Fichier nettoyé sauvegardé :", output_file)
