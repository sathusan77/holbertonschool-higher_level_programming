# Task 04: Flask API for User Management

## Objectif

Créer une API RESTful avec Flask pour gérer des utilisateurs.

## Installation
```bash
pip install Flask --break-system-packages
```

## Fichiers

- `task_04_flask.py` : Application Flask principale
- `test_flask_api.sh` : Script de test Bash
- `test_flask_api.py` : Script de test Python

## Endpoints

### `GET /`
Message de bienvenue.

**Réponse :**
```
Welcome to the Flask API!
```

### `GET /status`
Vérifie le statut de l'API.

**Réponse :**
```
OK
```

### `GET /data`
Retourne la liste de tous les usernames.

**Réponse :**
```json
["jane", "john"]
```

### `GET /users/<username>`
Retourne les informations d'un utilisateur.

**Réponse (succès) :**
```json
{
  "username": "jane",
  "name": "Jane",
  "age": 28,
  "city": "Los Angeles"
}
```

**Réponse (404) :**
```json
{
  "error": "User not found"
}
```

### `POST /add_user`
Ajoute un nouvel utilisateur.

**Body :**
```json
{
  "username": "alice",
  "name": "Alice",
  "age": 25,
  "city": "San Francisco"
}
```

**Réponse (201) :**
```json
{
  "message": "User added",
  "user": {
    "username": "alice",
    "name": "Alice",
    "age": 25,
    "city": "San Francisco"
  }
}
```

**Erreurs :**
- `400` : Username manquant ou JSON invalide
- `409` : Username déjà existant

## Utilisation

### Démarrer le serveur
```bash
flask --app task_04_flask run
```

ou
```bash
python3 task_04_flask.py
```

### Tester avec curl
```bash
# Root
curl http://localhost:5000/

# Status
curl http://localhost:5000/status

# Ajouter un utilisateur
curl -X POST http://localhost:5000/add_user \
  -H "Content-Type: application/json" \
  -d '{"username":"jane","name":"Jane","age":28,"city":"Los Angeles"}'

# Liste des usernames
curl http://localhost:5000/data

# Récupérer un utilisateur
curl http://localhost:5000/users/jane
```

### Script de test
```bash
./test_flask_api.sh
# ou
python3 test_flask_api.py
```

## Codes de statut

- `200 OK` : Succès
- `201 Created` : Utilisateur créé
- `400 Bad Request` : Requête invalide
- `404 Not Found` : Ressource non trouvée
- `409 Conflict` : Conflit (username existe déjà)

## Notes

- Les données sont stockées en mémoire (volatiles)
- Redémarrer le serveur efface les données
- Pour une application réelle, utiliser une base de données
