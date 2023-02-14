# Skills métiers de la data

Ce projet personnel a pour but de vérifier quelles sont les compétences les plus attendues pour des métiers dans le domaine des sciences de données, à savoir data analyst/data scientist/data engineer. Dans l'optique où un étudiant chercherais à améliorer ses compétences dans certaines technologies ou framework, et qu'il peinerait à faire des choix, ceci permet de se guider pour savoir ce que les recruteurs veulent vraiment. Me posant la question moi-même lors de ma recherche d'emploi, j'ai décidé d'y répondre par moi même.

# Récupération et stockage des données

Je me suis basé sur des données scrappées sur le site WelcomeToTheJungle. J'ai récupéré celles-ci avec selenium et BeautifulSoup. Dans un premier temps, j'ai stocké ces données dans un fichier json. Cependant, étant donné que de nouvelles offres arrivent constament, j'ai trouvé pertinant d'utiliser plutôt une base de données NoSQL (mongoDB), ce qui me permettait d'ajouter facilement des données à celle-ci. 

# Présentation des résultat

J'ai choisi de représenter les découvertes sur un dashboard accessible publiquement à ce lien : https://skills-metiers-data.streamlit.app/, fait à partir du framework streamlit de python. L'application se connecte automatiquement à la base de données quand on l'ouvre, et affiche les graphiques actualisés.

# Perspectives

J'ai pu relever un certain nombre d'informations assez intéressantes avec ce projet.
-L'extrême majorité des offres d'emploi se trouve en île de france (dont à peu près la moitié à paris même).
-Il semble presque inenvisageable, de trouver un travail en tant que data scientist ou engineer sans master, et le doctorat est souvent un plus.
-Il est presque autant indispensable pour un data scientist de maîtriser SQL que python pour trouver un emploi. Savoir utiliser R est très rarement exigé, encore moins que java.
-Les trois principaux services cloud (AWS, Azure, GCP) sont presque aussi demandés les uns que les autres, avec une légère avance pour Azure.

# Conclusion

J'ai pu répondre aux questions que je me posait, et créer une visualisation claire pour cela. Les objectifs du projt ont été remplis, et j'ai appris à utiliser une technologie NoSQL.

