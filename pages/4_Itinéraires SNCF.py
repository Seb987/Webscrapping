import streamlit as st
from streamlit_folium import st_folium
import folium
import geopandas as gpd
import pandas as pd
from datetime import datetime
from datetime import timedelta

if 'button' not in st.session_state:
    st.session_state['button'] = False

villes = [
    "Paris",
    "Marseille",
    "Lyon",
    "Toulouse",
    "Nice",
    "Nantes",
    "Strasbourg",
    "Montpellier",
    "Bordeaux",
    "Lille",
    "Rennes",
    "Reims",
    "Toulon",
    "Grenoble",
    "Dijon",
    "Angers"
]

def get_trajets(m,gares, ville_origine, ville_destination):
    gare_origine=gares.loc[gares['commune_libellemin'].str.contains(ville_origine, na=False)]
    gare_destination=gares.loc[gares['commune_libellemin'].str.contains(ville_destination, na=False)]

    coord_origine = [gare_origine.iloc[0]['geometry'].y,gare_origine.iloc[0]['geometry'].x]
    coord_destination = [gare_destination.iloc[0]['geometry'].y,gare_destination.iloc[0]['geometry'].x]

    #On marque sur la carte la gare d'origine et de destination
    folium.Marker(
    coord_origine, popup=gare_origine['alias_libelle_noncontraint'].values[0], tooltip=gare_origine['alias_libelle_noncontraint'].values[0]
    ).add_to(m)
    folium.Marker(
    coord_destination, popup=gare_destination['alias_libelle_noncontraint'].values[0], tooltip=gare_destination['alias_libelle_noncontraint'].values[0]
    ).add_to(m)

    #Crée une ligne qui relie les 2 gares
    folium.PolyLine([coord_origine, coord_destination], color="red", weight=2.5, opacity=0.5,arrow_style='->',arrow_color='blue',arrow_size=10
    ).add_to(m)

    return

st.title("Itinéraires SNCF")

#Dataframe des évènements que l'utilisateur a choisi
df_selected = pd.read_csv('selected.csv')

#Liste des gares 
gares = gpd.read_file("sncf/gares.geojson")

#Liste des trajets
itineraires= pd.read_csv("sncf/tarifs.csv",sep=';')

gares['uic_code'] = gares['uic_code'].astype('str')
itineraires['Gare origine - code UIC']=itineraires['Gare origine - code UIC'].astype('str')
itineraires['Gare destination - code UIC']=itineraires['Gare destination - code UIC'].astype('str')
gares.dropna(how='all',inplace=True,subset=['commune_libellemin','geometry'])
gares['commune_libellemin']=gares['commune_libellemin'].str.upper()


#On vérifie que l'utilisateur a bien choisi des dates pour chaque évènement
if 'Date_Choix' not in df_selected.columns or df_selected['Date_Choix'].isnull().values.any():
    st.header("Vous n'avez pas choisi de date pour tous les évènements, veuillez vous rendre à la page Airbnb")
else:
    df_selected.sort_values(by='Date_Choix',inplace=True)
    st.dataframe(df_selected)

    ville=st.selectbox("Ville de départ (Vous pouvez l'écrire au clavier ou choisir parmi les choix)", villes)

    if (st.session_state['button']==False):
        btn=st.button("Afficher l'itinéraire")
    else:
        btn=True
    if (btn):
        st.session_state['button'] = True
        gare=gares.loc[gares['commune_libellemin'].str.contains(ville.upper(), na=False)]
        
        m = folium.Map(location=[gare.iloc[0]['geometry'].y,gare.iloc[0]['geometry'].x], zoom_start=7)
        get_trajets(m,gares,ville.upper(),df_selected.iloc[0]['Ville'])
        for i in range(len(df_selected)-1):
            if df_selected.iloc[i]['Ville'] == df_selected.iloc[i+1]['Ville']:
                continue
            get_trajets(m,gares,df_selected.iloc[i]['Ville'],df_selected.iloc[i+1]['Ville'])
        get_trajets(m,gares,df_selected.iloc[-1]['Ville'],ville.upper())
        st_data=st_folium(m, width=725)
    
    
