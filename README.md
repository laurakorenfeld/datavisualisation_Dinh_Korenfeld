# Comptes rendus des TP et projet de Data Visualisation
Hien Dinh & Laura Korenfeld 
EPISEN ITS3 - FISA


## TP/Projet DataViz avec la stack ELK

L'objectif de ce TP/Projet est de prendre en main la stack ELK afin de mener un projet de bout en bout de collecte et de représentation de data.

Prise en main de la stack ELK

### Partie 01

Requirements, demarrage de la stack et injection des data de demo

### Partie 02

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



### Partie 03

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

### Conclusion :

Ce TP nous a permis de manipuler différentes visualisations et de nous initier à la complexité du choix du modèle qui permet de mettre en avant les données de manière claire.
Le lancement via Docker nous a permis d'avancer rapidement sur le projet sans nous préoccuper des installations de Kibana.

## Projet de datavisualization


Dans le cadre de notre projet de Data Visualisation, nous avons créé un système de collecte et de visualisation de données météorologiques en utilisant la stack ELK. Notre objectif était de mettre en place une infrastructure robuste pour la collecte, le stockage et l'analyse des données météorologiques provenant de différentes villes. 

Pour cela, nous avons sélectionné l'API Open-Meteo, c'est un service gratuit qui permet aux développeurs d'accéder à des données météorologiques en temps réel et prévisionnelles pour différentes régions à travers le monde. Cette API offre un accès facile et flexible à une vaste gamme de données météorologiques, telles que les températures actuelles, les conditions météorologiques, les précipitations, la vitesse du vent, la visibilité,...

Grâce à cette API, il est possible d'intégrer ces informations dans diverses applications, sites Web et projets, y compris des projets de visualisation de données. 

Pour ce projet, nous avons sélectionné 10 villes françaises afin d'en comparer différentes données météoroliques. Cette étude montrera donc les villes de :

- Bordeaux
- Lille
- Lyon
- Nice
- Paris
- Rennes
- Rouen
- Strasbourg
- Toulouse
- Tours

## Méthodologie 

Dans le but d'obtenir les données de ces villes, il nous a fallu récupérer leur position géographique caractérisée par la latitude et la longitude.

<img width="623" alt="Capture d’écran 2024-04-30 à 09 50 48" src="https://github.com/laurakorenfeld/datavisualisation_Dinh_Korenfeld/assets/102244020/18ed46e5-ee40-46c4-8ba0-97ba1129d636">

Pour chacune d'entre elles, nous avons selectionné les critères suivant : température, précipitations (pluie, neige) et couverture nuageuse.

Nous avons configuré les composants de la stack ELK : Elasticsearch, Logstash, Kibana et Cerebro. Elasticsearch a été utilisé comme moteur de recherche et de stockage des données, Logstash pour le traitement des flux de données, Kibana pour la visualisation et l'analyse des données, et Cerebro pour la gestion des index Elasticsearch.

Nous avons développé un script Python pour interroger l'API et récupérer les données horaires pour chaque ville spécifiée. Les données ont été demandées en fonction des coordonnées géographiques de chaque ville et sur une période spécifiée.

Une fois les données récupérées, nous les avons transformées en lignes JSON pour les préparer à l'indexation dans Elasticsearch. Chaque ligne JSON contient des informations détaillées sur les conditions météorologiques, telles que la température, la probabilité de précipitation, les précipitations et la couverture nuageuse, ainsi que des métadonnées telles que le nom de la ville et les coordonnées géographiques.

Nous avons ensuite enregistré les données transformées dans un fichier JSON pour faciliter l'indexation dans Elasticsearch. Cette étape était cruciale pour préparer les données à être visualisées et analysées dans Kibana.

Une fois les données indexées dans Elasticsearch, nous avons utilisé Kibana pour créer des visualisations et des tableaux de bord interactifs. Nous avons exploré différentes facettes des données météorologiques, en analysant les tendances de la température, les variations de précipitation et les modèles météorologiques sur différentes périodes et pour différentes villes.

## Choix des visualisations

Pour mener à bien notre projet, nous avons sélectionné plusieurs critères météorologiques qui sont intéréssants à observés sur différents graphiques. Nous avons également varié la période prise en compte, pour créer trois dashboards : 
- données du jour
- données des trois derniers jours
- données de la semaine passée

Voici le tableau récapitulatif des critères que nous avons sélectionnés :

<img width="301" alt="Capture d’écran 2024-05-02 à 16 43 20" src="https://github.com/laurakorenfeld/datavisualisation_Dinh_Korenfeld/assets/102244020/c4cf749c-6494-4029-9f8b-8778ff3372b6">

## Visualiser les données du jour en cours (19/04/2024)

<img width="771" alt="Capture d’écran 2024-05-02 à 16 48 27" src="https://github.com/laurakorenfeld/datavisualisation_Dinh_Korenfeld/assets/102244020/0efd302a-cb76-4ee4-8d16-c76ed06c23e3">

Parmi nos villes sélectionnées, Bordeaux est la ville qui a enregistré la température la plus élevée à 18,2°C, aujourd'hui (19/04/2004). Cette information met en évidence la température la plus chaude atteinte parmi un ensemble de villes surveillées durant cette période spécifique.
Cela permet d'avoir une vue directes du des températures extrêmes. 

<img width="903" alt="Capture d’écran 2024-05-02 à 17 01 10" src="https://github.com/laurakorenfeld/datavisualisation_Dinh_Korenfeld/assets/102244020/33bd9cb3-f297-4775-b7ff-4bdd5b8b889c">

Voici un graphique traçant la moyenne de nos données sur les villes sélectionnées au cours de la journée du 19/04/2024.
Cela nous donne un aperçu global de la valeur de ces données en France car les villes selectionnées, sont réparties dans tout le pays.
On observe une couverture nuageuse moyenne, elle tourne autour de 50% (entre 40% et 60%).
La probabilité de précipitation, quant à elle, est faible en début de journée  (mois de 10%  entre minuit de 13h). Cependant, elle augmente linéairement pour atteindre un pic à 30% à 19h et diminue de nouveau par la suite.
La température est remarquablement stable sur la journée, le minimum est atteint à 9h avec 7°C. Le maximum, 13°C est atteint à 19h.
Les trois données, que sont la couverture nuageuse, la probabilité de précipitation et la température atteindent toutes leur maximum à 19h.
Enfin, la précipitation, de l'ordre du millimètre a une valeur trop basse pour être observé sur ce graphique. Il y a donc eu très peu de pluie.

<img width="898" alt="Capture d’écran 2024-05-02 à 17 01 38" src="https://github.com/laurakorenfeld/datavisualisation_Dinh_Korenfeld/assets/102244020/0c2718b6-1308-4490-922d-e69b80da4793">

Dans ce graphique, nous observont les mêmes données que précédemment mais cette fois-ci pour une ville donnée, ici Lille.
La couverture nuageuse à été maximale toute la journée. Le ciel n'a commencé à se dégager qu'à 19h.
La probabilité de précipitation à évolué entre 0 et 90%, avec deux pics au maximum.
La température est resté constante, autour de 9°C toute la journée.
Enfin, quelques centimètres de pluie sont observables, notemment à 5h et autour de 17h.

### Voici le rendu du Dashboard complet pour le jour en cours : 

<img width="607" alt="Capture d’écran 2024-05-02 à 17 05 24" src="https://github.com/laurakorenfeld/datavisualisation_Dinh_Korenfeld/assets/102244020/03a5d3cd-72d0-4704-9837-1f1d32991842">


## Visualiser les données des trois derniers jours (du 17 au 19/04/2024)

<img width="592" alt="Capture d’écran 2024-05-02 à 17 04 04" src="https://github.com/laurakorenfeld/datavisualisation_Dinh_Korenfeld/assets/102244020/ced3820b-8483-4134-9955-ba46825074cb">

Ce diagramme à barres verticales expose les températures moyenne dans la journée pour chaque ville que nous avons sélectionné.
Sans grande surprise, Nice garde la température moyenne la plus haute sur ces trois jours. La tendance des températures moyennes reste globalement constante sur ces trois jours.

<img width="613" alt="Capture d’écran 2024-05-02 à 17 04 15" src="https://github.com/laurakorenfeld/datavisualisation_Dinh_Korenfeld/assets/102244020/7ac54ce3-3cea-430f-8b32-30a916781a6a">

Ici, nous affichons la précipitation cumulée des trois derniers jours grâce à une carte de chaleur. La couleur dégradée, du blanc au vert foncé rendre très facile la lecture de la hauteur de pluie qui est tombée.
Il y a eu plus de 12mm de pluie à Paris et Lyon tandis qu'à Toulouse, Tours ou Bordeaux, il n'a pas ou très peu plu.

### Voici le rendu du Dashboard complet pour les trois derniers jours : 

<img width="607" alt="Capture d’écran 2024-05-02 à 17 05 10" src="https://github.com/laurakorenfeld/datavisualisation_Dinh_Korenfeld/assets/102244020/5f34b41c-e6fc-4103-9cf3-20f59c32c15e">

## Visualiser les données de la semaine passée (du 13 au 20/04/2024)

<img width="493" alt="Capture d’écran 2024-05-02 à 17 10 34" src="https://github.com/laurakorenfeld/datavisualisation_Dinh_Korenfeld/assets/102244020/fae23f01-50c7-4da3-bc71-e9332d6e34a9">

Ce diagrammes à barres nous expose la température moyenne à Bordeaux pour chaque jour de la semaine passée. La température était élevée autour du 14/04, entre 28 et 30°C, elle est redescendue à 15°C  entre le 16 et le 19/04.

<img width="492" alt="Capture d’écran 2024-05-02 à 17 10 48" src="https://github.com/laurakorenfeld/datavisualisation_Dinh_Korenfeld/assets/102244020/8fd3ee01-91e9-4ab3-90d0-0c8e54e2b241">

Voici un graphique circulaire pour rendre compte de la répartition des précipitations durant la semaine.
La ville en présentant le plus est Lille avec près d'un tiers des précipitations parmi nos 10 villes sélectionnées. 5 villes sur 10 y figurent, les autres (Tours, Nice, Toulouse, Rennes, et Bordeaux) figurent dans les 9,75% restant.

<img width="493" alt="Capture d’écran 2024-05-02 à 17 11 00" src="https://github.com/laurakorenfeld/datavisualisation_Dinh_Korenfeld/assets/102244020/97dea77b-9886-4044-a85d-381447252f0a">

Nous avons sélectionné un graphique à barres horizontales pour représenter la probabilité de précipitation moyenne de la semaine.
Elle était la plus grande à Strasbourg avec 40% et la plus faible à Bordeaux à 6%.

<img width="489" alt="Capture d’écran 2024-05-02 à 17 11 13" src="https://github.com/laurakorenfeld/datavisualisation_Dinh_Korenfeld/assets/102244020/85ee80c7-08f4-41b1-9469-423bbffa8455">

Ces jauges de températures maximalent classent les températures des trois villes dans lesquelles il fait le plus chaud parmi les 10 sélectionnées.
On a classé les températures en 3 catégories : faible (entre 0 et 25), moyenne entre (25 et 30) et élevée (entre 29 et 60). Bordeaux a la plus grande température maximale avec 29,3°C.

<img width="492" alt="Capture d’écran 2024-05-02 à 17 11 26" src="https://github.com/laurakorenfeld/datavisualisation_Dinh_Korenfeld/assets/102244020/33ec025e-0649-4116-ac70-21138ab39f33">

Ce graphique représente l'évolution de la couverture nuageuse moyenne en pourcentage pour 5 villes. Nice présente globalement le moins de nuage et Strasbourg le plus.

<img width="492" alt="Capture d’écran 2024-05-02 à 17 11 34" src="https://github.com/laurakorenfeld/datavisualisation_Dinh_Korenfeld/assets/102244020/9a32cf9f-bf04-474f-935b-64ed61c5398a">

Pour un autre point de vue, nous avons également affiché la couverture nuageuse moyenne par ville (pour la période de la semaine passée).
Nice est encore une fois la ville avec la plus faible couverture nuageuse (seulement 20%) et s'oppose à Strasbourg qui a été très couverte (90%)


### Voici le rendu du Dashboard complet pour la semaine passée : 

<img width="621" alt="Capture d’écran 2024-05-04 à 16 03 41" src="https://github.com/laurakorenfeld/datavisualisation_Dinh_Korenfeld/assets/102244020/f06bd177-a6ec-4a1d-9eff-5ad2065c090c">

### Conclusion

Pour conclure, notre projet nous a permis de mettre en place avec succès un système de collecte et de visualisation de données météorologiques en utilisant la stack ELK. Nous avons suivi une approche structurée pour configurer les composants ELK, récupérer et transformer les données, et les visualiser dans Kibana. Ce rapport détaille notre méthodologie, nos résultats et notre analyse, démontrant notre capacité à tirer parti des fonctionnalités puissantes de la stack ELK pour répondre à nos besoins en matière de collecte et de représentation de données météorologiques.

Notre analyse des données météorologiques pourrait également être étendue pour comprendre l'influence des reliefs géographiques, des masses d'eau, et d'autres facteurs sur le climat local. Par exemple, nous pourrions examiner la répartition de la faune et de la flore en corrélation avec les données météorologiques pour mieux comprendre les écosystèmes locaux et leur sensibilité aux changements climatiques.
Ce projet ouvre donc la voie à des possibilités d'analyse plus approfondie et de prise de décision informée dans divers domaines, de l'urbanisme à la conservation de la nature, en passant par l'agriculture et le tourisme.
Il serait également intéressant d'obtenir les données précises de prévision pour pouvoir les comparer aux données effectives.
