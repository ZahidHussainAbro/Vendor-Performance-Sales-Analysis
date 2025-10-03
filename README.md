#  🛒 Vendor-Performance-Sales-Analysis (2024-2025)
Python+SQL+PowerBI Project

## Part 1: Company Overview and Goal

The company operates in the **retail and consumer goods industry**, distributing a variety of fast-moving products such as beverages, personal care, household goods, dairy, and snacks across physical stores and digital platforms.
company wants to optimize its sales inventory, cost, and stocks


### Business Goals:
- Analyze and extract insights from monthly, yearly stock inventory vendor trends to improve **stock inventory** and **sales performance**
- Identify **top-performing vendors** contributing to sales and gross profit and **underperforming vendors** that require promotional or pricing adjustments **shipping segments**
- Investigate **profitability** between top-performing and low-performing vendors
- Evaluate **sales performance** (delayed stock, shipping inventory costs, unsold stock) to optimize inventory and the impact of **bulk purchasing** on unit costs
- Assess **inventory turnover** to reduce holding costs and improve efficiency
- Improve sales inventory with key **key performing vendors** and **top products**

---

## Part 2: Dataset Overview
Six CSV-based tables as begin_inventory, end_inventory, purchase, purchase_prices, sales, invoice_payment. Sales with 1 crore+ records. Similarly, used python-pandas, high-level data overview, extracted initial data for EDA using sqlite3, and ingested into the database using queries, data cleaning, and feature selection, performed Exploratory Data Analysis, identified patterns, trends, relevant answerable columns, and then extracted the final vendor summary analysis table through SQL queries.
# Python Scripts
- for automating workflow
- Measuring query performance time, data processing, functionality monitoring

### Key Columns:
Vendor Number,	Vendor Name,	Brand,	Description,	Purchase Price,	Actual Price,	Volume,	Total Purchase Quantity,	Total Purchase Dollars,	Total Sales Dollars,	Total Sales Price,	Total Sales Quantity,	Total Excise Tax,	Freight Cost,	Gross Profit,	Profit Margin,	Stock Turnover,	Sales Purchase Ratio.

### Supplementary Fields:
- VendorName,	Brand Unique Number, Brand Description, Purchase Price,	Actual Price, Freight Cost
The dataset spans from **2024 to 2025**, enabling detailed month-over-month and year-over-year analysis.

---

## Part 3: Analytical Framework

### Supporting Metrics:
- Gross Profit  
- Profit Margin 
- Stock Turnover 
- Sales Purchase Ratio  

### Key Dimensions:
- Time (Month-Year)  
- Vendor Name 
- Brand description (Actual Price, Total Excise Tax, Freight Cost, Total Purchase Dollars,	Total Sales Dollars) 

### Analysis Objectives:
- Understand revenue trends over time  
- Analyze vendor-level performance  
- Measure Month-over-Month (MoM) and Year-over-Year (YoY) growth  
- Assess performance across vendor Brands and Sales Turnover  
- Derive insights to guide promotional strategy, budget allocation, and inventory planning

---

## Part 4: Summary Recommendations

Based on the insights derived from the 2022–2023 dataset, here are high-level recommendations aligned with the business goals:

- **Stabilize February Performance:** Launch retention or loyalty campaigns in late January to avoid revenue loss during seasonal dips.
- **Capitalize on Strong Categories:** Invest in Personal Care and Household during Q2 and Q4 as they consistently show peak performance.
- **Enhance Online Experience:** With online revenue outpacing in-store, focus on digital UX, personalization, and exclusive online deals.
- **Refine Membership Strategy:** Convert declining Regular members into VIPs with structured loyalty incentives.
- **Target 18–45 Age Group:** Tailor product placements and marketing campaigns toward younger and mid-career consumers who showed the most growth.

---

## Part 5: Executive Summary

![image](https://github.com/user-attachments/assets/3c4bd3df-2bd2-4859-af0a-85e061f1d51f)

In 2023, revenue peaked in *January*, followed by a sharp decline in *February* — the lowest point of the year. Subsequent spikes occurred in *May* and *August*, then stabilizing  to *December*. 
In contrast, 2022 showed a more consistent trend from *January* to *October*, before declining in *November*.

By region, *Sydney* generated the most revenue in 2022, while *Melbourne* led in 2023.

At the category level, *Personal Care* was the top-performing segment in 2023, whereas *Snacks* led in 2022.

Among individual products, *Soda* consistently ranked as a top contributor in both years. The lowest-performing products were *Cheese* in 2022 and *Nuts Mix* in 2023.

---

## Part 6: Orders and AOV Performance

![image](https://github.com/user-attachments/assets/d9bdca5b-889b-4236-a33e-2e348f6200bd)

### Key Observations:
- **February** marked the lowest performance across both metrics: orders dropped **31.5%** and AOV fell to **$116.93 (-12.3%)**, resulting in the sharpest monthly revenue decline.
- **March to July** showed steady recovery. **July** was particularly strong — it had one of the **highest order counts (140)** and also the **highest AOV ($145.60)**, contributing to a secondary revenue peak.
- **November** had the **second-lowest order volume**, but revenue stayed relatively stable thanks to a **significant increase in AOV ($143.78, +30.9%)** — indicating customers placed fewer but higher-value orders.

### Recommendations:
- **Stabilize February** with early Q1 promotions or loyalty pushes to avoid simultaneous drops in both volume and value.
- **Leverage high-AOV months** (like **July and November**) to introduce premium product bundles or upsell offers.
- Use insights from **November’s high-AOV behavior** to build **holiday season strategies** that focus on value per customer, even if volume is lower.
- Tailor marketing to monthly AOV patterns — deploy **basket-size incentives** during low-AOV periods and focus on **premium promotions** during high-AOV months.
---

## Part 7: Deep Dive – Product Category Breakdown

![image](https://github.com/user-attachments/assets/d7b406f3-a4c0-42ae-893d-cc3d62586bba)

### Key Observations:
In 2023, January recorded the highest monthly revenue, driven by increases across nearly all product categories — particularly Personal Care. The only exception was Household, which declined slightly.

In contrast, February experienced the lowest revenue of the year, showing a steep 39.9% drop from January. This was primarily due to sharp declines across all major categories, especially:

- Beverages: ↓ 63.9%  
- Dairy: ↓ 42.4%  
- Snacks: ↓ 47.0%

Revenue recovered strongly in March, increasing by 42% compared to February, mainly due to:

- Beverages: ↑ 102%  
- Household: ↑ 81.6%

From March through July, revenue showed a general upward trend, peaking with a spike in May, despite Snacks contributing only 6% of total revenue that month — indicating other categories (especially Beverages and Personal Care) drove the growth.

After July, revenue dipped slightly in August, then remained relatively stable through November, before picking up again in December — likely reflecting end-of-year consumer activity and holiday demand.

### Recommendations:
