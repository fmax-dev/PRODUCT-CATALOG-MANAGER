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
    search_query = normalize(input("\nEnter product name: "))

    if search_query in catalog:
        print(f"\n📦 {search_query.capitalize()}: ${catalog[search_query]}")
    else:
        print(f"\n❌ '{search_query.capitalize()}' not found.")
    

def view_product(catalog):
    """Allow users to view existing products"""
    if not catalog:
        print("\nProduct catalog is empty")
    else:
        print("\n--- ALL PRODUCTS ---\n")
        for index, (product_name, price) in enumerate(catalog.items(), start=1):
            print(f"    {index}. {product_name.capitalize()}: ${price}")


def delete_product(catalog):
    """Allow users to delete existing products"""

    delete_query = normalize(input("\nEnter product name: "))

    if delete_query in catalog:
        del catalog[delete_query]
        save_products(catalog)
        print(f"\n✅ '{delete_query.capitalize()}' deleted successfully!")
    else:
        print(f"\n❌ '{delete_query.capitalize()}' not found")


def run_product_catalog():

    print("\n========== PRODUCT CATALOG MANAGER ==========")

    catalog = load_products()

    while True:
        print("\nAvailable options:\n")
        print("  1. Add Product")
        print("  2. Search Product")
        print("  3. View Product")
        print("  4. Delete Product")
        print("  5. Exit")

        user_choice = input("\nSelect an option: ").strip()

        # ROUTING LOGIC
        if user_choice == "1":
            add_product(catalog)
        elif user_choice == "2":
            search_product(catalog)
        elif user_choice == "3":
            view_product(catalog)
        elif user_choice == "4":
            delete_product(catalog)
        elif user_choice == "5":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    run_product_catalog()