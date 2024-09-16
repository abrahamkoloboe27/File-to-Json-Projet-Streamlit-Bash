import streamlit as st
import pandas as pd

st.set_page_config(page_title="Uploader et transformer des fichiers CSV/Excel en JSON", 
                   #sidebar=True,
                   layout="wide",
                   page_icon=":open_file_folder:")

# Fonction pour lire les fichiers CSV ou Excel
def load_file(uploaded_file):
    if uploaded_file is not None:
        # Si le fichier est un Excel
        if uploaded_file.name.endswith('.xls') or uploaded_file.name.endswith('.xlsx'):
            # Charger le fichier Excel
            excel_file = pd.ExcelFile(uploaded_file)
            # Si le fichier Excel contient plusieurs feuilles
            if len(excel_file.sheet_names) > 1:
                sheet = st.selectbox("Sélectionnez une feuille", excel_file.sheet_names)
                df = pd.read_excel(uploaded_file, sheet_name=sheet)
            else:
                df = pd.read_excel(uploaded_file)
        # Si c'est un fichier CSV
        elif uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            st.error("Format de fichier non supporté")
            return None
        return df
    return None

# Interface principale
st.title("Uploader et transformer des fichiers CSV/Excel en JSON")

# Charger le fichier
uploaded_file = st.file_uploader("Uploader un fichier CSV ou Excel", type=['csv', 'xls', 'xlsx'])

# Charger le fichier dans un dataframe Pandas
df = load_file(uploaded_file)

# Si un fichier a été chargé avec succès
if df is not None:
    st.write("Aperçu des données :")
    with st.expander("Afficher les données", False):
        st.dataframe(df.head(), use_container_width=True) 

    # Sélectionner les colonnes à extraire (au moins une colonne doit être sélectionnée)
    columns_to_select = st.multiselect("Sélectionnez les colonnes", df.columns)
    
    # Ajouter un bouton pour valider la sélection
    if st.button("Valider la sélection des colonnes"):
        if len(columns_to_select) >= 1:
            # Créer un DataFrame avec les colonnes sélectionnées
            df_selected = df[columns_to_select]
            st.write("Colonnes sélectionnées :")
            with st.expander("Afficher les données sélectionnées", False):
                st.dataframe(df_selected, use_container_width=True)

            # Convertir les données en JSON
            data_json = df_selected.to_json(orient='records')
            
            # Afficher le JSON
            st.write("Données en JSON :")
            with st.expander("Afficher les données JSON", False):
                st.json(data_json)

            # Permettre de télécharger le JSON
            st.download_button(label="Télécharger JSON", data=data_json, file_name='data.json', mime='application/json')
        else:
            st.warning("Veuillez sélectionner au moins une colonne.")
else:   
    # Ecrire un Readme pour expliquer comment utiliser l'application
    st.markdown("""
    ### Comment utiliser l'application ?
    1. Uploader un fichier CSV ou Excel
    2. Sélectionner les colonnes à extraire
    3. Valider la sélection
    4. Télécharger le fichier JSON
    """)
    