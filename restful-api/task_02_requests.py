#!/usr/bin/python3
"""
Module to fetch and process data from JSONPlaceholder API
"""


import requests
import csv


def fetch_and_print_posts():
    """
    Fetches all posts from JSONPlaceholder and prints their titles
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    
    try:
        response = requests.get(url)
        
        print("Status Code: {}".format(response.status_code))
        
        if response.status_code == 200:
            posts = response.json()
            
            for post in posts:
                print(post['title'])
        else:
            print("Failed to fetch posts. Status Code: {}".format(
                response.status_code))
    
    except requests.exceptions.RequestException as e:
        print("Error fetching data: {}".format(e))


def fetch_and_save_posts():
    """
    Fetches all posts from JSONPlaceholder and saves them to a CSV file
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            posts = response.json()
            
            # Structure data as list of dictionaries
            posts_data = []
            for post in posts:
                post_dict = {
                    'id': post['id'],
                    'title': post['title'],
                    'body': post['body']
                }
                posts_data.append(post_dict)
            
            # Write to CSV file
            with open('posts.csv', 'w', newline='', encoding='utf-8') as f:
                fieldnames = ['id', 'title', 'body']
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                
                writer.writeheader()
                writer.writerows(posts_data)
            
            print("Posts saved to posts.csv")
        else:
            print("Failed to fetch posts. Status Code: {}".format(
                response.status_code))
    
    except requests.exceptions.RequestException as e:
        print("Error fetching data: {}".format(e))
