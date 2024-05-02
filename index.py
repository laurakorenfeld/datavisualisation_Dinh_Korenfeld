import json
import requests
import datetime

# Informations sur les villes
villes = {
    "Bordeaux": {"latitude": 44.8404, "longitude": -0.5805},
    "Lille": {"latitude": 50.633, "longitude": 3.0586},
    "Lyon": {"latitude": 45.7485, "longitude": 4.8467},
    "Nice": {"latitude": 43.7031, "longitude": 7.2661},
    "Paris": {"latitude": 48.8534, "longitude": 2.3488},
    "Rennes": {"latitude": 48.112, "longitude": -1.6743},
    "Rouen": {"latitude": 49.4431, "longitude": 1.0993},
    "Strasbourg": {"latitude": 48.5839, "longitude": 7.7455},
    "Toulouse": {"latitude": 43.6043, "longitude": 1.4437},
    "Tours": {"latitude": 47.3948, "longitude": 0.704}
}

def obtenir_donnees_meteo(nom_ville, date_debut, date_fin):
    # Récupérer les coordonnées géographiques de la ville
    latitude = villes[nom_ville]["latitude"]
    longitude = villes[nom_ville]["longitude"]

    # Construire l'URL de l'API météo
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,precipitation_probability,precipitation,cloud_cover&timezone=Europe%2FBerlin&start_date={date_debut}&end_date={date_fin}"

    # Envoyer une requête GET à l'API
    reponse = requests.get(url)

    # Vérifier si la requête a réussi
    if reponse.status_code == 200:
        # Ajouter le nom de la ville aux données JSON
        donnees = reponse.json()
        donnees['ville'] = nom_ville
        return donnees
    else:
        # Retourner une erreur si la requête a échoué
        return f"Erreur : Impossible de récupérer les données, code d'état {reponse.status_code}"

# Fonction pour transformer les données JSON en lignes JSON
def transformer_json_en_lignes_json(donnees_json):
    donnees_horaires = donnees_json["hourly"]
    nom_ville = donnees_json["ville"]
    latitude = villes[nom_ville]["latitude"]
    longitude = villes[nom_ville]["longitude"]
    lignes_json = []

    for i in range(len(donnees_horaires["time"])):
        ligne = {
            "ville": nom_ville,
            "localisation": {"lat": latitude, "lon": longitude},
            "heure": donnees_horaires["time"][i],
            "temperature": donnees_horaires["temperature_2m"][i],
            "probabilite_precipitation": donnees_horaires["precipitation_probability"][i],
            "precipitation": donnees_horaires["precipitation"][i],
            "nuage": donnees_horaires["cloud_cover"][i]
        }
        lignes_json.append(json.dumps(ligne))

    return lignes_json

# Paramètres de date pour la requête
date_debut = datetime.date.today() - datetime.timedelta(days=6) # 6 jours = une semaine
date_fin = datetime.date.today()

# Liste pour stocker toutes les lignes JSON de toutes les villes
toutes_les_lignes_json = []

# Itérer sur chaque ville et récupérer les données météorologiques
for nom_ville in villes:
    donnees_meteo = obtenir_donnees_meteo(nom_ville, date_debut, date_fin)
    lignes_json_transformees = transformer_json_en_lignes_json(donnees_meteo)
    toutes_les_lignes_json.extend(lignes_json_transformees)

# Enregistrer les données transformées dans un fichier
with open("C:/Users/hien2/Downloads/github/datavisualisation_Dinh_Korenfeld/elk-demo/data/data_meteo.json", 'w') as fichier:
    for ligne in toutes_les_lignes_json:
        fichier.write(ligne + "\n")

# Confirmer l'enregistrement des données
print("Données enregistrées dans data_meteo.json")