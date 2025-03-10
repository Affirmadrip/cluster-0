import streamlit as st

# Set up the page configuration
st.set_page_config(page_title="Well Shop", layout="wide")

# CSS for styling the page
st.markdown("""
    <style>
        html, body, [class*="st-emotion-cache"] {
            font-family: 'Arial', sans-serif;
            background: linear-gradient(to right, #ffde59, #ff914d);
        }

        .title {
            font-size: 40px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 30px;
            color: #333;
        }

        .banner {
            width: 100%;
            height: 600px;
            background: linear-gradient(135deg, #6a11cb, #2575fc);
            border-radius: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 3px 5px 15px rgba(0, 0, 0, 0.2);
            overflow: hidden;
            position: relative;
            margin-bottom: 40px;
        }

        .banner img {
            width: 800px;
            height: 600px;
            object-fit: cover;
            border-radius: 20px;
            opacity: 0.85;
        }

        .banner-text {
            position: absolute;
            font-size: 32px;
            font-weight: bold;
            color: white;
            text-shadow: 2px 2px 10px rgba(0, 0, 0, 0.5);
        }

        .subtitle {
            font-size: 26px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 20px;
            color: #444;
        }

        .product-box {
            width: 100%;
            max-width: 500px;
            height: auto;
            border-radius: 15px;
            box-shadow: 2px 4px 8px rgba(0, 0, 0, 0.1);
            padding: 15px;
            text-align: center;
            background: white;
            transition: transform 0.2s, box-shadow 0.2s;
            margin-bottom: 20px;
        }

        .product-box img {
            width: 100%;
            height: auto;
            object-fit: cover;
            border-radius: 10px;
        }

        .product-box:hover {
            transform: scale(1.05);
            box-shadow: 4px 6px 12px rgba(0, 0, 0, 0.2);
        }

        .product-name {
            font-size: 16px;
            font-weight: bold;
            margin-top: 10px;
        }

        .product-price {
            font-size: 14px;
            color: #E44D26;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Store name
st.markdown("<div class='title'>Well Shop</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Recommendations for teenagers through to middle-aged customers</div>", unsafe_allow_html=True)

# Hot-Deal
st.markdown("<div class='subtitle'>❄️ Winter Hot Deal ❄️</div>", unsafe_allow_html=True)
st.image("https://i.imgur.com/KpBYIVy.jpeg", use_container_width=True)

# Product categories and their respective images with titles
categories = {
    "Recommended Clothings 👔": [
        {"url": "https://i.imgur.com/IUmsPud.jpeg", "title": "Shirt"},
        {"url": "https://i.imgur.com/4eThFKY.jpeg", "title": "Pants"},
        {"url": "https://i.imgur.com/JqFZekN.jpeg", "title": "Black Blouse"},
        {"url": "https://i.imgur.com/nT9QTcO.jpeg", "title": "Red Blouse"},
        {"url": "https://i.imgur.com/TJR7Uuv.jpeg", "title": "Indigo Shorts"},
        {"url": "https://i.imgur.com/RPOLH6K.jpeg", "title": "Black Shorts"},
        {"url": "https://i.imgur.com/ozgzDqx.jpeg", "title": "Grey Shirt"},
        {"url": "https://i.imgur.com/Eolcc9V.jpeg", "title": "Light Grey Shirt"}
    ],
    "Accessories 💎": [
        {"url": "https://i.imgur.com/he93pjD.jpeg", "title": "Backpack"},
        {"url": "https://i.imgur.com/iYhiqha.jpeg", "title": "Belt"},
        {"url": "https://i.imgur.com/avYSpDI.jpeg", "title": "Hat"},
        {"url": "https://i.imgur.com/OqFHMuv.jpeg", "title": "Jewelry Necklace"},
        {"url": "https://i.imgur.com/7O1K734.jpeg", "title": "Scarf"},
        {"url": "https://i.imgur.com/DJP2YYG.jpeg", "title": "Polarized Sunglasses"},
        {"url": "https://i.imgur.com/YaB7wCm.jpeg", "title": "UV400 Fashioned Sunglasses"},
    ],
    "Footwear 👞": [
        {"url": "https://i.imgur.com/WrZwaCb.jpeg", "title": "Sandals"},
        {"url": "https://i.imgur.com/UJ7lVRf.jpeg", "title": "White Sneakers"},
        {"url": "https://i.imgur.com/BWH9unv.jpeg", "title": "Black Sneakers"},
        {"url": "https://i.imgur.com/z94viq3.jpeg", "title": "Shoes"},
        {"url": "https://i.imgur.com/YX8pU6Y.jpeg", "title": "Boots"}
    ],
    "Outerwear 🧥": [
        {"url": "https://i.imgur.com/OPMicJ1.jpeg", "title": "Coat"},
        {"url": "https://i.imgur.com/ipv6U6Z.jpeg", "title": "Jacket"}
    ]
}

cols_per_row = 4  # Define the number of columns per row

for category, products in categories.items():
    st.markdown(f"<div class='subtitle'>{category}</div>", unsafe_allow_html=True)
    total_products = len(products)
    index = 0
    
    # Calculate number of full rows and remainder products for the last row
    full_rows = total_products // cols_per_row
    remainder_products = total_products % cols_per_row

    # Display full rows
    for _ in range(full_rows):
        col_group = st.columns(cols_per_row)  # Create a full row of columns
        for col in col_group:
            product = products[index]
            with col:
                st.markdown(f"""
                    <div class='product-box'>
                        <img src='{product["url"]}' alt='{product["title"]}'>
                        <div class='product-name'>{product["title"]}</div>
                    </div>
                """, unsafe_allow_html=True)
            index += 1

    # Display remainder row with adjusted column widths if needed
    if remainder_products > 0:
        # Create adjusted column width ratios to fill the row
        col_widths = [1] * remainder_products  # This ensures each column takes up equal space
        col_group = st.columns(col_widths)
        
        for i in range(remainder_products):
            product = products[index]
            with col_group[i]:
                st.markdown(f"""
                    <div class='product-box'>
                        <img src='{product["url"]}' alt='{product["title"]}'>
                        <div class='product-name'>{product["title"]}</div>
                    </div>
                """, unsafe_allow_html=True)
            index += 1







