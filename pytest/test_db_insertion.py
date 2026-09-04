# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Fixture
#  Author       : Team Tinitiate
# ==============================================================================



import json
import psycopg2
import pytest
# Assuming you have this function available
from db_insertion import add_product_to_database

# Update the connection details for the test database
TEST_DB_CONNECTION = {
    "host": "localhost",
    "port": 5432,
    "dbname": "tinitiate",
    "user": "tinitiate",
    "password": "tinitiate"
}

@pytest.fixture(scope="module")
def test_db_connection():
    # Create connection to test database and create necessary schema and tables
    conn = psycopg2.connect(**TEST_DB_CONNECTION)
    yield conn
    conn.close()

@pytest.fixture(scope="function", autouse=True)
def setup_and_teardown(test_db_connection):
    # Create schema and tables before each test and clean up after each test
    cursor = test_db_connection.cursor()
    cursor.execute("CREATE SCHEMA IF NOT EXISTS shoppingcart;")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS shoppingcart.products (
            product_id SERIAL PRIMARY KEY,
            product_category TEXT,
            product_name TEXT,
            unit_price NUMERIC
        );
    """)
    test_db_connection.commit()
    yield
    cursor.execute("DROP SCHEMA IF EXISTS shoppingcart CASCADE;")
    test_db_connection.commit()

def test_add_product_success():
    data = {
        "id": 124,
        "category": "Electronics",
        "name": "Smartphone",
        "price": 599.99
    }
    
    response = add_product_to_database(data)
    
    assert response["statusCode"] == 200
    assert "Product added successfully" in json.loads(response["body"])["message"]

def test_add_product_failure():
    data = {
        "id": 124,
        "category": "Electronics",
        "name": "Smartphone",
        "price": 599.99
    }
    
    response = add_product_to_database(data)
    
    assert response["statusCode"] == 500
    assert "Failed to add product" in json.loads(response["body"])["message"]
