import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from datetime import datetime
from datetime import timedelta
from urllib import request
from bs4 import BeautifulSoup

#Fonction qui transforme un mois en format lettre en format numérique string : janv. -> 01
def from_string_to_date_month(str_month):
    nb_month=0
    if(str_month=='janv.'):
        nb_month="01"
    elif(str_month=='fev.'):
        nb_month="02"
    elif(str_month=='mars'):
        nb_month="03"
    elif(str_month=='avr.'):
        nb_month="04"
    elif(str_month=='mai'):
        nb_month="05"
    elif(str_month=='juin'):
        nb_month="06"
    elif(str_month=='juil.'):
        nb_month="07"
    elif(str_month=='août'):
        nb_month="08"
    elif(str_month=='sept.'):
        nb_month="09"
    elif(str_month=='oct.'):
        nb_month="10"
    elif(str_month=='nov.'):
        nb_month="11"
    elif(str_month=='dec.'):
        nb_month="12"
    return nb_month
#Fonction qui transforme une date de format 08 avr. 2023 en format 2023-04-08
def from_string_to_date(str_date):
    #La fonction prends en compte les différents types de dates, on split la date et on regarde la taille du tableau
    #Si la taille est de 3, on a une date du style 08 avr. 2023
    #Si la taille est de 5, on a une date du style 07 au 08 avr. 2023
    #Si la taille est de 6, on a une date du style 08 mars au 08 avr. 2023
    #Si la taille est de 7, on a une date du style 08 dec. 2022 au 08 avr. 2023
    #Si la date correspond à un créneau de date, la fonction va toujours retourner la date correspondant au début
    arr_date=str_date.split(" ")
    year=arr_date[len(arr_date)-1]
    day=arr_date[0]
    if(len(arr_date)==3 or len(arr_date)==6):
        month=from_string_to_date_month(arr_date[1])
    elif(len(arr_date)==7):
        year = arr_date[2]
        month=from_string_to_date_month(arr_date[1])
    elif(len(arr_date)==5):
        month=from_string_to_date_month(arr_date[3])
    return datetime.strptime(year+"-"+month+"-"+day, '%Y-%m-%d')
#Fonction qui permet de récupérer les airbnb d'une ville pour une période donnée  
def scrap_airbnb(place, date_debut, date_fin):
    #On récupère la page html de la recherche en fonction de la ville, de la date de début et de la date de fin
    url="https://www.airbnb.fr/s/"+place+"/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&price_filter_num_nights=1&date_picker_type=calendar&checkin="+date_debut+"&checkout="+date_fin+"&source=structured_search_input_header&search_type=search_query"
    request_text = request.urlopen(url).read()
    htmlpage= BeautifulSoup(request_text, features="html.parser")

    #On stocke les résultats dans un tableau de dictionnaire
    hotels=[]
    for item in htmlpage.findAll('div',{'class':'lwy0wad l1tup9az dir dir-ltr'}):
        try:
            hotel={}
            hotel['Titre']=item.find('div',{'class':'t1jojoys dir dir-ltr'}).text.replace('\n','')
            hotel['Type']=item.find('span',{'class':'t6mzqp7 dir dir-ltr'}).text.replace('\n','')
            hotel['Lit']=item.find('div',{'class':'f15liw5s s1cjsi4j dir dir-ltr'}).text.replace('\n','')
            Prix = item.find('div',{'class':'_tt122m'}).text.strip().replace('\n','').replace('€ au total','').replace('\u202f','')
            hotel['Prix']=int(Prix)
            item_rating=item.find('span',{'class':'r1dxllyb dir dir-ltr'})
            #Si la note n'est pas renseignée, ce qui peut être le cas pour les nouveaux logements on ne l'ajoute pas dans le tableau
            if(item_rating == None):
                continue
            else:
                #Puisque le text qu'on récupère est de la forme 4.7(120), on enlève d'abord le ")" on split sur le "("" 
                # Et on récupère la note et le nombre de revues dans un tableau
                rating= item_rating.text.replace(')','').split('(')
                if(len(rating)==2):
                    hotel['Note (sur 5)']=rating[0]
                    hotel['Nombre de revues']=rating[1]
            hotel['Link']="https://www.airbnb.fr/"+str(item.find('div',{'class':'c14whb16 dir dir-ltr'}).find('a')['href'])
            hotels.append(hotel)
        except:
            continue
    return pd.DataFrame(hotels)

#Dataframe des évènements que l'utilisateur a choisi
df_selected = pd.read_csv('selected.csv')

#Tableau des plus grandes villes afin de savoir si on effectue une recherche sur une ville ou sur un lieu d'évènement
biggest_cities = ["PARIS", "MARSEILLE", "LYON", "TOULOUSE", "NICE", "NANTES", "MONTPELLIER", "STRASBOURG", "BORDEAUX", "LILLE"]

if(len(df_selected)==0):
    st.header("Vous n'avez choisi aucun évènement")
else:
    st.header("Liste de airbnb")
    st.write("")
    for i in range(len(df_selected)):
            with st.container():
                #On réaffiche l'image, la date, le lieu, le type, le prix et les artistes
                image_column, text_column =st.columns((1,3.5))
                with image_column:  
                    st.image(df_selected['Image'][i],width=140)
                with text_column:
                    st.markdown(df_selected['Date'][i])
                    st.markdown(df_selected['Lieu'][i]+" - "+df_selected['Ville'][i])
                    st.markdown(df_selected['Type'][i])
                    st.markdown(str(df_selected['Prix'][i]) + " €")
                    st.markdown(df_selected['Artiste'][i])

                #Si la date de début de l'évènement est antérieure à la date d'aujourd'hui, on affiche la date d'aujourd'hui à la place
                dt=from_string_to_date(df_selected['Date'][i]).date()
                if dt < datetime.today().date():
                    date_debut=datetime.today().date()
                else:
                    date_debut=dt
                date_event=st.date_input("Veuillez saisir la date à laquelle vous souhaitez assister à chaque évènement", date_debut, key=i)
                date_fin=(date_debut+ timedelta(days=1)).strftime('%Y-%m-%d')
                date_debut=date_debut.strftime('%Y-%m-%d')

                #Si la ville est une des plus grandes villes, on effectue la recherche sur le lieu de l'évènement
                if(str(df_selected['Ville'][i]).upper() in biggest_cities):
                    place=df_selected['Lieu'][i].replace(' ', '-')
                #Sinon on effectue la recherche sur la ville
                else:
                    place=df_selected['Ville'][i].replace(' ', '-')

                #On récupère les différents logements autour de l'évènement
                df_airbnb=scrap_airbnb(place,date_debut,date_fin)
                df_airbnb.dropna(how='any', inplace=True) #On supprime les lignes qui possèdent des attributs vides

                #Selon le choix de l'utilisateur, on trie le tableau par prix ou par note, l'option par défaut sera le prix
                sort_choice=st.selectbox("Choisissez de trier par:",['Prix','Note'],key=i+100)
                if (sort_choice=="Prix"):
                    df_airbnb.sort_values(by=['Prix'], inplace=True)
                if (sort_choice=="Note"):
                    df_airbnb.sort_values(by=['Note (sur 5)'], inplace=True, ascending=False)

                titre_column, type_column, lit_column, prix_column, note_column, nbrevue_column =st.columns((4,6,2,1,1.5,2))
                with titre_column:
                    st.markdown('Titre')
                with type_column:
                    st.markdown('Type')
                with lit_column:
                    st.markdown('Lit')
                with prix_column:
                    st.markdown('Prix (€)')
                with note_column:
                    st.markdown('Note (sur 5)')
                with nbrevue_column:
                    st.markdown('Nombre de revues')
                #Affiche tous les logements
                for index, row in df_airbnb.iterrows():
                    with st.container():
                        titre_column, type_column, lit_column, prix_column, note_column, nbrevue_column =st.columns((4,6,2,1,1.5,2))
                        with titre_column:
                            #On affiche le titre du logement avec l'option de cliquer pour être redirigé vers le site d'Airbnb
                            st.markdown(f"[{row['Titre']}]({row['Link']})")
                        with type_column:
                            st.markdown(row['Type'])
                        with lit_column:
                            st.markdown(row['Lit'])
                        with prix_column:
                            st.markdown(row['Prix'])
                        with note_column:
                            st.markdown(row['Note (sur 5)'])
                        with nbrevue_column:
                            st.markdown(row['Nombre de revues'])
                st.write("----------------------------------------------------------------------")
            