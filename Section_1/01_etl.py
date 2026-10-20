# Program 1: ETL (Extract, Transform, and Load)

# Source data
sales = ["1200", "1500", "1800", "2100", "2500"]

# Extract
extracted_sales = sales.copy()
print("Type before transformation:", type(extracted_sales[0]).__name__)

# Transform strings into integers
transformed_sales = [int(value) for value in extracted_sales]

# Load into a target list
sales_warehouse = []
sales_warehouse.extend(transformed_sales)

print("Extracted data  :", extracted_sales)
print("Transformed data:", transformed_sales)
print("Loaded data     :", sales_warehouse)
print("Type after transformation:", type(transformed_sales[0]).__name__)