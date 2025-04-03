import netCDF4 as nc
import pandas as pd

# Ouvrir le fichier .nc
nc_file = 'newdata/instant.nc'  # remplace par le vrai nom du fichier
dataset = nc.Dataset(nc_file)

# Afficher les dimensions et les variables
print("Dimensions :", dataset.dimensions.keys())
print("Variables disponibles :", dataset.variables.keys())

# Extraire les coordonnées
valid_time = dataset.variables['valid_time'][:]     # Temps (en timestamps ou autre format)
latitudes = dataset.variables['latitude'][:]
longitudes = dataset.variables['longitude'][:]

# Extraire les variables météo (attention à la forme exacte de chaque variable)
u10 = dataset.variables['u10'][:]
v10 = dataset.variables['v10'][:]
t2m = dataset.variables['t2m'][:]
msl = dataset.variables['msl'][:]
z = dataset.variables['z'][:]

# Préparation des données
data = []

# Supposons la forme (time, lat, lon)
for t_index, t in enumerate(valid_time):
    for lat_index, lat in enumerate(latitudes):
        for lon_index, lon in enumerate(longitudes):
            try:
                row = [
                    t,
                    lat,
                    lon,
                    u10[t_index, lat_index, lon_index],
                    v10[t_index, lat_index, lon_index],
                    t2m[t_index, lat_index, lon_index],
                    msl[t_index, lat_index, lon_index],
                    z[t_index, lat_index, lon_index],
                ]
            except IndexError:
                row = [t, lat, lon, None, None, None, None, None]
            data.append(row)

# Création du DataFrame
columns = ['valid_time', 'latitude', 'longitude', 'u10', 'v10', 't2m', 'msl', 'z']
df = pd.DataFrame(data, columns=columns)

# Optionnel : convertir les timestamps si besoin
# from datetime import datetime, timedelta
# df["datetime"] = [datetime(1900, 1, 1) + timedelta(hours=int(h)) for h in df["valid_time"]]

# Sauvegarde
df.to_csv('newdata/output_instant.csv', index=False)
print("✅ Données extraites et enregistrées dans output_instant.csv")
