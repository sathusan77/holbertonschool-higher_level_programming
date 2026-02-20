# Task 02: Consuming and Processing Data from API using Python

## Objectif

Utiliser la bibliothèque `requests` de Python pour consommer des données d'une API REST et les traiter.

## Installation
```bash
pip install requests --break-system-packages
```

## Fichiers

- `task_02_requests.py` : Module principal avec les fonctions
- `main_02_requests.py` : Script de test
- `posts.csv` : Fichier CSV généré
- `demo_requests.py` : Démonstration avancée (bonus)

## Fonctions

### `fetch_and_print_posts()`

Récupère tous les posts depuis JSONPlaceholder et affiche leurs titres.

**Comportement :**
1. Affiche le status code de la réponse
2. Si succès (200), parse le JSON
3. Affiche le titre de chaque post

### `fetch_and_save_posts()`

Récupère tous les posts et les sauvegarde dans un fichier CSV.

**Comportement :**
1. Récupère les posts
2. Structure les données (id, title, body)
3. Crée un fichier `posts.csv`

## Utilisation
```bash
# Exécuter le script principal
python3 main_02_requests.py

# Vérifier le CSV créé
cat posts.csv | head -5

# Démo avancée (bonus)
python3 demo_requests.py
```

## Exemple de sortie
```
Status Code: 200
sunt aut facere repellat provident occaecati excepturi optio reprehenderit
qui est esse
ea molestias quasi exercitationem repellat qui ipsa sit aut
...
Posts saved to posts.csv
```

## Concepts clés

- **requests.get()** : Effectue une requête GET
- **response.status_code** : Code de statut HTTP
- **response.json()** : Parse la réponse JSON
- **csv.DictWriter** : Écrire des dictionnaires dans un CSV

## Codes de statut HTTP

- `200 OK` : Succès
- `404 Not Found` : Ressource inexistante
- `500 Internal Server Error` : Erreur serveur
