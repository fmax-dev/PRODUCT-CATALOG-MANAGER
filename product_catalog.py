import os
import json

# Filename where we will store our data
DATA_FILE = "catalog.json"

def normalize(value):
    """Normalize a string to lowercase and strip whitespace for consistent storage and lookup."""
    return value.lower().strip()


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
    product_name = normalize(input("\nEnter product name: "))
    price = float(input("Enter product price: "))

    # DUPLICATE PRODUCT VALIDATION
    if product_name in catalog:
        print(f"\n❌ '{product_name.capitalize()}' already exists! Please enter another product")
        return

    if product_name and price:
        catalog[product_name] = price
        
        save_products(catalog)

        print(f"\n✅ Product '{product_name.capitalize()}' added successfully.")
    else:
        print("\n❌ Error: Product name and Price cannot be empty!")


def search_product(catalog):
    """Allow users to search products"""
    query = normalize(input("\nEnter product name: "))

    if query in catalog:
        print(f"\n📦 {query.capitalize()}: ${catalog[query]}")
    else:
        print(f"\n❌ '{query.capitalize()}' not found.")
    

def view_product(catalog):
    """Allow users to view existing products"""
    if not catalog:
        print("\nProduct catalog is empty")
    else:
        print("\n--- ALL PRODUCTS ---\n")
        for index, (product_name, price) in enumerate(catalog.items(), start=1):
            print(f"    {index}. {product_name.capitalize()}: ${price}")


def run_product_catalog():

    print("\n========== PRODUCT CATALOG MANAGER ==========")

    catalog = load_products()

    while True:
        print("\nAvailable options:\n")
        print("  1. Add Product")
        print("  2. Search Product")
        print("  3. View Product")

        user_choice = input("\nSelect an option: ").strip()

        if user_choice == "1":
            add_product(catalog)
        elif user_choice == "2":
            search_product(catalog)
        elif user_choice == "3":
            view_product(catalog)
            break
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    run_product_catalog()