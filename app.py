import streamlit as st
import random

# ----------- CONFIG -----------
st.set_page_config(
    page_title="RNG Ikan Roblox – Secret Chance",
    page_icon="🐟",
    layout="centered"
)

# ----------- CUSTOM CSS -----------
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #71b7e6, #9b59b6);
        color: white;
    }
    .title {
        text-align: center;
        font-size: 40px;
        font-weight: 900;
        color: #fff;
        text-shadow: 1px 1px 3px #000;
        margin-bottom: 10px;
    }
    .subtitle {
        text-align: center;
        color: #f0f0f0;
        margin-top: -10px;
        font-size: 18px;
    }
    .card {
        background: rgba(255,255,255,0.15);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
        backdrop-filter: blur(8px);
    }
    .result-box {
        padding: 15px;
        border-radius: 10px;
        background: rgba(255,255,255,0.2);
        font-size: 22px;
        font-weight: 700;
        text-align: center;
    }
    .gacha-btn button {
        background-color: #ffdd57 !important;
        color: #000 !important;
        font-weight: 700 !important;
        border-radius: 10px !important;
    }
    </style>
""", unsafe_allow_html=True)

# ----------- TITLE -----------
st.markdown("<div class='title'>🐟 RNG Ikan Roblox</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Hitung peluang mendapatkan ikan Secret</div><br>", unsafe_allow_html=True)


# ----------- INPUT SECTION -----------
st.markdown("<div class='card'>", unsafe_allow_html=True)

st.subheader("📥 Input Jumlah Ikan per Rarity")

legend = st.number_input("Legendary", min_value=0, value=5)
epic = st.number_input("Epic", min_value=0, value=10)
rare = st.number_input("Rare", min_value=0, value=20)
mystic = st.number_input("Mitos", min_value=0, value=1)

st.markdown("</div>", unsafe_allow_html=True)


# ----------- CALCULATE SECRET CHANCE -----------
total = legend + epic + rare + mystic

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("📊 Hasil Perhitungan")

if total == 0:
    st.warning("Isi jumlah ikan dulu! Pool masih kosong.")
    secret_chance = 0
else:
    secret_chance = (1 / total) * 100
    st.markdown(
        f"<div class='result-box'>🎯 Peluang Secret: <br><span style='font-size:35px'>{secret_chance:.6f}%</span></div>",
        unsafe_allow_html=True
    )
    st.write(f"Total ikan (tanpa secret): **{total}**")

st.markdown("</div>", unsafe_allow_html=True)


# ----------- GACHA SIMULATION -----------
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("🎣 Simulasi Gacha (1x)")

col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.markdown("<div class='gacha-btn'>", unsafe_allow_html=True)
    gacha = st.button("🎁 Coba Gacha!")
    st.markdown("</div>", unsafe_allow_html=True)

if gacha:

    if total == 0:
        st.error("Pool kosong, nggak bisa gacha.")
    else:
        # Secret success check based on chance
        roll = random.random() * 100  # 0–100

        if roll < secret_chance:
            result = "Secret"
        else:
            # pick normal rarity proportional to amount
            pool = (
                ["Legendary"] * legend +
                ["Epic"] * epic +
                ["Rare"] * rare +
                ["Mitos"] * mystic
            )
            result = random.choice(pool)

        if result == "Secret":
            st.success("🔥 SELAMAT! Kamu dapat **SECRET**!! GGWP 🚀")
        else:
            st.info(f"Kamu dapat: **{result}**")

st.markdown("</div>", unsafe_allow_html=True)
