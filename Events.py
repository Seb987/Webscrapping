import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

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
df_selected = pd.read_csv('selected.csv')

st.header("Catégories")

selected = option_menu(None, 
    ["Concert", "Festival", "Spectacle et comédie musicale", 'Humour et One man show','Sport','Parc','Exposition et musée','Théâtre','Cirque','Salon', 'Danse', 'Classique et opéra', 'Loisirs et tourisme', 'Soirée'], 
    menu_icon="cast", orientation="horizontal",
    styles={
        #"container": {"padding": "0!important"},
        "nav-link": { "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "green"},
    })

#    icons=['house', 'cloud-upload', "list-task", 'gear'], 

if selected == 'Concert':
    for i in range(5):
        with st.container():
            image_column, text_column, btn_column =st.columns((4,12,3))
            with image_column:  
                st.image(df_concert['Image'][i],width=140)
            with text_column:
                st.markdown(df_concert['Date'][i])
                st.markdown(df_concert['Lieu'][i]+" - "+df_concert['Ville'][i])
                st.markdown(df_concert['Type'][i])
                st.markdown(str(df_concert['Prix'][i]) + " €")
                st.markdown( df_concert['Artiste'][i])
            with btn_column:
                btn=st.button("Ajouter",key=i)
                if btn:
                    df_selected.append(df_concert.iloc[i]).to_csv('selected.csv',index=False)
            st.write("----------------------------------------------------------------------")

if selected == 'Festival':
    for i in range(5):
        with st.container():
            image_column, text_column, btn_column =st.columns((4,12,3))            
            with image_column:  
                st.image(df_festival['Image'][i],width=140)
            with text_column:
                st.markdown(df_festival['Date'][i])
                st.markdown(df_festival['Lieu'][i]+" - "+df_festival['Ville'][i])
                st.markdown(df_festival['Type'][i])
                st.markdown(str(df_festival['Prix'][i]) + " €")
                st.markdown( df_festival['Artiste'][i])
            with btn_column:
                btn=st.button("Ajouter",key=i)
                if btn:
                    df_selected.append(df_festival.iloc[i]).to_csv('selected.csv',index=False)
            st.write("----------------------------------------------------------------------")


if selected == 'Spectacle et comédie musicale':
    for i in range(5):
        with st.container():
            image_column, text_column, btn_column =st.columns((4,12,3))            
            with image_column:  
                st.image(df_spectacle['Image'][i],width=140)
            with text_column:
                st.markdown(df_spectacle['Date'][i])
                st.markdown(df_spectacle['Lieu'][i]+" - "+df_spectacle['Ville'][i])
                st.markdown(df_spectacle['Type'][i])
                st.markdown(str(df_spectacle['Prix'][i]) + " €")
                st.markdown( df_spectacle['Artiste'][i])
            with btn_column:
                btn=st.button("Ajouter",key=i)
                if btn:
                    df_selected.append(df_spectacle.iloc[i]).to_csv('selected.csv',index=False)
            st.write("----------------------------------------------------------------------")

if selected == 'Humour et One man show':
    for i in range(5):
        with st.container():
            image_column, text_column, btn_column =st.columns((4,12,3))            
            with image_column:  
                st.image(df_humour['Image'][i],width=140)
            with text_column:
                st.markdown(df_humour['Date'][i])
                st.markdown(df_humour['Lieu'][i]+" - "+df_humour['Ville'][i])
                st.markdown(df_humour['Type'][i])
                st.markdown(str(df_humour['Prix'][i]) + " €")
                st.markdown( df_humour['Artiste'][i])
            with btn_column:
                btn=st.button("Ajouter",key=i)
                if btn:
                    df_selected.append(df_humour.iloc[i]).to_csv('selected.csv',index=False)
            st.write("----------------------------------------------------------------------")

if selected == 'Sport':
    for i in range(5):
        with st.container():
            image_column, text_column, btn_column =st.columns((4,12,3))            
            with image_column:  
                st.image(df_sport['Image'][i],width=140)
            with text_column:
                st.markdown(df_sport['Date'][i])
                st.markdown(df_sport['Lieu'][i]+" - "+df_sport['Ville'][i])
                st.markdown(df_sport['Type'][i])
                st.markdown(str(df_sport['Prix'][i]) + " €")
                st.markdown( df_sport['Artiste'][i])
            with btn_column:
                btn=st.button("Ajouter",key=i)
                if btn:
                    df_selected.append(df_sport.iloc[i]).to_csv('selected.csv',index=False)
            st.write("----------------------------------------------------------------------")

if selected == 'Parc':
    for i in range(5):
        with st.container():
            image_column, text_column, btn_column =st.columns((4,12,3))            
            with image_column:  
                st.image(df_parc['Image'][i],width=140)
            with text_column:
                st.markdown(df_parc['Date'][i])
                st.markdown(df_parc['Lieu'][i]+" - "+df_parc['Ville'][i])
                st.markdown(df_parc['Type'][i])
                st.markdown(str(df_parc['Prix'][i]) + " €")
                st.markdown( df_parc['Artiste'][i])
            with btn_column:
                btn=st.button("Ajouter",key=i)
                if btn:
                    df_selected.append(df_parc.iloc[i]).to_csv('selected.csv',index=False)
            st.write("----------------------------------------------------------------------")
 

if selected == 'Exposition et musée':
    for i in range(5):
        with st.container():
            image_column, text_column, btn_column =st.columns((4,12,3))            
            with image_column:  
                st.image(df_expo['Image'][i],width=140)
            with text_column:
                st.markdown(df_expo['Date'][i])
                st.markdown(df_expo['Lieu'][i]+" - "+df_expo['Ville'][i])
                st.markdown(df_expo['Type'][i])
                st.markdown(str(df_expo['Prix'][i]) + " €")
                st.markdown( df_expo['Artiste'][i])
            with btn_column:
                btn=st.button("Ajouter",key=i)
                if btn:
                    df_selected.append(df_expo.iloc[i]).to_csv('selected.csv',index=False)
            st.write("----------------------------------------------------------------------")

if selected == 'Théâtre':
    for i in range(5):
        with st.container():
            image_column, text_column, btn_column =st.columns((4,12,3))            
            with image_column:  
                st.image(df_theatre['Image'][i],width=140)
            with text_column:
                st.markdown(df_theatre['Date'][i])
                st.markdown(df_theatre['Lieu'][i]+" - "+df_theatre['Ville'][i])
                st.markdown(df_theatre['Type'][i])
                st.markdown(str(df_theatre['Prix'][i]) + " €")
                st.markdown( df_theatre['Artiste'][i])
            with btn_column:
                btn=st.button("Ajouter",key=i)
                if btn:
                    df_selected.append(df_theatre.iloc[i]).to_csv('selected.csv',index=False)
            st.write("----------------------------------------------------------------------")

if selected == 'Cirque':
    for i in range(5):
        with st.container():
            image_column, text_column, btn_column =st.columns((4,12,3))            
            with image_column:  
                st.image(df_cirque['Image'][i],width=140)
            with text_column:
                st.markdown(df_cirque['Date'][i])
                st.markdown(df_cirque['Lieu'][i]+" - "+df_cirque['Ville'][i])
                st.markdown(df_cirque['Type'][i])
                st.markdown(str(df_cirque['Prix'][i]) + " €")
                st.markdown( df_cirque['Artiste'][i])
            with btn_column:
                btn=st.button("Ajouter",key=i)
                if btn:
                    df_selected.append(df_cirque.iloc[i]).to_csv('selected.csv',index=False)
            st.write("----------------------------------------------------------------------")

if selected == 'Salon':
    for i in range(5):
        with st.container():
            image_column, text_column, btn_column =st.columns((4,12,3))            
            with image_column:  
                st.image(df_salon['Image'][i],width=140)
            with text_column:
                st.markdown(df_salon['Date'][i])
                st.markdown(df_salon['Lieu'][i]+" - "+df_salon['Ville'][i])
                st.markdown(df_salon['Type'][i])
                st.markdown(str(df_salon['Prix'][i]) + " €")
                st.markdown( df_salon['Artiste'][i])
            with btn_column:
                btn=st.button("Ajouter",key=i)
                if btn:
                    df_selected.append(df_salon.iloc[i]).to_csv('selected.csv',index=False)
            st.write("----------------------------------------------------------------------")

if selected == 'Danse':
    for i in range(5):
        with st.container():
            image_column, text_column, btn_column =st.columns((4,12,3))            
            with image_column:  
                st.image(df_danse['Image'][i],width=140)
            with text_column:
                st.markdown(df_danse['Date'][i])
                st.markdown(df_danse['Lieu'][i]+" - "+df_danse['Ville'][i])
                st.markdown(df_danse['Type'][i])
                st.markdown(str(df_danse['Prix'][i]) + " €")
                st.markdown( df_danse['Artiste'][i])
            with btn_column:
                btn=st.button("Ajouter",key=i)
                if btn:
                    df_selected.append(df_danse.iloc[i]).to_csv('selected.csv',index=False)
            st.write("----------------------------------------------------------------------")

if selected == 'Classique et opéra':
    for i in range(5):
        with st.container():
            image_column, text_column, btn_column =st.columns((4,12,3))            
            with image_column:  
                st.image(df_classique['Image'][i],width=140)
            with text_column:
                st.markdown(df_classique['Date'][i])
                st.markdown(df_classique['Lieu'][i]+" - "+df_classique['Ville'][i])
                st.markdown(df_classique['Type'][i])
                st.markdown(str(df_classique['Prix'][i]) + " €")
                st.markdown( df_classique['Artiste'][i])
            with btn_column:
                btn=st.button("Ajouter",key=i)
                if btn:
                    df_selected.append(df_classique.iloc[i]).to_csv('selected.csv',index=False)
            st.write("----------------------------------------------------------------------")

if selected == 'Loisirs et tourisme':
    for i in range(5):
        with st.container():
            image_column, text_column, btn_column =st.columns((4,12,3))            
            with image_column:  
                st.image(df_loisir['Image'][i],width=140)
            with text_column:
                st.markdown(df_loisir['Date'][i])
                st.markdown(df_loisir['Lieu'][i]+" - "+df_loisir['Ville'][i])
                st.markdown(df_loisir['Type'][i])
                st.markdown(str(df_loisir['Prix'][i]) + " €")
                st.markdown( df_loisir['Artiste'][i])
            with btn_column:
                btn=st.button("Ajouter",key=i)
                if btn:
                    df_selected.append(df_loisir.iloc[i]).to_csv('selected.csv',index=False)
            st.write("----------------------------------------------------------------------")

if selected == 'Soirée':
    for i in range(4):
        with st.container():
            image_column, text_column, btn_column =st.columns((4,12,3))            
            with image_column:  
                st.image(df_soiree['Image'][i],width=140)
            with text_column:
                st.markdown(df_soiree['Date'][i])
                st.markdown(df_soiree['Lieu'][i]+" - "+df_soiree['Ville'][i])
                st.markdown(df_soiree['Type'][i])
                st.markdown(str(df_soiree['Prix'][i]) + " €")
                st.markdown( df_soiree['Artiste'][i])
            with btn_column:
                btn=st.button("Ajouter",key=i)
                if btn:
                    df_selected.append(df_soiree.iloc[i]).to_csv('selected.csv',index=False)
            st.write("----------------------------------------------------------------------")  

