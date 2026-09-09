# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Expected Failure
#  Author       : Team Tinitiate
# ==============================================================================



import pytest
from products import ProductManager

@pytest.fixture
def product_manager():
    return ProductManager()

def test_add_product(product_manager):
    product_data = {
        "product_id": "P123",
        "product_category": "Electronics",
        "product_name": "Smartphone",
        "unit_price": 599.99
    }
    product_manager.add_product(product_data)
    product = product_manager.get_product("P123")   # <-- use P123 consistently
    assert product[0] == "P123"
    assert product[1] == "Electronics"
    assert product[2] == "Smartphone"
    assert product[3] == 599.99

def test_update_product(product_manager):
    # Add first
    product_manager.add_product({
        "product_id": "P123",
        "product_category": "Electronics",
        "product_name": "Smartphone",
        "unit_price": 599.99
    })
    # Then update
    updated_data = {
        "product_category": "Gadgets",
        "product_name": "Updated Smartphone",
        "unit_price": 699.99
    }
    product_manager.update_product("P123", updated_data)
    product = product_manager.get_product("P123")
    assert product[1] == "Gadgets"
    assert product[2] == "Updated Smartphone"
    assert product[3] == 699.99

def test_delete_product(product_manager):
    # Add first
    product_manager.add_product({
        "product_id": "P123",
        "product_category": "Electronics",
        "product_name": "Smartphone",
        "unit_price": 599.99
    })
    product_manager.delete_product("P123")
    product = product_manager.get_product("P123")
    assert product is None

@pytest.mark.xfail(reason="Intentional failure")
def test_get_product(product_manager):
    product = product_manager.get_product("P123")
    assert product is None

# Run pytest
if __name__ == "__main__":
    pytest.main()
