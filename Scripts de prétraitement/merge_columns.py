import pandas as pd

def merge_columns(source_file, destination_file, output_file):
    # Lire les deux fichiers CSV
    source_df = pd.read_csv(source_file)
    dest_df = pd.read_csv(destination_file)
    
    # Vérifier si la source a au moins 4 colonnes
    if len(source_df.columns) < 4:
        print(f"Erreur : Le fichier source {source_file} n'a pas au moins 4 colonnes")
        return
    
    # Récupérer la 4ème colonne de la source
    fourth_column = source_df.iloc[:, 3]
    
    # Ajouter la colonne au fichier destination
    dest_df['tp'] = fourth_column
    
    # Sauvegarder le résultat
    dest_df.to_csv(output_file, index=False)
    print(f"La colonne a été ajoutée avec succès dans le fichier : {output_file}")

if __name__ == "__main__":
    # Ces valeurs devront être remplacées par les vrais noms de fichiers
    source_file = "newdata/output_accum_readable.csv"  # À remplacer par le nom de votre fichier source
    destination_file = "newdata/output_instant_readable.csv"  # À remplacer par le nom de votre fichier destination
    output_file = "newdata/output_readable.csv"  # Nom du fichier de sortie
    
    merge_columns(source_file, destination_file, output_file) 