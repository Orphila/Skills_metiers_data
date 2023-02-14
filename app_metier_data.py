#---------------Construction app st-----------------------------------------

import streamlit as st  
import plotly.express as px  
import matplotlib.pyplot as plt

st.set_page_config(page_title="Skills pour métiers data", 
                   page_icon=":bar_chart:",
                   layout="wide")
# ---- MAINPAGE ----
st.title(":bar_chart: Skills pour métiers de la data")

import pymongo
import os
username = str(os.environ.get("MONGODB_USERNAME"))
password = str(os.environ.get("MONGODB_PASSWORD"))


link ="mongodb+srv://"+username+":"+password+"!@cluster0.osnqmmc.mongodb.net/test?authMechanism=DEFAULT"
client = pymongo.MongoClient(link)
db = client["dashboard_metiers_data"]
collection = db["data"]
cursor = collection.find({})

import pandas as pd
st.markdown(username)
st.markdown(list(cursor))

df = pd.DataFrame(list(cursor))
client.close()
df = df.drop('_id',axis=1)
#df = pd.read_json("df2.json")
df = df.rename(columns={'outil': 'Outils'})
df = df.rename(columns={'package': 'Modules'})
df = df.rename(columns={'tech': 'Langages'})
for i in range(len(df)):
    if 'Paris' in df.loc[i]['lieu']:
        df.loc[i]['lieu']='Paris'
    if 'Marcq-En-Baroeul' in df.loc[i]['lieu']:
        df.loc[i]['lieu']='Marcq-En-Baroeul'
    if 'Montpellier' in df.loc[i]['lieu']:
        df.loc[i]['lieu']='Montpellier'

import plotly.express as px

#----- Filtre métiers
st.sidebar.header("Filtrez les métiers qui vous intéresse")
liste_metiers=list(df['poste'].unique())
metiers = st.sidebar.multiselect("Selectionnez les métiers:",
                            options=liste_metiers,
                            default=liste_metiers)

df_selection = df.query("poste == @metiers")

# ---- Création des graphs ---
def dip(df):
    """
    obtenir les données pour le piechart
    """
    list_diplomes=[]
    EX  =  ['Doctorat','Master','License']
    
    for k in EX: #On vérifie que tous les métiers sont dans la sélection
        if k in list(df['diplome']):
            list_diplomes.append(k)
    
    nb_diplomes_asked=[df['diplome'].value_counts()[diplome] for diplome in list_diplomes]
    
    dip_res = pd.DataFrame({'nombre': nb_diplomes_asked,
                       'diplome': list_diplomes})
    
    return dip_res
fromage = px.pie(dip(df_selection), values='nombre', names='diplome')
fromage.update_layout(title_text="Répartition des diplômes demandés")
fromage.update_traces(hole=0.55)
fromage.update_layout(height=400, width=300)


def get_nb_techs(recherche):
    """
    donne les données des techs/outils/packages (recherche) 
    pour un metier
    """
    data = df_selection[recherche]
    list_techs={}
    for i in list(data.index):
        techs = data.loc[i]
        for tech in techs:
            if tech not in list_techs: #Si la tech n'est pas dans le dico, on l'ajoute
                list_techs[tech]=0 
            if tech=='powerbi':
                print('powerbi est  là')
            else:
                list_techs[tech]+=1 #Sinon on l'a croisée une fois de plus, on l'ajoute 
    return list_techs
 
def bar_techs(recherche):
    """
    On crée le barchart pour les techs/outils/packages (recherche) 
    """
    list_techs = get_nb_techs(recherche)
    list_techs = pd.DataFrame(list(list_techs.items()), 
                              columns=[recherche, 'Nombre'])
    list_techs = list_techs.sort_values(by='Nombre',ascending=False)
    chart = px.bar(
    list_techs,
    x=recherche,
    y='Nombre',
    title=recherche + " les plus recherchés"
    )
    chart.update_traces(marker_color='red')
    chart.update_layout(height=400, width=300)
    return chart
    
def carte(df):
    df_counts = df.groupby("lieu").size().reset_index(name="counts")
    fig = px.treemap(df_counts,
                     path=["lieu"],
                     values="counts",
                     title="Répartition des villes des offres")
    fig.update_layout(height=500, width=700)
    return fig
# ---- Affichage des graphs ----


#----test BAR CHART ----


#----test BAR CHART ----

col_left,col_mid,col_right=st.columns(3)

col_left.plotly_chart(bar_techs('Langages'))
col_mid.plotly_chart(bar_techs('Outils'))
col_right.plotly_chart(bar_techs('Modules'))

st.markdown("""---""")

left_column, right_column = st.columns([2,1])

left_column.plotly_chart(carte(df_selection))
right_column.plotly_chart(fromage)



