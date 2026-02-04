# Inventory-Analysis
Built an end-to-end retail analytics solution covering inventory movement, sales performance, and vendor costs. Used Python chunk-based aggregation to handle large datasets efficiently. Analyzed opening vs closing stock, classified fast/slow movers, compared vendor spend and prices, and delivered insights via an interactive Power BI dashboard.

Business Objectives

Analyze opening vs closing inventory to identify stock changes.

Classify products into fast-moving, medium, and slow-moving items.

Evaluate vendor-wise purchase spend.

Identify high-cost vendors and pricing inefficiencies.

Build a Power BI dashboard for business users.

🗂️ Dataset Description

The project uses multiple CSV files representing different business processes:

begin_inventory.csv – Opening inventory levels

end_inventory.csv – Closing inventory levels

purchases.csv – Purchase transactions

vendor_invoice.csv – Vendor billing information

purchase_prices.csv – Product purchase prices

sales.csv – Large sales dataset (1.5 GB, processed using chunks)

🛠️ Tools & Technologies

Python (Pandas, NumPy)

Power BI (Data modeling & visualization)

CSV datasets

Chunk-based data processing for large files

🔄 Project Workflow
1️⃣ Data Loading & Inspection

Loaded multiple CSV files

Verified schema, data types, duplicates, and missing values

Identified key columns such as InventoryId, VendorName, and sales metrics

2️⃣ Inventory Movement Analysis

Aggregated opening and closing stock using InventoryId

Calculated stock change and categorized inventory as:

Increased

Decreased

No Change

📄 Output:
inventory_movement_summary.csv

3️⃣ Vendor & Purchase Cost Analysis

Vendor-wise total purchase spend

Vendor-wise average purchase price

Brand + Vendor price comparison to detect overpriced suppliers

📄 Outputs:

vendor_purchase_summary.csv

vendor_price_comparison.csv

brand_vendor_price_comparison.csv

4️⃣ Inventory + Sales Analysis (Large Data Handling)

Processed 12+ million sales records using chunk-based aggregation

Created sales summary per product

Merged inventory and sales data

Classified products into:

Fast Moving

Medium Moving

Slow Moving

📄 Output:
inventory_sales_movement_summary.csv

5️⃣ Power BI Dashboard

Built an interactive dashboard featuring:

KPI cards (Total Sales, Quantity, Fast Moving Products)

Inventory movement analysis

Vendor spend & price comparison

Fast vs slow-moving product insights

