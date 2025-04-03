import netCDF4 as nc
import pandas as pd

# Ouvrir le fichier .nc
nc_file = 'newdata/accum.nc'  # remplace par le vrai nom du fichier
dataset = nc.Dataset(nc_file)

# Afficher les dimensions (utile pour debug)
print("Dimensions :", dataset.dimensions.keys())
print("Variables disponibles :", dataset.variables.keys())

# Extraire les variables
valid_time = dataset.variables['valid_time'][:]     # Le temps
latitudes = dataset.variables['latitude'][:]        # Latitudes
longitudes = dataset.variables['longitude'][:]      # Longitudes
valeurs = dataset.variables['tp'][:]                # Valeur principale (précipitation ?)

# Stocker les données dans un tableau
data = []

for t_index, t in enumerate(valid_time):
    for lat_index, lat in enumerate(latitudes):
        for lon_index, lon in enumerate(longitudes):
            try:
                val = valeurs[t_index, lat_index, lon_index]
            except IndexError:
                # Dans certains cas, la structure peut être [time, lat, lon] ou [time, ensemble, lat, lon]
                val = None
            data.append([t, lat, lon, val])

# Créer un DataFrame et sauvegarder
df = pd.DataFrame(data, columns=['valid_time', 'latitude', 'longitude', 'tp'])
df.to_csv('newdata/output_accum.csv', index=False)
print("✅ Conversion terminée → output.csv")
