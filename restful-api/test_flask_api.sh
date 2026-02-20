#!/bin/bash

echo "==========================================="
echo "   Test Flask API - task_04_flask.py"
echo "==========================================="
echo ""

echo "1. Test Root endpoint (/) :"
curl -s http://localhost:5000/
echo -e "\n"

echo "2. Test /status endpoint :"
curl -s http://localhost:5000/status
echo -e "\n"

echo "3. Test /data endpoint (before adding users) :"
curl -s http://localhost:5000/data | jq '.'
echo ""

echo "4. Add user Jane :"
curl -s -X POST http://localhost:5000/add_user \
  -H "Content-Type: application/json" \
  -d '{"username":"jane","name":"Jane","age":28,"city":"Los Angeles"}' | jq '.'
echo ""

echo "5. Add user John :"
curl -s -X POST http://localhost:5000/add_user \
  -H "Content-Type: application/json" \
  -d '{"username":"john","name":"John","age":30,"city":"New York"}' | jq '.'
echo ""

echo "6. Test /data endpoint (after adding users) :"
curl -s http://localhost:5000/data | jq '.'
echo ""

echo "7. Get user Jane :"
curl -s http://localhost:5000/users/jane | jq '.'
echo ""

echo "8. Get user John :"
curl -s http://localhost:5000/users/john | jq '.'
echo ""

echo "9. Get non-existent user (404) :"
curl -s http://localhost:5000/users/unknown | jq '.'
echo ""

echo "10. Add user without username (400) :"
curl -s -X POST http://localhost:5000/add_user \
  -H "Content-Type: application/json" \
  -d '{"name":"Alice","age":25}' | jq '.'
echo ""

echo "11. Add duplicate user (409) :"
curl -s -X POST http://localhost:5000/add_user \
  -H "Content-Type: application/json" \
  -d '{"username":"jane","name":"Jane Doe","age":29}' | jq '.'
echo ""

echo "12. Add user with invalid JSON (400) :"
curl -s -X POST http://localhost:5000/add_user \
  -H "Content-Type: application/json" \
  -d 'invalid' | jq '.'
echo ""

echo "==========================================="
echo "   Tests terminés !"
echo "==========================================="
