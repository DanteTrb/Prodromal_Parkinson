import streamlit as st

st.set_page_config(page_title="🧠 Monitoraggio Prodromico", layout="centered")

st.title("🧠 Valutazione rischio prodromico Parkinson")
st.markdown("Inserisci i valori del soggetto sano. Se ha i **prodromi 1011** e parametri clinico-biomeccanici tipici, suggeriremo il monitoraggio.")

st.header("📥 Input soggetto sano")

# === INPUT: Feature biomeccaniche e cliniche ===
cadence = st.number_input("Cadence", min_value=80.0, max_value=140.0, value=100.0)
det_ml = st.number_input("%det ML", min_value=10.0, max_value=80.0, value=35.0)
det_ap = st.number_input("%det AP", min_value=10.0, max_value=80.0, value=40.0)
tilt = st.number_input("Tilt", min_value=0.0, max_value=6.0, value=3.0)
double_support = st.number_input("Double Support (%)", min_value=0.0, max_value=60.0, value=22.0)
single_support = st.number_input("Single Support (%)", min_value=0.0, max_value=60.0, value=27.0)
stride_length = st.number_input("Stride Length (m)", min_value=0.5, max_value=3.0, value=1.6)

age = st.number_input("Età", min_value=18, max_value=100, value=70)
sex = st.selectbox("Sesso", options=["Maschio", "Femmina"])
duration = st.number_input("Durata dei sintomi (anni)", min_value=0, max_value=30, value=5)
onset = st.selectbox("Onset", options=["Early (<49)", "Middle (50–69)", "Late (>70)"])
postural = st.selectbox("Postural Alteration", options=["No", "Sì"])

# === TRASFORMAZIONE LOGICA ===
sex_val = 1 if sex == "Maschio" else 2
onset_val = {"Early (<49)": 1, "Middle (50–69)": 2, "Late (>70)": 3}[onset]
postural_val = 1 if postural == "Sì" else 2

# === REGOLA 1011: prodromi specifici presenti ===
has_1011 = st.checkbox("✅ Il soggetto ha la combinazione prodromica 1011", value=True)

# === LOGICA DECISIONALE ===
if st.button("🔍 Valuta il rischio"):
    if has_1011:
        if (
            100 <= cadence <= 110 and
            30 <= det_ml <= 45 and
            15 <= det_ap <= 50 and
            2.5 <= tilt <= 3.5 and
            20 <= double_support <= 30 and
            20 <= single_support <= 30 and
            1.3 <= stride_length <= 1.9 and
            65 <= age <= 75 and
            1 <= sex_val <= 2 and
            6 <= duration <= 14 and
            1 <= onset_val <= 2 and
            postural_val == 1
        ):
            st.success("✅ Profilo a rischio identificato: si consiglia **monitoraggio clinico**.")
        else:
            st.warning("🟡 Il soggetto ha i prodromi 1011 ma **non rientra nei range biomeccanici caratteristici**.")
    else:
        st.info("🟢 I prodromi 1011 **non sono presenti**. Nessuna azione urgente.")