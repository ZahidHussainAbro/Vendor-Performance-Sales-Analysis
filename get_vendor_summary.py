import pandas as pd
import os
from sqlalchemy import create_engine
import logging
from ingestion_db import ingest_db

logging.basicConfig(
    filename="logs/get_vendor_summary.logs",
    level=logging.DEBUG,
    format="%(asctime)s-%(levelname)s-%(message)s",
    filemode="a"
)

def create Vendor_Summary(conn):
""" This function will merge the different tables to get overall vendor summary and adding new columns resultant data"""
       Vendor_Sales_Summary= pd.read_sql_query(""" WITH FreightSummary AS(
  SELECT
     VendorNumber,
     SUM(freight) AS FreightCost
  FROM vendor_invoice
  GROUP BY VendorNumber
),

PurchaseSummary AS(
  SELECT
     p.VendorNumber,
     p.VendorName,
     p.Brand,
     P.Description,
     p.PurchasePrice,
     pp.Price AS ActualPrice,
     pp.Volume,
     SUM(p.Quantity) as TotalPurchaseQuantity,
     SUM(p.Dollars) as TotalPurchaseDollars
  FROM purchases p
  JOIN purchase_prices pp
     ON p.Brand=pp.Brand
  WHERE p.PurchasePrice> 0
  GROUP BY p.VendorNumber, p.VendorName, p.Brand, p.Description, p.PurchasePrice, pp.Price, pp.Volume
),

SalesSummary AS(
   SELECT
     VendorNo,
     Brand,
     SUM(SalesDollars) as TotalSalesDollars,
     SUM(SalesPrice) as TotalSalesPrice,
     SUM(SalesQuantity) as TotalSalesQuantity,
     SUM(ExciseTax) as TotalExciseTax
  FROM sales 
  GROUP BY VendorNo, Brand
)

SELECT
  ps.VendorNumber,
  ps.VendorName,
  ps.Brand,
  ps.Description,
  ps.PurchasePrice,
  ps.ActualPrice,
  ps.Volume,
  ps.TotalPurchaseQuantity,
  ps.TotalPurchaseDollars,
  ss.TotalSalesDollars,
  ss.TotalSalesPrice,
  ss.TotalSalesQuantity,
  ss.TotalExciseTax,
  fs.FreightCost
FROM PurchaseSummary ps
LEFT JOIN SalesSummary ss
  ON ps.VendorNumber=ss.VendorNo
  AND ps.Brand=ss.Brand
LEFT JOIN FreightSummary fs
  ON ps.VendorNumber=fs.VendorNumber
ORDER BY ps.TotalPurchaseDollars DESC""", conn)
return Vendor_Sales_Summary

def clean_data(df):
    """this function will clean the data"""
    # changing datatype to float
      df["Volume"]= df["Volume"].astype("float64")
 
    # filling missing value with 0
      df.fillna(0, inplace=True)

    # removing spaces from categorical columns
      df["VendorName"]= Vendor_Sales_Summary["VendorName"].str.strip()
      df["Description"]= df[]"Description"].str.strip()

    # creating new columns for better analysis
      Vendor_Sales_Summary["GrossProfit"]= Vendor_Sales_Summary["TotalSalesDollars"]- Vendor_Sales_Summary["TotalPurchaseDollars"]
      Vendor_Sales_Summary["GrossProfit"].min()
      Vendor_Sales_Summary["ProfitMargin"]= Vendor_Sales_Summary["GrossProfit"]/ Vendor_Sales_Summary["TotalPurchaseDollars"]*100
      Vendor_Sales_Summary["StockTurnover"]= Vendor_Sales_Summary["TotalSalesQuantity"]/ Vendor_Sales_Summary["TotalPurchaseDollars"]
      Vendor_Sales_Summary["SalestoPurchaseRatio"]= Vendor_Sales_Summary["TotalSalesDollars"]/ Vendor_Sales_Summary["TotalPurchaseDollars"]


      return df
          
if __name__=='__main__':
    # create database connection
    conn= sqlite3.connect("inventory_db")

    logging.info("Creating Vendor Summary Tale.....")
    Summary_df= Create_Vendor_Summary(conn)
    logging.info(Summary_df.head())

    logging.info("Cleaning Data.....")
    clean_df= clean_data(Summary_df)
    logging.info(clean_df.head())

    logging.info("Ingesting data.....")
    ingest_db(clean_df, "Vendor_Sales_Summary", conn)
    logging.info("Completed")