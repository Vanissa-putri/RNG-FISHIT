import streamlit as st

st.set_page_config(page_title="RNG Ikan Roblox – Secret Chance", page_icon="🐟")

st.title("🐟 RNG Ikan Roblox")
st.write("Hitung peluang dapat ikan **Secret** berdasarkan jumlah tiap rarity.")

st.subheader("Input Jumlah Ikan Berdasarkan Rarity")

legend = st.number_input("Jumlah Ikan Legendary", min_value=0, value=5)
epic = st.number_input("Jumlah Ikan Epic", min_value=0, value=10)
rare = st.number_input("Jumlah Ikan Rare", min_value=0, value=20)
mitos = st.number_input("Jumlah Ikan Mitos", min_value=0, value=1)
secret = st.number_input("Jumlah Ikan Secret", min_value=0, value=1)

total = legend + epic + rare + mitos + secret

st.divider()

st.subheader("📊 Hasil Perhitungan")

if total == 0:
    st.warning("Isi jumlah ikan dulu, total masih 0.")
else:
    chance_secret = (secret / total) * 100
    st.success(f"🎯 **Kemungkinan dapat Secret: {chance_secret:.4f}%**")
    st.write(f"Total semua ikan: **{total}**")

st.divider()

st.subheader("🎣 Simulasi Gacha (1x)")

import random

if st.button("Coba Gacha"):
    pool = (
        ["Legendary"] * legend +
        ["Epic"] * epic +
        ["Rare"] * rare +
        ["Mitos"] * mitos +
        ["Secret"] * secret
    )

    if len(pool) == 0:
        st.error("Pool masih kosong, tidak bisa gacha.")
    else:
        result = random.choice(pool)
        if result == "Secret":
            st.success("🔥 Kamu dapat **SECRET**!! GG EZ")
        else:
            st.info(f"Kamu dapat: **{result}**")
