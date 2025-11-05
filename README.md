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

## ✅ Day 3 – Wallet Setup & Balance Reading
- Added the **Sepolia** test network to MetaMask  
  *(MetaMask now auto-names it “Sepolia” with symbol “SepoliaETH”)*.
- Requested **free test ETH** from the Sepolia faucet (0.15 – 0.5 SepoliaETH).  
- Copied wallet address and created script `src/wallet/balance.py` to read balance.  
- Confirmed the program returns the live on-chain value.

**Output Example**
 Wallet: 0xB7C4Eb5F98Fad995E940476711fe0785b66D5851
Balance: 0.149582088703659 SepoliaETH


### 🚀 Day 4 – Sending Transactions
- Created a second MetaMask wallet  
- Stored both wallet addresses + private key in `.env` (testnet only)  
- Wrote `src/wallet/transfer.py` to send 0.01 SepoliaETH  
- Verified the transaction on [Sepolia Etherscan](https://sepolia.etherscan.io)

**Example Output**
🚀 Transaction sent! Hash: 0xbb572c108efbcca7931230a7972a135b477cf836b0caf724ffd093bdddd9dd9f
🔍 View it on: https://sepolia.etherscan.io/tx/0xbb572c108efbcca7931230a7972a135b477cf836b0caf724ffd093bdddd9dd9f



---

## 🧰 Tech Stack
Python · web3.py · dotenv · Alchemy · MetaMask · Streamlit (later)

---

## 📁 Project Structure

stablecoin-learning-project/
├── README.md
├── .env
├── requirements.txt
├── docs/
│ └── plan.md
└── src/
├── main.py
└── wallet/
├── balance.py
└── transfer.py


---

## ⚙️ How to Run

1️⃣ Clone the repo  
```bash
git clone https://github.com/grochaarteaga/stablecoin-learning-project.git
cd stablecoin-learning-project

2️⃣ Activate virtual env and install deps
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

3️⃣ Add your .env
ALCHEMY_URL=https://eth-sepolia.g.alchemy.com/v2/YOUR_KEY
SENDER_PRIVATE_KEY=your_wallet1_private_key
SENDER_ADDRESS=0xYourWallet1
RECEIVER_ADDRESS=0xYourWallet2


4️⃣ Run connection test
python src/main.py

5️⃣ Run balance check
python src/wallet/balance.py

6️⃣ Send test transaction
python src/wallet/transfer.py


