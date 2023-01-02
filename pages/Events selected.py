import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import pyautogui

placeholder = st.empty()
df_selected = pd.read_csv('selected.csv')

st.title("Évènements choisis")
st.header("Voici les évènements que vous avez choisi:")

for i in range(len(df_selected)):
    with st.container():
        image_column, text_column, btn_column =st.columns((4,12,3))
        with image_column:  
            st.image(df_selected['Image'][i],width=140)
        with text_column:
            st.markdown(df_selected['Date'][i])
            st.markdown(df_selected['Lieu'][i]+" - "+df_selected['Ville'][0])
            st.markdown(df_selected['Type'][i])
            st.markdown(str(df_selected['Prix'][i]) + " €")
            st.markdown(df_selected['Artiste'][i])
        with btn_column:
            btn=st.button("Retirer",key=i)
            if btn:
                df_selected.drop(df_selected.index[i]).to_csv('selected.csv',index=False)
                pyautogui.hotkey("F5")
        st.write("----------------------------------------------------------------------")