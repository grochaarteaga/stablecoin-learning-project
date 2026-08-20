# Stablecoin Learning Project 💸

This repository documents my **14-day journey** learning how stablecoins and crypto transactions work by building a **mini stablecoin wallet** in Python.

# From zero to a real USDC transfer on mainnet, in fourteen days

I work in payments and I did not want to reason about stablecoins from slides, so I gave myself two weeks to go from nothing to moving real money onchain from my own code, and I logged every day of it.

**Where it ended up**

- A signed USDC transfer on Ethereum mainnet, confirmed on Etherscan
- ERC 20 `approve` and `allowance` implemented and verified, the mechanics every DeFi and payment integration depends on
- Gas estimation and cost simulation before sending
- A dashboard showing live ETH, DAI and USDC balances with USD valuation from CoinGecko
- Transaction history through the Etherscan v2 multichain API, migrated off the deprecated v1

**Why the daily log is still here**

Because the log is the point. Most of my work is going into a domain I do not know yet and being useful in it quickly. This is fourteen days of that, written down while it happened.

Python · web3.py · Alchemy · Streamlit · Etherscan · CoinGecko

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



### 🧩 Day 5 – Interacting with ERC-20 Smart-Contracts
- Learned what **smart-contracts** are and why tokens like USDC are contracts.
- Used verified **DAI** contract on Sepolia (`0x68194a729C2450ad26072b3D33ADaCbcef39D574`).
- Created `src/wallet/token_balance.py` to read token info (`symbol`, `decimals`, `balanceOf`).

**Example Output**
🪙 Token: DAI
💰 Address: 0xB7C4Eb5F98Fad995E940476711fe0785b66D5851
Balance: 0.0 DAI


### 💸 Day 6 – Token Transfers
- Implemented ERC-20 `transfer()` using web3.py.
- Sent (or simulated) 0.1 DAI between wallets.
- Learned about gas, nonce, and transaction signing for tokens.

**Example Output**
🚀 Token transfer submitted! Hash: 0x0cf4cb306e31930974e3ab7c56c6c8c864e2132edfdec0a2344edbf2d02829b6
🔍 View on Etherscan: https://sepolia.etherscan.io/tx/0x0cf4cb306e31930974e3ab7c56c6c8c864e2132edfdec0a2344edbf2d02829b6

### 🧠 Day 7 – Approve & Allowance
- Implemented ERC-20 `approve()` and `allowance()`.
- Understood how DeFi apps use these to spend tokens.
- Verified approval on Etherscan.

**Example Output**
Approve transaction sent! Hash: 0x0a2dd40e436283324d8d3d46654ed8692f56b590e8e035e6caa9e428e29c81c4
🔍 View it on: https://sepolia.etherscan.io/tx/0x0a2dd40e436283324d8d3d46654ed8692f56b590e8e035e6caa9e428e29c81c4
📊 Allowance for spender: 1.0 DAI

**Concepts Learned**
- Smart-contract = program that lives on the blockchain.  
- ERC-20 defines standard token functions (`balanceOf`, `transfer`, `approve`).  
- Sepolia doesn’t host official USDC, so we use mock DAI for testing.  
- On Mainnet, Circle’s verified USDC contract address works the same way.  

### 🌍 Day 9 – Mainnet Connection
- Connected to Ethereum Mainnet (real blockchain).
- Read wallet’s real ETH balance in USD.
- Verified exact match with MetaMask.
- No private key used (read-only).

### ⛽ Day 10 – Gas & Simulation
- Simulated real ETH transaction cost without sending.
- Estimated gas usage and converted fee to USD.
- Learned how Ethereum fees work in practice.

### 🖥️ Day 11 – Streamlit Dashboard
- Added interactive dashboard to visualize wallet balances.
- Used Streamlit to display ETH and DAI values in USD.
- Data sources: Alchemy (on-chain) + CoinGecko (off-chain).

---

### 🧾 Day 12 – Transaction History (Etherscan V2)
- Upgraded from deprecated Etherscan V1 API to the new V2 Multichain API.
- Added `chainid=1` for Ethereum mainnet compatibility.
- Displayed the last 5 transactions directly in the dashboard.
- Each transaction hash links to its Etherscan page.
- Dashboard now combines:
  - 🔹 Live ETH & DAI balances
  - 🔹 Real-time USD values (CoinGecko)
  - 🔹 Recent transaction history (Etherscan)

---

### 💸 Day 13 – Real USDC Transfer (Mainnet)
- Connected to Alchemy mainnet node.
- Built and signed USDC transfer using Web3.py.
- Confirmed successful transaction on Etherscan.
- Demonstrated full end-to-end wallet integration from code.

### 💰 Day 14 – Dashboard with ETH, DAI & USDC
- Displays live ETH, DAI, and USDC balances from Ethereum Mainnet.
- Calculates USD value using CoinGecko API.
- Automatically updates portfolio total.


### 🛠️ Technical Notes
- Using Etherscan V2 ensures long-term API stability (post-Aug 2025).
- Minor indexing delay is expected before new transactions appear.
- Optional: install `watchdog` for faster Streamlit reloads.


---

## 🧰 Tech Stack
Python · web3.py · dotenv · Alchemy · MetaMask · Streamlit (later)

---

## 📁 Project Structure

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


4. Run connection test
python src/main.py

5️. Run balance check
python src/wallet/balance.py

6. Send test transaction
python src/wallet/transfer.py

7. Read DAI token balance
python src/wallet/token_balance.py
