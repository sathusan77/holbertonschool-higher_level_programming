from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# ---------------- JSON ----------------
def read_json():
    try:
        with open('products.json', 'r') as f:
            return json.load(f)
    except Exception:
        return None

# ---------------- CSV ----------------
def read_csv():
    try:
        products = []
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row["id"] = int(row["id"])
                row["price"] = float(row["price"])
                products.append(row)
        return products
    except Exception:
        return None

# ---------------- SQL (SQLite) ----------------
def read_sql():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()

        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()

        conn.close()

        products = []
        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            })

        return products

    except sqlite3.Error:
        return None

# ---------------- ROUTE ----------------
@app.route('/products')
def products():
    source = request.args.get('source')

    if source == "json":
        data = read_json()

    elif source == "csv":
        data = read_csv()

    elif source == "sql":
        data = read_sql()

    else:
        return render_template('product_display.html', error="Wrong source")

    if data is None:
        return render_template('product_display.html', error="Error loading data")

    return render_template('product_display.html', products=data)

# ---------------- RUN ----------------
if __name__ == '__main__':
    app.run(debug=True, port=5000)
