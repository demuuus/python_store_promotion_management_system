# Python CRUD Application for Cashier Promotion Event Management System

A Python application for managing minimarket promotion data with Create, Read, Update, and Delete (CRUD) operations.

## Business Understanding

This project caters to the minimarket/retail industry, specifically addressing the need to manage promotion data efficiently. Promotions help minimarkets attract customers through different discount events such as percentage discounts, Buy 2 Get 1 (B2G1), and fixed discounts.

**Benefits:**

* Improved promotion data accuracy and consistency
* Streamlined promotion management processes
* Easier management of promotion periods and discount rules
* Support for cashier transactions using active promotions

**Target Users:**

This application is designed for minimarket owners and cashiers to manage promotions and apply available promotions during customer transactions.

## Features

* **Create:**
    * Add new promotion entries with details such as promotion name, promotion type, start date, end date, and discount.
    * Implement validation rules for promotion names, promotion types, dates, and discount values.
* **Read:**
    * View and search promotion records by promotion name, type, or discount.
    * View and search product records by product ID, name, or category.
* **Update:**
    * Modify existing promotion data such as name, type, dates, and discount.
    * Provide confirmation and error messages based on update success or failure.
* **Delete:**
    * Allow the removal of unwanted promotion records.
    * Provide confirmation before deleting promotion data.
* **Security:**
    * The application does not implement user authentication or authorization.
* **Reporting:**
    * The application displays promotion, product, and transaction information through the command-line interface.

## Installation

1. **Prerequisites:**
    * Python 3.x
    * No additional packages are required.

2. **Installation:**
    ```bash
    git clone https://github.com/demuuus/python_store_promotion_management_system.git
    cd python_store_promotion_management_system
    ```

3. **Database Setup (if applicable):**
    No database setup is required. The application uses Python lists and dictionaries to store data in memory.

## Usage

1. **Run the application:**
    ```bash
    python main.py
    ```

2. **CRUD Operations:**
    * **Create:** Add a new promotion by providing the promotion name, type, promotion period, and discount.
    * **Read:** View and search promotion or product information.
    * **Update:** Modify existing promotion details.
    * **Delete:** Remove a promotion record from the system.
    * **Transaction:** Process a customer purchase and apply an active promotion such as percentage, B2G1, or fixed discount.

## Data Model
This project utilizes Python lists and dictionaries to represent promotion and product data. The following fields are typically stored:

   * `id_promotion`: (Integer) - Unique identifier for a promotion.
   * `name_promotion`: (String) - Name of the promotion.
   * `type_promotion`: (String) - Type of promotion: percentage, B2G1, or fixed.
   * `start_date`: (Date) - Start date of the promotion.
   * `end_date`: (Date) - End date of the promotion.
   * `discount`: (Integer) - Discount value for the selected promotion type.
   * `id_product`: (Integer) - Unique identifier for a product.
   * `name_product`: (String) - Name of the product.
   * `price_product`: (Integer) - Product price.
   * `stock_product`: (Integer) - Available product stock.
   * `category_product`: (String) - Product category.

## Contributing
We welcome contributions to this project! Please feel free to open a pull request, sent to [demas.anggara04@gmail.com] or submit an issue if you encounter any problems or have suggestions for improvements.
