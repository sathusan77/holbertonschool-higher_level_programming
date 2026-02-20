#!/bin/bash

echo "=== TEST POST - Créer un nouveau post ==="
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"title":"Mon nouveau post","body":"Contenu du post","userId":1}' \
  https://jsonplaceholder.typicode.com/posts | jq '.'
