# ==========================================
# INVENTORY, SALES & VENDOR ANALYSIS PROJECT
# ==========================================

import pandas as pd
import numpy as np

# ------------------------------------------
# 1. LOAD DATA FILES
# ------------------------------------------
begin_inventory = pd.read_csv("begin_inventory.csv")
end_inventory = pd.read_csv("end_inventory.csv")
purchases = pd.read_csv("purchases.csv")
sales_file = "sales.csv"

print("All files loaded successfully")

# ------------------------------------------
# 2. INVENTORY MOVEMENT ANALYSIS
# ------------------------------------------
print("\n--- INVENTORY MOVEMENT ANALYSIS ---")

begin_summary = (
    begin_inventory
    .groupby("InventoryId")["onHand"]
    .sum()
    .reset_index()
    .rename(columns={"onHand": "Begin_Quantity"})
)

end_summary = (
    end_inventory
    .groupby("InventoryId")["onHand"]
    .sum()
    .reset_index()
    .rename(columns={"onHand": "End_Quantity"})
)

inventory_movement = begin_summary.merge(
    end_summary,
    on="InventoryId",
    how="outer"
)

inventory_movement.fillna(0, inplace=True)

inventory_movement["Stock_Change"] = (
    inventory_movement["End_Quantity"]
    - inventory_movement["Begin_Quantity"]
)

def stock_status(x):
    if x > 0:
        return "Increased"
    elif x < 0:
        return "Decreased"
    else:
        return "No Change"

inventory_movement["Stock_Status"] = inventory_movement["Stock_Change"].apply(stock_status)

inventory_movement.to_csv("inventory_movement_summary.csv", index=False)
print("inventory_movement_summary.csv saved")

# ------------------------------------------
# 3. VENDOR PURCHASE ANALYSIS
# ------------------------------------------
print("\n--- VENDOR PURCHASE ANALYSIS ---")

vendor_purchase_summary = (
    purchases
    .groupby("VendorName")["Dollars"]
    .sum()
    .reset_index()
    .sort_values(by="Dollars", ascending=False)
)

vendor_purchase_summary.to_csv(
    "vendor_purchase_summary.csv",
    index=False
)
print("vendor_purchase_summary.csv saved")

# ------------------------------------------
# 4. VENDOR PRICE COMPARISON
# ------------------------------------------
vendor_price = (
    purchases
    .groupby("VendorName")["PurchasePrice"]
    .mean()
    .reset_index()
    .sort_values(by="PurchasePrice", ascending=False)
)

vendor_price.to_csv(
    "vendor_price_comparison.csv",
    index=False
)
print("vendor_price_comparison.csv saved")

# ------------------------------------------
# 5. BRAND + VENDOR PRICE COMPARISON
# ------------------------------------------
brand_vendor_price = (
    purchases
    .groupby(["Brand", "VendorName"])["PurchasePrice"]
    .mean()
    .reset_index()
    .sort_values(by="PurchasePrice", ascending=False)
)

brand_vendor_price.to_csv(
    "brand_vendor_price_comparison.csv",
    index=False
)
print("brand_vendor_price_comparison.csv saved")

# ------------------------------------------
# 6. SALES ANALYSIS (CHUNK PROCESSING)
# ------------------------------------------
print("\n--- SALES ANALYSIS (CHUNK PROCESSING) ---")

sales_chunks = pd.read_csv(
    sales_file,
    chunksize=500_000
)

sales_summary_list = []

for chunk in sales_chunks:
    temp = (
        chunk
        .groupby("InventoryId")[["SalesQuantity", "SalesDollars"]]
        .sum()
        .reset_index()
    )
    sales_summary_list.append(temp)

sales_summary = (
    pd.concat(sales_summary_list)
    .groupby("InventoryId")
    .sum()
    .reset_index()
)

# ------------------------------------------
# 7. INVENTORY + SALES (FAST / SLOW MOVING)
# ------------------------------------------
inventory_sales = inventory_movement.merge(
    sales_summary,
    on="InventoryId",
    how="left"
)

inventory_sales.fillna(0, inplace=True)

q75 = inventory_sales["SalesQuantity"].quantile(0.75)
q25 = inventory_sales["SalesQuantity"].quantile(0.25)

def sales_category(x):
    if x >= q75:
        return "Fast Moving"
    elif x <= q25:
        return "Slow Moving"
    else:
        return "Medium Moving"

inventory_sales["Sales_Category"] = inventory_sales["SalesQuantity"].apply(sales_category)

inventory_sales.to_csv(
    "inventory_sales_movement_summary.csv",
    index=False
)

print("inventory_sales_movement_summary.csv saved")

print("\n✅ PROJECT EXECUTION COMPLETED SUCCESSFULLY")




