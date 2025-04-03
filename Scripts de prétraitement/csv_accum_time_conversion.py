import pandas as pd
from datetime import datetime, timezone

# Charger le CSV
df = pd.read_csv('newdata/output_accum.csv')

# Convertir valid_time (UNIX timestamp) en datetime lisible
df['datetime'] = pd.to_datetime(df['valid_time'], unit='s', utc=True)
df['datetime'] = df['datetime'].dt.tz_convert('Europe/Paris')  # facultatif

# Réorganiser les colonnes
df = df[['datetime', 'latitude', 'longitude', 'tp']]

# Sauvegarder
df.to_csv('newdata/output_accum_readable.csv', index=False)
print("✅ Fichier converti avec dates lisibles → output_readable.csv")
