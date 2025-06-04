# 🧠 Prodromal Parkinson Monitor: Clinical Rule-based App powered by Streamlit

## 🧾 Overview

**Prodromal Parkinson Monitor** è una webapp interattiva sviluppata con **Streamlit**, pensata per aiutare clinici e ricercatori a monitorare soggetti sani che mostrano **pattern motori e clinici compatibili con fasi prodromiche del Parkinson**.

L'app sfrutta regole cliniche derivate da un'analisi approfondita di un dataset reale per suggerire il monitoraggio in presenza di specifiche combinazioni di:
- caratteristiche demografiche
- parametri di cammino
- marker clinici
- segnali di instabilità posturale

Tutto in un'interfaccia semplice, accessibile e spiegabile.

## 📊 Cosa fa l'app

- ✅ Permette di inserire **feature cliniche e cinematiche** di un soggetto
- ✅ Applica **regole decisionali trasparenti** e interpretabili
- ✅ Genera un **output diretto**: *monitoraggio raccomandato* oppure *nessun segnale rilevante*
- ✅ Interfaccia **real-time** in Streamlit
- ✅ Supporto a **estensioni future** (modelli ML, explainability, salvataggio dati)

## 💡 Logica Decisionale

L'algoritmo attuale si basa su **regole statiche** estratte da uno studio statistico e clinico.

## 📂 Struttura della Repository

Prodromal_Parkinson/
│
├── data/ # Dataset pulito e aggregato
├── figures/ # Grafici ed export di analisi
├── models/ # (future) Modelli ML/XAI
├── notebooks/ # Notebook di analisi e sviluppo
├── webapp.py # Codice principale della webapp Streamlit
├── requirements.txt # Dipendenze Python
├── .gitignore # Esclusione cartelle pesanti
└── README.md # (Questo file)

## 🧠 Dataset e Feature Usate

Il dataset include soggetti **sani e parkinsoniani**, con valutazioni su:

- **Demografici:** Sesso, Età, Anni dalla diagnosi
- **Prodromi:** Stipsi, Iposmia, RBD, Depressione (presenti come colonne)
- **Cinematica del passo:** Cadence, Double Support, Single Support, Stride Length
- **Postura e stabilità:** %Det ML/AP, Tilt, Postural Alteration

Tutte le soglie usate nell'app derivano da una **distribuzione empirica** su un campione clinico reale.

## 🚀 Avvio Locale

1. Clona la repo  
-bash
git clone https://github.com/DanteTrb/Prodromal_Parkinson.git
cd Prodromal_Parkinson

# Crea e attiva un virtualenv
python3 -m venv .venv
source .venv/bin/activate

# Installa le dipendenze
pip install -r requirements.txt
# Avvia l'app
streamlit run webapp.py

✅ Si aprirà nel browser.

---

## 🌐 Deployment Online

L'app è disponibile anche pubblicamente via **Streamlit Cloud**:

👉 [Clicca qui per provarla](https://appromalparkinson-rnf9afzmjxeh8huhotlsze.streamlit.app/)  

## 🔮 Sviluppi Futuri

##  Roadmap futura

- 🔍 Integrazione modelli ML per classificazione combinata
- 🧠 SHAP / SHAPSet plot per interpretabilità
- 🩺 Esportazione in PDF del profilo soggetto
- 💾 Salvataggio dati in backend cloud (es. Firebase / PostgreSQL)
- 👨‍⚕️ Possibilità di usare anche test cognitivi e funzionali

## 👨‍🔬 Autore

Sviluppato da **Dante Trabassi**  
PhD Candidate & AI Biomedical Researcher  
Sapienza Università di Roma – Dipartimento di Neuroscienze  

🔗 [LinkedIn](https://www.linkedin.com/in/dantetrabassi)  
📬 Contatti disponibili nella sezione profilo