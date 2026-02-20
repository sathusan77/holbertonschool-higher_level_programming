# Task 03: Simple API using http.server

## Objectif

Créer une API simple en utilisant le module `http.server` de Python.

## Fichiers

- `task_03_http_server.py` : Serveur API simple
- `task_03_http_server_advanced.py` : Version avancée avec logging (bonus)
- `test_api.sh` : Script de test automatisé

## Endpoints

### `GET /`
Retourne un message de bienvenue.

**Réponse :**
```
Hello, this is a simple API!
```

### `GET /data`
Retourne des données JSON.

**Réponse :**
```json
{
  "name": "John",
  "age": 30,
  "city": "New York"
}
```

### `GET /status`
Vérifie le statut de l'API.

**Réponse :**
```
OK
```

### `GET /info`
Retourne des informations sur l'API.

**Réponse :**
```json
{
  "version": "1.0",
  "description": "A simple API built with http.server"
}
```

### Autres endpoints
Retourne une erreur 404.

**Réponse :**
```json
{
  "error": "Endpoint not found"
}
```

## Utilisation

### Démarrer le serveur
```bash
python3 task_03_http_server.py
```

### Tester les endpoints
```bash
# Test root
curl http://localhost:8000/

# Test data
curl http://localhost:8000/data

# Test status
curl http://localhost:8000/status

# Test info
curl http://localhost:8000/info

# Test 404
curl http://localhost:8000/unknown
```

### Script de test automatisé
```bash
./test_api.sh
```

## Arrêter le serveur

Appuyez sur `Ctrl+C` dans le terminal où le serveur est en cours d'exécution.

## Concepts clés

- **http.server.BaseHTTPRequestHandler** : Classe de base pour les handlers
- **do_GET()** : Méthode pour gérer les requêtes GET
- **send_response()** : Envoyer le code de statut HTTP
- **send_header()** : Ajouter un header
- **end_headers()** : Terminer les headers
- **wfile.write()** : Écrire la réponse

## Notes

- Ce serveur est pour le développement/apprentissage uniquement
- Ne pas utiliser en production
- Utiliser Flask ou FastAPI pour des applications réelles
```

**Sauvegardez**

---

## **✅ ÉTAPE 8 : Arrêter le serveur**

Dans le terminal où le serveur est en cours d'exécution :

**Appuyez sur `Ctrl+C`**

**Résultat :**
```
^C
Server stopped.
