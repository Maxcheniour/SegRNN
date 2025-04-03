import pandas as pd

# === Charger le fichier ===
df = pd.read_csv("newdata/weather_enriched.csv")
df['date'] = pd.to_datetime(df['date'])

# === Créer une colonne "jour" (sans l'heure) ===
df['date_only'] = df['date'].dt.date

# === Calculer le total de précipitations par jour ===
daily_tp = df.groupby('date_only')['tp'].sum().reset_index()
daily_tp.rename(columns={'tp': 'tp_daily_total'}, inplace=True)

# === Fusionner avec le dataframe original ===
df = df.merge(daily_tp, on='date_only', how='left')

# === Supprimer la colonne intermédiaire si tu veux pas la garder ===
df.drop(columns=['date_only'], inplace=True)
df.drop(columns=['tp_6h'], inplace=True)

# === Sauvegarde ===
df.to_csv("newdata/weather0.csv", index=False)
print("✅ Fichier enrichi avec précipitations journalières : weather0.csv")
