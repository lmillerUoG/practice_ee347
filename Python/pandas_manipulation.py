import pandas as pd

# Step 2: Load the data from CSV
df = pd.read_csv('sales_data.csv')

# Step 3: Calculate Revenue and add it as a new column
df['Revenue'] = df['Quantity'] * df['Price']

# Step 4: Filter data for North region
north_region_df = df[df['Region'] == 'North']

# Step 5: Group by Product and calculate the total quantity sold for each product in the North region
total_quantity_north = north_region_df.groupby('Product')['Quantity'].sum().reset_index()

# Print the total quantity sold for each product in the North region
print("Total quantity sold for each product in the North region:")
print(total_quantity_north)

# Step 6: Calculate total revenue for each product and find the product with the highest total revenue
total_revenue_by_product = df.groupby('Product')['Revenue'].sum()
max_revenue_product = total_revenue_by_product.idxmax()
max_revenue_amount = total_revenue_by_product.max()

# Print the product with the highest total revenue
print(f"\nThe product with the highest total revenue is {max_revenue_product} with revenue of {max_revenue_amount}.")

# Step 7: Save the North region data to a new CSV file
north_region_df.to_csv('north_sales.csv', index=False)
