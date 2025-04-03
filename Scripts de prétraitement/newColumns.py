import pandas as pd
import numpy as np

# === Fichiers ===
input_file = "newdata/weather.csv"  # ton fichier de base
output_file = "newdata/weather_enriched.csv"

# === Lecture des données ===
df = pd.read_csv(input_file)
df['date'] = pd.to_datetime(df['date'])

# === Variables temporelles ===
df['hour'] = df['date'].dt.hour
df['dayofweek'] = df['date'].dt.dayofweek
df['month'] = df['date'].dt.month

# === Encodage cyclique temporel ===
df['hour_sin'] = np.sin(2 * np.pi * df['hour'] / 24)
df['hour_cos'] = np.cos(2 * np.pi * df['hour'] / 24)
df['dayofweek_sin'] = np.sin(2 * np.pi * df['dayofweek'] / 7)
df['dayofweek_cos'] = np.cos(2 * np.pi * df['dayofweek'] / 7)
df['month_sin'] = np.sin(2 * np.pi * df['month'] / 12)
df['month_cos'] = np.cos(2 * np.pi * df['month'] / 12)

# === Vent : magnitude et direction ===
df['wind_speed'] = np.sqrt(df['u10']**2 + df['v10']**2)
wind_dir = np.arctan2(df['v10'], df['u10'])  # en radians
df['wind_dir_sin'] = np.sin(wind_dir)
df['wind_dir_cos'] = np.cos(wind_dir)

# === Précipitations cumulées sur 6h ===
df['tp_6h'] = df['tp'].rolling(window=6).sum()

# === Nettoyage : enlever les lignes NaN créées par rolling (facultatif) ===
df = df.dropna().reset_index(drop=True)

# === Sauvegarde ===
df.to_csv(output_file, index=False)
print(f"✅ Données enrichies sauvegardées dans : {output_file}")
