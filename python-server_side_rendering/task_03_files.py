#!/usr/bin/python3
"""Flask application with JSON and CSV data sources."""
import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json(product_id=None):
    """Read products from JSON file."""
    try:
        with open('products.json', 'r') as f:
            products = json.load(f)
        if product_id:
            products = [p for p in products if p['id'] == product_id]
        return products
    except Exception:
        return []


def read_csv(product_id=None):
    """Read products from CSV file."""
    try:
        products = []
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['price'] = float(row['price'])
                row['id'] = int(row['id'])
                products.append(row)
        if product_id:
            products = [p for p in products if p['id'] == product_id]
        return products
    except Exception:
        return []


@app.route('/products')
def products():
    """Render products page with data from the specified source."""
    source = request.args.get('source')
    product_id = request.args.get('id')
    error = None
    data = []

    if product_id:
        product_id = int(product_id)

    if source == 'json':
        data = read_json(product_id)
    elif source == 'csv':
        data = read_csv(product_id)
    else:
        error = 'Wrong source'

    if not error and product_id and not data:
        error = 'Product not found'

    return render_template('product_display.html', products=data, error=error)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
