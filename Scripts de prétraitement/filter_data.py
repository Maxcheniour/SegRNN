import pandas as pd

def filter_data(input_file, output_file):
    # Lire le fichier CSV
    df = pd.read_csv(input_file)
    
    # Filtrer les lignes où latitude = 49.0 et longitude = 2.5
    filtered_df = df[(df['latitude'] == 49.0) & (df['longitude'] == 2.5)]
    
    # Sauvegarder le résultat
    filtered_df.to_csv(output_file, index=False)
    print(f"Les données ont été filtrées avec succès. Résultat sauvegardé dans : {output_file}")
    print(f"Nombre de lignes conservées : {len(filtered_df)}")

if __name__ == "__main__":
    input_file = "newdata/output_readable.csv"
    output_file = "newdata/output_filtered.csv"
    
    filter_data(input_file, output_file) 