import streamlit as st
import pandas as pd

# Load dataset
df = pd.read_csv("amazon.csv")

# Drop rows with critical missing info
df.dropna(subset=["product_name", "discounted_price", "rating", "product_link"], inplace=True)

# Keep only rows with valid image links (basic filtering)
df = df[df["img_link"].str.contains("http", na=False) & df["img_link"].str.contains(r'\.(jpg|jpeg|png|webp)', case=False)]

# Streamlit page setup
st.set_page_config(page_title="Amazon Recommender", layout="wide")
st.title("🛍️ Amazon Product Recommender")
st.markdown("Get personalized product suggestions based on your selection.")

# Category filter
categories = df["category"].dropna().unique()
selected_category = st.selectbox("📂 Filter by Category (optional)", ["All"] + sorted(categories))

# Filter products by selected category
filtered_df = df if selected_category == "All" else df[df["category"] == selected_category]

# Product selection
product_names = filtered_df["product_name"].unique()
selected_product = st.selectbox("🔍 Choose a Product", sorted(product_names))

# Get selected product details
product_info = filtered_df[filtered_df["product_name"] == selected_product].iloc[0]

# Display selected product info
st.markdown("### 🎯 Selected Product")
with st.container():
    cols = st.columns([1, 3])
    with cols[0]:
        st.image(product_info["img_link"], width=180, caption="Selected Product")
    with cols[1]:
        st.markdown(f"**🛍️ {product_info['product_name']}**")
        st.markdown(f"💸 Price: `{product_info['discounted_price']}`")
        st.markdown(f"⭐ Rating: `{product_info['rating']}`")
        st.markdown(f"🔗 [View on Amazon]({product_info['product_link']})")
        if pd.notnull(product_info['about_product']):
            st.markdown(f"📄 _{product_info['about_product'][:300]}..._")

# Recommended products from same category
st.markdown("---")
st.subheader("📌 Recommended Products")

recommendations = filtered_df[
    (filtered_df["product_name"] != selected_product) &
    (filtered_df["category"] == product_info["category"])
].head(5)

for _, row in recommendations.iterrows():
    with st.container():
        cols = st.columns([1, 3])
        with cols[0]:
            st.image(row["img_link"], width=140, caption="Recommendation")
        with cols[1]:
            st.markdown(f"**🛍️ {row['product_name']}**")
            st.markdown(f"💸 Price: `{row['discounted_price']}` | ⭐ Rating: `{row['rating']}`")
            st.markdown(f"🔗 [View on Amazon]({row['product_link']})")
            if pd.notnull(row["about_product"]):
                st.markdown(f"📄 _{row['about_product'][:200]}..._")
        st.markdown("---")
