# Product Catalog Manager

A simple CLI-based program to manage your product catalog. Products are stored locally in a JSON file — no database or internet connection required.

## Table of Contents
- [Features Overview](#features-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Next Steps](#next-steps)

## Features Overview

| # | Feature | Description |
|---|---------|-------------|
| 1 | Add Product | Add a new product with a name and price. Duplicate names are rejected. |
| 2 | Search Product | Look up a product by name and display its price. |
| 3 | View Products | List all products in the catalog with their prices. |
| 4 | Delete Product | Remove a product from the catalog by name. |
| 5 | Exit | Quit the program. |

## Installation
To install this program, use the commands below:
```bash
git clone https://github.com/fmax-dev/PRODUCT-CATALOG-MANAGER.git
cd PRODUCT-CATALOG-MANAGER
```
No external dependencies are required — the program uses only Python's standard library (`os` and `json`).

## Usage
To start using this program:
1. Clone this repo using the commands above
2. Run the program:
    - Windows: `python product_catalog.py`
    - Mac/Linux: `python3 product_catalog.py`
3. Select an option from the menu and follow the prompts

```
========== PRODUCT CATALOG MANAGER ==========

Available options:

  1. Add Product
  2. Search Product
  3. View Product
  4. Delete Product
  5. Exit
```

## Next Steps
- Add product update/edit functionality
- Add price validation to reject negative or zero values
- Add support for product categories