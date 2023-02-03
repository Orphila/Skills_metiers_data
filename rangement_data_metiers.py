import pandas as pd
import numpy as np
"""
df = pd.read_excel("res_metiers_data_1.xlsx")


print(df)
"""

def recherche_poste(offre):
    poste=offre[0].lower()
    if 'data analyst' in poste:
        return 'data analyst'
    if 'data scientist' in poste:
        return 'data scientist'
    if 'data engineer' in poste or 'ingénieur data' in poste:
        return 'data engineer'
    return 'Null'

def recherche_contrat(offre):
    return offre['contrat']

def recherche_ville(offre):
    return offre['ville']

def recherche_diplome(offre):
    profil=offre[2]
    for i in profil:
        if 'phd' in i.lower() or 'doctorat' in i.lower():
            return 'Doctorat'
        if  'bac+3' in i.lower().replace(" ", ""):
            return 'License'
    return 'Master'

def recherche_technos(offre):
    technos=['python','sql','java','scala','matlab','javascript']
    profil=offre[2]
    techs=[]
    for i in profil:
        p=i.lower()
        for j in technos:
            if j in p:
                techs.append(j)
        if ' R ' in i:
            techs.append('R')
            print('on demande du R')
        if ' SAS ' in i:
            techs.append('SAS')
            print('on demande du SAS')
    return techs
def recherche_outils(offre):
    outils=['aws','azure','gcp','git','tableau','talend','qlik','excel','mongodb'
            'powerbi','jira','kubernetes','docker','jenkis','dataiku']
    profil=offre[2]
    outil=[]
    for i in profil:
        p=i.lower()
        for j in outils:
            if j in p:
                outil.append(j)
            if 'google cloud' in p:
                outil.append('gcp')
    return outil
def recherche_packages(offre):
    packages=['sklearn','tensorflow','seaborn','matplotlib','keras','pandas',
              'spark','pytorch','plotly','ggplot2','data.table','shiny','knitre',
              'mlr3','dplyr','tidyr','streamlit']
    profil=offre[2]
    package=[]
    for i in profil:
        p=i.lower()
        for j in packages:
            if j in p:
                package.append(j)
        if 'scikit' in p:
            package.append('sklearn')
    return package



def data(df):
    df2 = pd.DataFrame(columns=["poste",
                               "contrat", 
                               "lieu", 
                               "diplome", 
                               "tech", 
                               "outil", 
                               "package"])
    for i in range(len(df)):
        row=df.loc[i]
        print('row = ',row)
        Poste = list(np.unique(recherche_poste(row)))[0]
        Contrat = list(np.unique(recherche_contrat(row)))[0]
        Ville = list(np.unique(recherche_ville(row)))[0]
        Diplome = list(np.unique(recherche_diplome(row)))[0]
        Technos = list(np.unique(recherche_technos(row)))
        Outils = list(np.unique(recherche_outils(row)))
        Packages = list(np.unique(recherche_packages(row)))
        df2.loc[len(df2)] = [Poste, 
                           Contrat, 
                           Ville,
                           Diplome,
                           Technos,
                           Outils,
                           Packages]
    return df2

