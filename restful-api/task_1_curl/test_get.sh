#!/bin/bash

echo "=== TEST GET - Récupérer tous les posts ==="
curl -s https://jsonplaceholder.typicode.com/posts | jq '. | length'
echo ""

echo "=== TEST GET - Récupérer le post 1 ==="
curl -s https://jsonplaceholder.typicode.com/posts/1 | jq '.'
echo ""

echo "=== TEST GET - Headers uniquement ==="
curl -I https://jsonplaceholder.typicode.com/posts
