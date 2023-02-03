import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.common.by import By


df = pd.DataFrame(columns=["titre_offre", 
                           "caractéristiques_contrat", 
                           "profil recherché"])

def g_url(page,metier):
    res = "https://www.welcometothejungle.com/fr/jobs?page="+str(page)+"&groupBy=job&sortBy=mostRelevant&query=data%20"+str(metier)
    return res

def recup(page,metier):

    url=g_url(page,metier)
    """
    options = webdriver.EdgeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    driver = webdriver.Edge(options=options)
    """
    driver = webdriver.Edge()
    driver.get(url)
    time.sleep(3)
    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content,"html.parser")
    titres = soup.find_all('div',{"class":"sc-1peil1v-4 fOyHIw"})
    liens=driver.find_elements(By.XPATH,"//a[@display='inline']")
    for k in range(len(liens)):
        liens[k]=liens[k].get_attribute('href')
    for k in range(len(titres)):
        titres[k]=titres[k].get_text()
    job_elements = driver.find_elements(By.XPATH,"//li[@class='ais-Hits-list-item']")
    #list_job=[]
    offres=[]
    main_window = driver.current_window_handle
    for job_element in job_elements:
        job_element.click()
        i=job_elements.index(job_element)
        current_url = liens[i]
        time.sleep(3)
        description = job_element.find_elements(By.XPATH,'.//li[@class="sc-16yjgsd-0 dalnlt"]')
        driver2 = webdriver.Edge()
        driver2.get(current_url)
        time.sleep(3)
        content = driver2.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content,"html.parser")
        profils = soup.find_all('div',{"class":"itvpid-1 jpqriD"})
        profil=list()
        driver2.close()
        for k in profils:
            profil.append(k.get_text())
        for k in range(len(description)): 
            """
            Différents éléments (salaire, adresse, contrat, lieu) sont dans la description,
            mais pas toujour les mêmes. On les ajoute tous, on triera après
            """
            description[k]=description[k].text
        
        offres.append([titres[i],description,profil])
        driver.switch_to.window(main_window) #On reviens à la première fenêtre

    driver.close()
    return offres

métiers=['analyst','scientist','engineer']

def data(metier,nb_pages):
    liste=[]
    for i in range(nb_pages):
        print("on est sur la page num ",i)
        
        for j in recup(i,metier):
            liste.append(j)
            print("poste num ",len(liste))
    return liste
data_analyst = data('analyst',10)
data_scientist = data('scientist',10)
data_engineer = data('engineer',10)

all_data = []
all_data.extend(data_analyst)
all_data.extend(data_scientist)
all_data.extend(data_engineer)

res = pd.DataFrame(all_data, columns=["titre_offre", "caractéristiques_contrat", "profil recherché"])
        
df.to_excel("data_metiers_data_1")
 