#!/usr/bin/env python3
"""
Démonstration avancée de l'utilisation de requests
"""


import requests
import json


def demo_get():
    """Démo GET simple"""
    print("=== DEMO GET ===")
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    print("Status Code:", response.status_code)
    print("JSON Response:")
    print(json.dumps(response.json(), indent=2))
    print()


def demo_post():
    """Démo POST"""
    print("=== DEMO POST ===")
    data = {
        "title": "Mon nouveau post",
        "body": "Ceci est le contenu",
        "userId": 1
    }
    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=data
    )
    print("Status Code:", response.status_code)
    print("Created Post:")
    print(json.dumps(response.json(), indent=2))
    print()


def demo_put():
    """Démo PUT"""
    print("=== DEMO PUT ===")
    data = {
        "id": 1,
        "title": "Titre modifié",
        "body": "Corps modifié",
        "userId": 1
    }
    response = requests.put(
        "https://jsonplaceholder.typicode.com/posts/1",
        json=data
    )
    print("Status Code:", response.status_code)
    print("Updated Post:")
    print(json.dumps(response.json(), indent=2))
    print()


def demo_delete():
    """Démo DELETE"""
    print("=== DEMO DELETE ===")
    response = requests.delete(
        "https://jsonplaceholder.typicode.com/posts/1"
    )
    print("Status Code:", response.status_code)
    print("Response:", response.json())
    print()


def demo_headers():
    """Démo récupération des headers"""
    print("=== DEMO HEADERS ===")
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Headers:")
    for key, value in response.headers.items():
        print(f"{key}: {value}")
    print()


if __name__ == "__main__":
    demo_get()
    demo_post()
    demo_put()
    demo_delete()
    demo_headers()
