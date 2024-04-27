# Comptes rendus des TP et projet de Data Visualisation
Hien Dinh & Laura Korenfeld 
EPISEN ITS3 - FISA


**TP/Projet DataViz avec la stack ELK**

L'objectif de ce TP/Projet est de prendre en main la stack ELK afin de mener un projet de bout en bout de collecte et de représentation de data.

Prise en main de la stack ELK

*Partie 01*

Requirements, demarrage de la stack et injection des data de demo

*Partie 02*

Nous avons créé notre premier index pattern  pour faciliter les requêtes et l'analyse des données. Nous l’avons nommé “log*”.
Voici le résultats de nos premières visualisations :

Répartition homme/femme mise en avant par un graphique circulaire. Comme nous avons deux catégories, ce graphique permet d'aisément repérer les proportions au premier coup d'oeil.

<img width="287" alt="Capture d’écran 2024-04-05 à 17 11 05" src="https://github.com/laurakorenfeld/datavisualisation_Dinh_Korenfeld/assets/102244020/2caf0334-2183-4a33-9017-3b99e8140622">

Top 10 des noms représenté par un histogramme horizontal. Chaque barre représentant un nom, on voit facilement que Judith et Michelle sont les plus répandus.

<img width="287" alt="Capture d’écran 2024-04-05 à 17 11 25" src="https://github.com/laurakorenfeld/datavisualisation_Dinh_Korenfeld/assets/102244020/685f1ea5-ac34-4a0c-8944-e6a55f141156">

Top 10 des villes représenté par un histogramme vertical. Emiliano Zapata est la ville qui est la plus présente dans le jeu de données avec 3 occurences.

<img width="287" alt="Capture d’écran 2024-04-05 à 17 11 58" src="https://github.com/laurakorenfeld/datavisualisation_Dinh_Korenfeld/assets/102244020/890f0f55-0290-4ba2-b0e9-6a2e20c63034">

Affichage du nombre de versions differentes il y a. La visualisation metric fournit un aperçu immédiat d'une métrique clé. 

<img width="287" alt="Capture d’écran 2024-04-05 à 17 12 20" src="https://github.com/laurakorenfeld/datavisualisation_Dinh_Korenfeld/assets/102244020/771bc31b-0d6f-4ca1-89fd-2c7e873a0f51">



**Dashboard regroupant ces visualizations :**

<img width="576" alt="Capture d’écran 2024-04-05 à 17 13 15" src="https://github.com/laurakorenfeld/datavisualisation_Dinh_Korenfeld/assets/102244020/78002f0e-484e-4be3-b0bc-dd9afc7377fd">



*Partie 03*

cleanez les data que vous avez injecté dans votre stack (en utilisant Cerebro)

changez la conf de logstash pour créer un nouveau champs email_domain reprenant le domain de l'adresse mail uniquement (erwan@aleikoum.net > aleikoum.net), pensez à regarder comment mutate fonctionne
une fois que c'est ok, créez une visualization avec le top 10 des domaines

<img width="527" alt="Capture d’écran 2024-04-27 à 09 49 13" src="https://github.com/laurakorenfeld/datavisualisation_Dinh_Korenfeld/assets/102244020/95e8cb7a-bb08-4305-aab3-a62294e9cf82">

Ce code nous permet d'ajouter un champ, "email_domain". On a en fait dupliqué le champ "email". On a ensuite séparer le mail par le symbole "@" pour enfin ne garder que la deuxième partie du champ "email_domain", qui correspond au nom de domaine.

<img width="604" alt="Capture d’écran 2024-04-27 à 20 21 18" src="https://github.com/laurakorenfeld/datavisualisation_Dinh_Korenfeld/assets/102244020/e786ea70-7335-4a1a-82f0-95dfcf0ef196">

<img width="605" alt="Capture d’écran 2024-04-27 à 20 21 39" src="https://github.com/laurakorenfeld/datavisualisation_Dinh_Korenfeld/assets/102244020/7be88805-6c08-41a6-b1f5-d06184506fed">


Nous avons également supprimé le champ message qui était redondant. En effet, toutes les informations qu'il contient sont contenues dans les autres champs.

<img width="423" alt="Capture d’écran 2024-04-27 à 20 22 21" src="https://github.com/laurakorenfeld/datavisualisation_Dinh_Korenfeld/assets/102244020/509f3b0c-4a23-4259-acf9-2730df79b1d7">

La visualisation représente le top 10 des domaines d'e-mail classés par le nombre d'occurrences. Chaque barre horizontale correspond à un domaine spécifique et la longueur de la barre révèle le nombre d'occurrences de chancun des noms de domaine représentés.
Les domaines “ebay.co.uk” et “tiny.cc” sont les plus utilisés..

Voici le rendu final de notre dashbord :

<img width="586" alt="Capture d’écran 2024-04-27 à 20 24 49" src="https://github.com/laurakorenfeld/datavisualisation_Dinh_Korenfeld/assets/102244020/d5e0af1e-d2e9-45d2-ba93-eb7e42f0429b">

*Conclusion : *

Ce TP nous a permis de manipuler différentes visualisation et de nous initier à la complexité du choix du modèle qui permet de mettre en avant les données de manière claire.
Le lancement via Docker nous a permis d'avancer rapidement sur le projet sans nous préoccuper des installations de Kibana.

**Projet de datavisualization**


