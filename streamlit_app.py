import streamlit as st
import pickle
import numpy as np

# ====================================
# PAGE CONFIG
# ====================================
st.set_page_config(
    page_title="Crop Recommendation System",
    page_icon="🌱",
    layout="wide"
)

# ====================================
# MODERN PREMIUM UI DESIGN (CSS)
# ====================================
st.markdown("""
<style>
/* Hide default Streamlit clutter */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Global Theme & Background */
.stApp {
    background: radial-gradient(circle at 50% 50%, #0d1527 0%, #050914 100%);
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

/* Typography Overrides */
h1, h2, h3, p, label {
    color: #f3f4f6 !important;
}

/* Compact Page Spacing Tweak */
div[data-testid="stMainBlockContainer"] {
    padding-top: 20px !important;
    padding-bottom: 20px !important;
}

/* Isolated Login Wrapper Box */
.login-centered-container {
    max-width: 450px;
    margin: 80px auto 0px auto;
    text-align: center;
}

/* Bolder & Scaled Middle Title */
.login-title {
    font-size: 54px;
    font-weight: 900;
    background: linear-gradient(135deg, #4ade80 0%, #22c55e 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 6px;
    letter-spacing: -1.5px;
}

.login-subtitle {
    color: #9ca3af !important;
    font-size: 15px;
    font-weight: 400;
    margin-bottom: 40px;
}

/* Dashboard Input Box Styling Rules */
div[data-testid="stWidgetLabel"] p {
    font-size: 14px !important;
    font-weight: 600 !important;
    color: #9ca3af !important;
    margin-bottom: 4px !important;
    text-align: left !important;
}

.stTextInput input {
    background-color: rgba(17, 24, 39, 0.7) !important;
    border: 1px solid #1f2937 !important;
    border-radius: 10px !important;
    color: #ffffff !important;
    font-size: 15px !important;
    height: 44px !important;
    padding: 0 16px !important;
    transition: all 0.25s ease;
}

.stTextInput input:focus {
    border-color: #22c55e !important;
    box-shadow: 0 0 0 3px rgba(34, 197, 94, 0.15) !important;
    background-color: #111827 !important;
}

/* Styled Action Button (Strict Full-Width Override) */
div.stButton > button {
    width: 100% !important;
    height: 48px !important;
    font-size: 16px !important;
    font-weight: 600 !important;
    border-radius: 10px !important;
    background: linear-gradient(90deg, #16a34a, #22c55e) !important;
    color: white !important;
    border: none !important;
    transition: all 0.25s ease-in-out !important;
    margin-top: 10px !important;
    box-shadow: 0 4px 12px rgba(34, 197, 94, 0.2) !important;
}

div.stButton > button:hover {
    background: linear-gradient(90deg, #15803d, #16a34a) !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 16px rgba(34, 197, 94, 0.3) !important;
}

/* NATIVE CONTAINER PREMIUM OVERRIDE (Fixes the ghost container bug completely) */
div[data-testid="stMainBlockContainer"] div[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(255, 255, 255, 0.02) !important;
    backdrop-filter: blur(12px) !important;
    -webkit-backdrop-filter: blur(12px) !important;
    border: 1px solid rgba(255, 255, 255, 0.05) !important;
    border-radius: 20px !important;
    padding: 25px 30px !important;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.25) !important;
    margin-top: 10px !important;
    margin-bottom: 15px !important;
}

/* Top Right Logout Button Specific Styling Override */
div[data-testid="stColumn"]:last-child div.stButton > button {
    background: rgba(239, 68, 68, 0.1) !important;
    border: 1px solid rgba(239, 68, 68, 0.15) !important;
    color: #ef4444 !important;
    height: 38px !important;
    font-size: 14px !important;
    margin-top: 0px !important;
    box-shadow: none !important;
}

div[data-testid="stColumn"]:last-child div.stButton > button:hover {
    background: #ef4444 !important;
    color: white !important;
    transform: none !important;
    box-shadow: none !important;
}

/* Premium Dynamic Result Card */
.result-card {
    background: linear-gradient(135deg, rgba(22, 101, 52, 0.8), rgba(21, 128, 61, 0.8));
    border: 1px solid rgba(74, 222, 128, 0.3);
    backdrop-filter: blur(10px);
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    margin-top: 15px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.3);
}

.result-heading {
    font-size: 16px;
    font-weight: 500;
    color: #bbf7d0 !important;
    text-transform: uppercase;
    letter-spacing: 2px;
}

.crop-name {
    font-size: 52px;
    font-weight: 900;
    color: #fef08a !important;
    margin-top: 5px;
    letter-spacing: -1px;
}
</style>
""", unsafe_allow_html=True)

# ====================================
# LOGIN DETAILS
# ====================================
USER = "admin"
PASSWORD = "crop123"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ====================================
# LOGIN PAGE
# ====================================
def login():
    st.markdown('<div class="login-centered-container">', unsafe_allow_html=True)
    
    st.markdown("""
        <div class="login-title">🌱 Smart Farming</div>
        <div class="login-subtitle">Machine Learning Based Crop Recommendation System</div>
    """, unsafe_allow_html=True)

    username = st.text_input("👤 Username", placeholder="Enter your username")
    password = st.text_input("🔒 Password", type="password", placeholder="Enter your password")
    login_btn = st.button("Login 🚀")
    
    if login_btn:
        if username == USER and password == PASSWORD:
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.markdown("<br>", unsafe_allow_html=True)
            st.error("❌ Invalid credentials. Please try again.")
            
    st.markdown('</div>', unsafe_allow_html=True)

# Check authentication status
if not st.session_state.logged_in:
    login()
    st.stop()

# ====================================
# TOP HEADER BAR (LOGOUT BUTTON)
# ====================================
nav_col1, nav_col2 = st.columns([8.8, 1.2])

with nav_col2:
    if st.button("Log Out "):
        st.session_state.logged_in = False
        st.rerun()

# ====================================
# DASHBOARD INTERFACE
# ====================================
st.markdown('<h1 style="text-align: center; font-size: 44px; font-weight: 800; margin-bottom: 2px; margin-top: -20px;">🌾 Crop Recommendation Dashboard</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #9ca3af; font-size: 16px; margin-bottom: 15px;">Provide soil analysis parameters & microclimate conditions below</p>', unsafe_allow_html=True)

# FIXED: Replaced unsafe direct HTML div text segments with Streamlit's native clean container layout card
with st.container(border=True):
    col1, col2, col3 = st.columns(3, gap="large")

    with col1:
        st.markdown("### 🧪 Soil Compositions")
        N = st.text_input("Nitrogen (N Ratio)", placeholder="e.g. 90")
        P = st.text_input("Phosphorus (P Ratio)", placeholder="e.g. 42")
        K = st.text_input("Potassium (K Ratio)", placeholder="e.g. 43")

    with col2:
        st.markdown("### 🌤️ Environment Metrics")
        temperature = st.text_input("Temperature (°C)", placeholder="e.g. 24.5")
        humidity = st.text_input("Relative Humidity (%)", placeholder="e.g. 82.1")

    with col3:
        st.markdown("### 💧 Hydrological Indices")
        ph = st.text_input("Soil pH Level", placeholder="e.g. 6.5")
        rainfall = st.text_input("Annual Rainfall (mm)", placeholder="e.g. 202.4")

# Action execution bar
b_col1, b_col2, b_col3 = st.columns([1.2, 1, 1.2])
with b_col2:
    predict = st.button("Recommend Crop ✨")

# ====================================
# ML PREDICTION HANDLER
# ====================================
if predict:
    try:
        model = pickle.load(open("crop_model.pkl", "rb"))
        
        input_data = np.array([[
            float(N),
            float(P),
            float(K),
            float(temperature),
            float(humidity),
            float(ph),
            float(rainfall)
        ]])

        prediction = model.predict(input_data)[0]

        st.markdown(
            f"""
            <div class="result-card">
                <div class="result-heading">✨ Best Matching Crop Detected</div>
                <div class="crop-name">✨ {prediction.upper()} ✨</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    except ValueError:
        st.error("⚠️ Formatting Error: Please verify all text fields contain numeric integers/decimals before executing.")
    except FileNotFoundError:
        st.error("📂 Model Error: Could not locate your engine file 'crop_model.pkl' inside this working path directory.")
    except Exception as e:
        st.error(f"💥 An unexpected error occurred: {str(e)}")