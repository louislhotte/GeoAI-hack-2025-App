import streamlit as st

# Set page configuration
st.set_page_config(page_title="Locust Breeding Hotspots", layout="wide")

# Add a background image
st.markdown(
    """
    <style>
        .main {
            background: url('https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Desert_Locust.jpg/1280px-Desert_Locust.jpg');
            background-size: cover;
            background-position: center;
        }
        .title {
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            color: black;
        }
        .subtitle {
            text-align: center;
            font-size: 20px;
            font-weight: bold;
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title Section
st.markdown('<p class="title">🌍 Locust Breeding Hotspots Forecast</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Monitoring and predicting locust outbreaks using geospatial data</p>', unsafe_allow_html=True)

# # Add a high-quality locust image
# st.image(
#     "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Schistocerca_gregaria_Egypt_02.jpg/800px-Schistocerca_gregaria_Egypt_02.jpg",
#     caption="Desert Locust Swarm in Action",
#     use_column_width=True,
# )

# Sidebar Navigation
st.sidebar.header("🛰️ Navigation")
st.sidebar.subheader("Use the menu below to explore locust hotspot predictions.")

# Welcome Section
st.write(
    """
    🌱 **Welcome to InstaGeo Serve!**
    This interactive application uses **GeoTIFF satellite data** and **predictive modeling** to visualize 
    potential **locust breeding hotspots**. By leveraging **remote sensing**, we can help mitigate locust 
    plagues and protect food security in affected regions.

    🗺️ **What You Can Do:**
    - View interactive maps of **locust-prone areas** 📍
    - Analyze historical breeding patterns 📊
    - Gain insights for **early warning systems** 🚨
    - Assist in **agricultural and environmental planning** 🌾

    🔎 **Select a page from the sidebar to begin your exploration!**
    """
)

# Footer with a call to action
st.markdown("---")
st.markdown(
    "<p style='text-align: center; font-size: 18px;;'><b>🌾 Predict. Prevent. Protect. 🌍</b></p>",
    unsafe_allow_html=True,
)