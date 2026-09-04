# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Products
#  Author       : Team Tinitiate
# ==============================================================================



class ProductManager:
    def __init__(self):
        # Internal dictionary to store products
        # Key: product_id (string), Value: (product_id, category, name, unit_price)
        self._products = {}

    def add_product(self, product_data):
        """Add a new product to the store."""
        pid = str(product_data["product_id"])
        category = product_data["product_category"]
        name = product_data["product_name"]
        price = product_data["unit_price"]

        self._products[pid] = (pid, category, name, price)

    def update_product(self, product_id, updated_data):
        """Update an existing product by ID."""
        pid = str(product_id)
        if pid not in self._products:
            return None

        _, _, _, old_price = self._products[pid]

        category = updated_data.get("product_category", self._products[pid][1])
        name = updated_data.get("product_name", self._products[pid][2])
        price = updated_data.get("unit_price", old_price)

        self._products[pid] = (pid, category, name, price)
        return self._products[pid]

    def delete_product(self, product_id):
        """Delete a product by ID."""
        pid = str(product_id)
        if pid in self._products:
            del self._products[pid]

    def get_product(self, product_id):
        """Retrieve a product by ID. Returns a tuple or None."""
        pid = str(product_id)
        return self._products.get(pid)
