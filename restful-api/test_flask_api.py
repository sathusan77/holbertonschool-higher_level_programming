#!/usr/bin/env python3
"""
Test script for Flask API
"""


import requests
import json


BASE_URL = "http://localhost:5000"


def test_root():
    """Test root endpoint"""
    print("1. Testing root endpoint...")
    response = requests.get(f"{BASE_URL}/")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}\n")


def test_status():
    """Test status endpoint"""
    print("2. Testing /status endpoint...")
    response = requests.get(f"{BASE_URL}/status")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}\n")


def test_add_user(username, name, age, city):
    """Add a user"""
    print(f"Adding user {username}...")
    data = {
        "username": username,
        "name": name,
        "age": age,
        "city": city
    }
    response = requests.post(
        f"{BASE_URL}/add_user",
        json=data
    )
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}\n")


def test_get_data():
    """Get all usernames"""
    print("Getting all usernames...")
    response = requests.get(f"{BASE_URL}/data")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}\n")


def test_get_user(username):
    """Get a specific user"""
    print(f"Getting user {username}...")
    response = requests.get(f"{BASE_URL}/users/{username}")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}\n")


def test_errors():
    """Test error cases"""
    print("3. Testing error cases...")
    
    # Missing username
    print("- Adding user without username:")
    response = requests.post(
        f"{BASE_URL}/add_user",
        json={"name": "Alice", "age": 25}
    )
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}\n")
    
    # Duplicate username
    print("- Adding duplicate username:")
    response = requests.post(
        f"{BASE_URL}/add_user",
        json={"username": "jane", "name": "Jane Doe"}
    )
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}\n")
    
    # User not found
    print("- Getting non-existent user:")
    response = requests.get(f"{BASE_URL}/users/unknown")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}\n")


if __name__ == "__main__":
    print("="*50)
    print("   Flask API Test Suite")
    print("="*50)
    print()
    
    test_root()
    test_status()
    test_add_user("jane", "Jane", 28, "Los Angeles")
    test_add_user("john", "John", 30, "New York")
    test_get_data()
    test_get_user("jane")
    test_get_user("john")
    test_errors()
    
    print("="*50)
    print("   Tests completed!")
    print("="*50)01~#!/usr/bin/env python3
"""
Test script for Flask API
"""


import requests
import json


BASE_URL = "http://localhost:5000"


def test_root():
    """Test root endpoint"""
    print("1. Testing root endpoint...")
    response = requests.get(f"{BASE_URL}/")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}\n")


def test_status():
    """Test status endpoint"""
    print("2. Testing /status endpoint...")
    response = requests.get(f"{BASE_URL}/status")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}\n")


def test_add_user(username, name, age, city):
    """Add a user"""
    print(f"Adding user {username}...")
    data = {
        "username": username,
        "name": name,
        "age": age,
        "city": city
    }
    response = requests.post(
        f"{BASE_URL}/add_user",
        json=data
    )
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}\n")


def test_get_data():
    """Get all usernames"""
    print("Getting all usernames...")
    response = requests.get(f"{BASE_URL}/data")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}\n")


def test_get_user(username):
    """Get a specific user"""
    print(f"Getting user {username}...")
    response = requests.get(f"{BASE_URL}/users/{username}")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}\n")


def test_errors():
    """Test error cases"""
    print("3. Testing error cases...")
    
    # Missing username
    print("- Adding user without username:")
    response = requests.post(
        f"{BASE_URL}/add_user",
        json={"name": "Alice", "age": 25}
    )
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}\n")
    
    # Duplicate username
    print("- Adding duplicate username:")
    response = requests.post(
        f"{BASE_URL}/add_user",
        json={"username": "jane", "name": "Jane Doe"}
    )
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}\n")
    
    # User not found
    print("- Getting non-existent user:")
    response = requests.get(f"{BASE_URL}/users/unknown")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}\n")


if __name__ == "__main__":
    print("="*50)
    print("   Flask API Test Suite")
    print("="*50)
    print()
    
    test_root()
    test_status()
    test_add_user("jane", "Jane", 28, "Los Angeles")
    test_add_user("john", "John", 30, "New York")
    test_get_data()
    test_get_user("jane")
    test_get_user("john")
    test_errors()
    
    print("="*50)
    print("   Tests completed!")
    print("="*50)
