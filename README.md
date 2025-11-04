# Stablecoin Learning Project 💸

This repository documents my **14-day journey** learning how stablecoins and crypto transactions work by building a **mini stablecoin wallet** in Python.

---

## 🧠 Project Goals

- Understand how stablecoins (USDC, DAI, USDT) work
- Learn blockchain basics (wallets, gas, transactions, nodes)
- Build and test transactions on the Ethereum **Sepolia** testnet
- Create a Python mini wallet using **web3.py**
- Optionally deploy a small smart contract (escrow logic)

---

## 🧰 Tech Stack

- **Python 3**
- **web3.py** — interact with Ethereum blockchain  
- **python-dotenv** — manage secrets (API keys)  
- **Alchemy** — blockchain node provider  
- **MetaMask** — wallet for test transactions  
- **Streamlit (later)** — UI for the wallet  

---

## 📆 Progress Log

### ✅ **Day 1 – Stablecoin Fundamentals**
- Learned types of stablecoins (Fiat-backed, Crypto-backed, Algorithmic)
- Created GitHub repo structure
- Committed and published project

### ✅ **Day 2 – Blockchain Connection**
- Set up Python virtual environment (`.venv`)
- Installed `web3.py` and `python-dotenv`
- Created Alchemy account and testnet API key  
- Connected successfully to **Ethereum Sepolia testnet**
- Printed live block number from the blockchain 🎉  

**Output example:**
✅ Connected to Ethereum Sepolia testnet!
Current block number: 9560105


Next step → **Day 3: Connect MetaMask and read wallet balance.**

---

## 🗂️ Project Structure



stablecoin-learning-project/
├── README.md
├── .gitignore
├── requirements.txt
├── .env
├── docs/
│ └── plan.md
└── src/
└── main.py


---

## ⚙️ How to Run

1. Clone the repo  
   ```bash
   git clone https://github.com/grochaarteaga/stablecoin-learning-project.git
   cd stablecoin-learning-project


Create a virtual environment

python3 -m venv .venv
source .venv/bin/activate


Install dependencies

pip install -r requirements.txt


Add your .env file with your Alchemy URL

ALCHEMY_URL=https://eth-sepolia.g.alchemy.com/v2/YOUR_API_KEY


Run the script

python src/main.py