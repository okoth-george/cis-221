from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_inventory():
    conn = sqlite3.connect('fashion.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, price, bought, sold FROM products")
    rows = cursor.fetchall()
    products = []
    total_revenue = 0
    for name, price, bought, sold in rows:
        in_stock = bought - sold
        revenue = price * sold
        total_revenue += revenue
        products.append({
            'name': name,
            'price': price,
            'bought': bought,
            'sold': sold,
            'in_stock': in_stock,
            'revenue': revenue
        })
    conn.close()
    return products, total_revenue

@app.route('/')
def home():
    products, total_revenue = get_inventory()
    return render_template('fashion_store.html', products=products, total_revenue=total_revenue)

if __name__ == '__main__':
    app.run(debug=True)
