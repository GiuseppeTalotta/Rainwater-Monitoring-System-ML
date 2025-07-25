import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

# Carica il modello salvato
model = joblib.load("model_acqua.pkl")

# Personalizzazione pagina
st.set_page_config(page_title="Classificazione Qualità Acqua", layout="centered")

# Titolo principale
st.markdown("<h1 style='text-align: center; font-size: 30px;'>💧 Classificatore qualità dell'acqua</h1>", unsafe_allow_html=True)
st.markdown("---")

# 🔹 Sezione di inserimento manuale
st.markdown("### 📝 Inserimento manuale")
ph = st.number_input("🔹 Inserisci il valore di pH", min_value=0.0, max_value=14.0, step=0.1)
cond = st.number_input("🔹 Inserisci la conducibilità (μS/cm)", min_value=0, step=1)

if st.button("🔍 Classifica"):
    risultato = model.predict([[ph, cond]])
    if risultato[0] == 1:
        st.markdown("<p style='color: green; font-size: 18px;'>✅ Acqua Buona per l'irrigazione</p>", unsafe_allow_html=True)
    else:
        st.markdown("<p style='color: red; font-size: 18px;'>❌ Acqua Non Buona per l'irrigazione</p>", unsafe_allow_html=True)

# 🔹 Sezione: Caricamento file CSV
st.markdown("---")
st.markdown("### 📂 Carica file CSV")
file = st.file_uploader("📄 Carica un file con valori di pH e conducibilità", type=["csv", "txt", "tsv"])

if file is not None:
    try:
        # Prova vari separatori
        separators = [",", ";", "\t"]
        df = None
        for sep in separators:
            file.seek(0)
            temp_df = pd.read_csv(file, sep=sep)
            temp_df.columns = temp_df.columns.str.strip().str.lower()
            if "ph" in temp_df.columns and "conducibilita" in temp_df.columns:
                df = temp_df
                break

        if df is not None:
            st.success(f"✅ Colonne rilevate: {df.columns.tolist()}")
            predizioni = model.predict(df[["ph", "conducibilita"]])
            df["Qualità"] = ["Buona" if p == 1 else "Non Buona" for p in predizioni]
            st.subheader("📊 Risultati")
            st.dataframe(df)

            # 🔸 Grafico a dispersione
            fig1 = px.scatter(df, x="ph", y="conducibilita", color="Qualità",
                              title="🔬 Distribuzione pH e Conducibilità",
                              labels={"ph": "pH", "conducibilita": "Conducibilità"})
            st.plotly_chart(fig1)

            # 🔸 Grafico a barre
            count_df = df["Qualità"].value_counts().reset_index()
            count_df.columns = ["Qualità", "Conteggio"]
            fig2 = px.bar(count_df, x="Qualità", y="Conteggio", color="Qualità",
                          title="📈 Conteggio qualità acqua (Bar Chart)")
            st.plotly_chart(fig2)
        else:
            st.warning("⚠️ Il file deve contenere le colonne 'ph' e 'conducibilita'.")
    except Exception as e:
        st.error(f"❌ Errore durante la lettura o analisi del file: {e}")

# 🔹 Sezione: Chi siamo
st.markdown("---")
st.markdown("""
    <div style='text-align: center; font-size: 15px; color: gray;'>
        <strong style='font-size: 16px;'>👨‍🎓 Chi sono</strong><br>
        Mi chiamo <b>Giuseppe Talotta</b>, ho sviluppato questa applicazione come parte del mio progetto di tesi.<br>
        L'app consente di analizzare rapidamente la qualità dell'acqua attraverso modelli di machine learning,
        con una semplice interfaccia accessibile anche a utenti non esperti.
    </div>
""", unsafe_allow_html=True)

# 🔹 Sfondo
st.markdown("""
    <style>
        .stApp {
            background-image: url('https://images.unsplash.com/photo-1534081333815-ae5019106621?auto=format&fit=crop&w=1600&q=80');
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
        }
    </style>
""", unsafe_allow_html=True)
