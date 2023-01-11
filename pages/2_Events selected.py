import streamlit as st
import pandas as pd
import pyautogui

#Dataframe des évènements que l'utilisateur a choisi
df_selected = pd.read_csv('selected.csv')

st.title("Évènements choisis")

#Si aucun évènement n'a été choisi, on affiche un message correspondant
if(len(df_selected)==0):
    st.header("Vous n'avez choisi aucun évènement")
else:
    st.header("Voici les évènements que vous avez choisi :")
    st.write(' ')
    for i in range(len(df_selected)):
        with st.container():
            #On réaffiche l'image, la date, le lieu, le type, le prix et les artistes
            image_column, text_column, btn_column =st.columns((4,12,3))
            with image_column:  
                st.image(df_selected['Image'][i],width=140)
            with text_column:
                st.markdown(df_selected['Date'][i])
                st.markdown(df_selected['Lieu'][i]+" - "+df_selected['Ville'][i])
                st.markdown(df_selected['Type'][i])
                st.markdown(str(df_selected['Prix'][i]) + " €")
                st.markdown(df_selected['Artiste'][i])
            with btn_column:
                #Ajout d'un bouton pour retirer l'évènement de ses choix en mettant à jour le fichier selected.csv 
                #On va également réactualiser la page en faisant un F5 pour enlever de l'affichage l'évèmenent en question
                btn=st.button("Retirer",key=i)
                if btn:
                    df_selected.drop(df_selected.index[i]).to_csv('selected.csv',index=False)
                    pyautogui.hotkey("F5")
            st.write("----------------------------------------------------------------------")