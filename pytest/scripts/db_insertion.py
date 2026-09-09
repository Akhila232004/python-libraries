# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : DB Insertion
#  Author       : Team Tinitiate
# ==============================================================================



import json
import psycopg2

def add_product_to_database(data):
    try:
        conn = psycopg2.connect(
            host="localhost", dbname="tinitiate", user="tinitiate", password="tinitiate", port=5432
        )
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO shoppingcart.products (product_id, product_category, product_name, unit_price)
            VALUES (%s, %s, %s, %s);
        """, (data["id"], data["category"], data["name"], data["price"]))
        conn.commit()
        cur.close()
        conn.close()
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Product added successfully"})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"message": f"Failed to add product: {e}"})
        }
