## 🛍️ Amazon Product Recommender
An interactive Streamlit web app that suggests similar Amazon products based on the user's selected item and category.
Cleanly designed and easy to use, the app features product images, prices, ratings, and direct Amazon links — all powered by a structured CSV dataset.

🔗 Live App: https://amazon-recommedation.streamlit.app

## 🚀 Features
🔍 Product Selection: Choose from hundreds of Amazon products

📂 Category Filter: Narrow down choices by product category

💡 Smart Suggestions: Get 5 related product recommendations

🖼️ Image Display: View product images with graceful fallback

💸 See Pricing and Ratings

🔗 Direct Amazon Links: Buy or view more details instantly

## 🧾 Dataset
This app uses a cleaned CSV file containing:

product_name

category

discounted_price

rating

about_product

img_link

product_link

## 📍 Source: Scraped Amazon data (shared locally via amazon.csv)

## 🧰 Built With
Python

Pandas

Streamlit

## 📦 Installation
Clone this repo and run it locally:

git clone https://github.com/your-username/amazon-recommender-app.git
cd products_review

# (Optional) Create virtual environment
python -m venv venv
source venv/bin/activate  # or use venv\Scripts\activate on Windows

## Install dependencies
pip install streamlit pandas
▶️ Run the App
bash
Copy
Edit
streamlit run product_review.py
Make sure amazon.csv is in the same directory.

💡 How It Works
Loads and filters product data from a CSV file.

Allows user to pick a category and product.

Displays product details and 5 related recommendations.

Ensures only valid product images are shown.

## ✨ Future Improvements
✅ Default placeholder for broken image URLs

🔎 Add keyword search functionality

❤️ Save user favorites (wishlist)

📊 Add sorting (e.g., by price or rating)

## 👩‍💻 Developed By
Chaviva Otabor
📧 favourotabor16@gmail.com
🔗 GitHub Profile

## 📜 License
MIT License. Feel free to use and customize this project.

