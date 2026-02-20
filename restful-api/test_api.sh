#!/bin/bash

echo "==================================="
echo "   Test de l'API http.server"
echo "==================================="
echo ""

echo "1. Test Root endpoint (/) :"
curl -s http://localhost:8000/
echo -e "\n"

echo "2. Test /data endpoint :"
curl -s http://localhost:8000/data | jq '.'
echo ""

echo "3. Test /status endpoint :"
curl -s http://localhost:8000/status
echo -e "\n"

echo "4. Test /info endpoint :"
curl -s http://localhost:8000/info | jq '.'
echo ""

echo "5. Test 404 Not Found :"
curl -i http://localhost:8000/nonexistent 2>&1 | grep -E "HTTP|error"
echo ""

echo "==================================="
echo "   Tests terminés !"
echo "==================================="
