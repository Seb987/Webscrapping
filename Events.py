import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np

st.set_page_config(page_title="Choix d'évènements")

df_concert=pd.read_csv('events/concert.csv')
df_festival=pd.read_csv('events/festival.csv')
df_spectacle=pd.read_csv('events/spectacle-et-comedie-musicale.csv')
df_humour=pd.read_csv('events/humour-et-one-wo-man-show.csv')
df_sport=pd.read_csv('events/sport.csv')
df_parc=pd.read_csv('events/parc.csv')
df_expo=pd.read_csv('events/exposition-et-musee.csv')
df_theatre=pd.read_csv('events/theatre.csv')
df_cirque=pd.read_csv('events/cirque.csv')
df_salon=pd.read_csv('events/salon.csv')
df_danse=pd.read_csv('events/danse.csv')
df_classique=pd.read_csv('events/classique-et-opera.csv')
df_loisir=pd.read_csv('events/loisirs-et-tourisme.csv')
df_soiree=pd.read_csv('events/soiree.csv')

#Le fichier selected.csv permet de stocker temporairement
df_selected = pd.read_csv('selected.csv')

#Fonction qui permet de récupérer le fichier csv correspondant à la catégorie sélectionnée
def DataFrame_Events(selected):
    if selected == 'Concert':
        df=df_concert
    if selected == 'Festival':
        df=df_festival
    if selected == 'Spectacle et comédie musicale':
        df=df_spectacle
    if selected == 'Humour et One man show':
        df=df_humour
    if selected == 'Sport':
        df=df_sport
    if selected == 'Parc':
        df=df_parc
    if selected == 'Exposition et musée':
        df=df_expo
    if selected == 'Théâtre':
        df=df_theatre
    if selected == 'Cirque':
        df=df_cirque
    if selected == 'Salon':
        df=df_salon
    if selected == 'Danse':
        df=df_danse
    if selected == 'Classique et opéra':
        df=df_classique
    if selected == 'Loisirs et tourisme':
        df=df_loisir
    if selected == 'Soirée':
        df=df_soiree
    return df
    
st.title("Catégories")

selected = option_menu(None, 
    ["Concert", "Festival", "Spectacle et comédie musicale", 'Humour et One man show','Sport','Parc','Exposition et musée','Théâtre','Cirque','Salon', 'Danse', 'Classique et opéra', 'Loisirs et tourisme', 'Soirée'], 
    menu_icon="cast", orientation="horizontal",
    styles={
        "nav-link": { "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "green"},
    })

df=DataFrame_Events(selected)

if(selected == 'Soirée'):
    len_events=4
else: 
    len_events=30
#Nous avons décidé de n'afficher que les 30 premiers évènements, sauf pour les soirées où il n'y en a uniquement 4
for i in range(len_events):
    with st.container():
        image_column, text_column, btn_column =st.columns((4,10,3.5))
        with image_column:
            #Affichage de l'image  
            st.image(df['Image'][i],width=140)
        with text_column:
            #Affichage des informations concernant l'évènement
            st.write(df['Date'][i])
            st.write(df['Lieu'][i]+" - "+df['Ville'][i])
            st.write(df['Type'][i])
            st.write(str(df['Prix'][i]) + " €")
            st.write( df['Artiste'][i])
        with btn_column:
            #Ajout d'un bouton pour ajouter l'évènement dans le fichier selected.csv
            btn=st.button("Ajouter",key=i)
            if btn:
                st.success("Évenèment ajouté")
                df_selected.append(df.iloc[i]).to_csv('selected.csv',index=False)
        st.write("----------------------------------------------------------------------")