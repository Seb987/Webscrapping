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

#Récupère les coordonnées de la gare de départ et d'arrivée, puis les affiche sur la carte avec une ligne entre les deux
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
#Affiche le chemin à effectuer à partir de la ville où habite l'utilisateur et des villes des évènements qu'il a choisi dans l'ordre des dates
def afficher_chemin():
    chemin = []
    chemin.append(ville)
    chemin.append("  ----->  ") 
    for i in range(len(df_selected)):
        chemin.append(df_selected.iloc[i]['Ville'])
        chemin.append("  ----->  ") 
    chemin.append(ville)
    st.write("Itinéraire à effectuer :")
    st.write(" ".join(map(str, chemin)))
    return

st.title("Itinéraires SNCF")

#Dataframe des évènements que l'utilisateur a choisi
df_selected = pd.read_csv('selected.csv')

#Liste des gares 
gares = gpd.read_file("sncf/gares.geojson")

#Liste des trajets
itineraires= pd.read_csv("sncf/tarifs.csv",sep=';')

#On nettoie les données
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

    #Correspond à la ville où habite l'utilisateur
    ville=st.selectbox("Ville de départ (Vous pouvez l'écrire au clavier ou choisir parmi les choix)", villes)
    ville=ville.upper()

    #Si le boutton n'a pas été cliqué, on affiche le boutton
    if (st.session_state['button']==False):
        btn=st.button("Afficher l'itinéraire")
    else:
        btn=True
    if (btn):
        afficher_chemin()

        st.session_state['button'] = True
        gare=gares.loc[gares['commune_libellemin'].str.contains(ville.upper(), na=False)]
        
        #On affiche la carte centrée sur la ville de départ de l'utilisateur
        m = folium.Map(location=[gare.iloc[0]['geometry'].y,gare.iloc[0]['geometry'].x], zoom_start=7)

        #On affiche le trajet entre la ville de départ et la première ville de la liste des évènements
        get_trajets(m,gares,ville,df_selected.iloc[0]['Ville'])

        #On affiche le trajet entre chaque ville de la liste des évènements
        for i in range(len(df_selected)-1):
            if df_selected.iloc[i]['Ville'] == df_selected.iloc[i+1]['Ville']:
                continue
            get_trajets(m,gares,df_selected.iloc[i]['Ville'],df_selected.iloc[i+1]['Ville'])

        #On affiche le trajet entre la dernière ville de la liste des évènements et la ville de départ
        get_trajets(m,gares,df_selected.iloc[-1]['Ville'],ville)
        st_data=st_folium(m, width=725)
    
