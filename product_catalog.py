import os
import json

# Filename where we will store our data
DATA_FILE = "catalog.json"

# LOAD products from JSON file
def load_products():
    """Load products from JSON file."""
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except:
        return {}
    
# SAVE products to JSON file
def save_products(catalog):
    """Save products to JSON file."""
    with open(DATA_FILE, 'w') as f:
        json.dump(catalog, f, indent=2)

def add_product(catalog):
    """Add products to JSON file"""
    product_name = input("\nEnter product name: ").strip()
    price = float(input("Enter product price: "))

    if product_name and price:
        catalog[product_name] = price
        
        save_products(catalog)

        print(f"\n✅ Product '{product_name}' added successfully.")
    else:
        print("\n❌ Error: Product name and Price cannot be empty!")



def run_product_catalog():

    print("\n========== PRODUCT CATALOG MANAGER ==========")

    catalog = load_products()

    while True:
        print("\nAvailable options:")
        print("  1. Add Product")

        user_choice = input("\nSelect an option: ").strip()

        if user_choice == "1":
            add_product(catalog)
            break
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    run_product_catalog()