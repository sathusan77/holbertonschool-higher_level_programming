#!/bin/bash

echo "==================================="
echo "   TESTS CURL - JSONPlaceholder"
echo "==================================="
echo ""

echo "1. GET - Récupérer le post 1"
curl -s https://jsonplaceholder.typicode.com/posts/1 | jq '.title'
echo ""

echo "2. POST - Créer un post"
curl -s -X POST \
  -H "Content-Type: application/json" \
  -d '{"title":"Test Post","body":"Test Body","userId":1}' \
  https://jsonplaceholder.typicode.com/posts | jq '.id'
echo ""

echo "3. PUT - Remplacer le post 1"
curl -s -X PUT \
  -H "Content-Type: application/json" \
  -d '{"id":1,"title":"Updated","body":"Updated body","userId":1}' \
  https://jsonplaceholder.typicode.com/posts/1 | jq '.title'
echo ""

echo "4. PATCH - Modifier partiellement le post 1"
curl -s -X PATCH \
  -H "Content-Type: application/json" \
  -d '{"title":"Patched"}' \
  https://jsonplaceholder.typicode.com/posts/1 | jq '.title'
echo ""

echo "5. DELETE - Supprimer le post 1"
curl -s -X DELETE https://jsonplaceholder.typicode.com/posts/1
echo "{} (vide = succès)"
echo ""

echo "==================================="
echo "   Tests terminés !"
echo "==================================="
