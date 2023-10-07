import streamlit as st
import pandas as pd
import numpy as np
import matplotlib as plt

review_sale_df = all_df.groupby("product_category_name_english").agg({"review_score":"mean","order_id":"count"}).sort_values(by ="review_score",ascending=True).reset_index()
review_sale_df.head(5)

plt.figure(figsize=(20, 5))

colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
 
sns.barplot(x="order_id", y="product_category_name_english", data=review_sale_df.head(5), palette=colors)
plt.ylabel(None)
plt.xlabel(None)
plt.title("Kategori Produk Dengan Review Score Terendah", loc="center", fontsize=15)
plt.tick_params(axis ='y', labelsize=12)



cust = all_df.customer_city.value_counts().head(10)
print(cust)
plt.figure(figsize=(20, 10))
pl = cust.plot(kind="bar",rot=0)
plt.ylabel(None)
plt.xlabel(None)
plt.title("Kota dengan jumlah customer terbesar", loc="center", fontsize=15)
plt.tick_params(axis ='y', labelsize=12)
plt.tick_params(axis ='x', labelsize=12)


all_df = pd.read_csv("D:\Dimas Jalu P S\Database\Shopping Fest\all_data.csv")