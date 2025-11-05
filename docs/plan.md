# Stablecoin Learning Project – 14-Day Plan

---

## ✅ Day 1 – Stablecoin Fundamentals
- Learned about the main types of stablecoins  
  - **Fiat-backed**: USDC, USDT (backed by cash or short-term Treasuries)  
  - **Crypto-backed**: DAI (over-collateralized with ETH or stETH)  
  - **Algorithmic**: UST (collapsed – lesson on why stability mechanisms matter)
- Understood how stablecoins maintain their peg.
- Created GitHub repository `stablecoin-learning-project`.
- Added first documentation files and committed them.

---

## ✅ Day 2 – Python Setup + Blockchain Connection
- Installed Python 3, created a virtual environment `.venv`.
- Installed `web3.py` and `python-dotenv`.
- Registered on **Alchemy** and generated an Ethereum **Sepolia** API key.
- Added the key to `.env` and wrote the first script (`src/main.py`) to connect.
- Verified connection and printed the latest Sepolia block number.  


## Day 3 – Wallet Setup & Balance Reading

- Added Sepolia network in MetaMask
- Received 0.5 SepoliaETH from faucet
- Read wallet balance using Python + web3.py
- Verified on-chain connection works

## ✅ Day 4 – Sending ETH Transaction
- Created second MetaMask wallet for testing.
- Exported private key (Wallet 1) and stored it securely in `.env`.
- Wrote `src/wallet/transfer.py` to send 0.01 SepoliaETH to Wallet 2.
- Fixed attribute naming for Web3 v7 (`raw_transaction` instead of `rawTransaction`).
- Verified transaction on [Sepolia Etherscan](https://sepolia.etherscan.io).
- Learned:
  - **Nonce** = transaction counter per wallet  
  - **Gas & Gas Price** = transaction fees  
  - **Signing** = authorizing transfer with private key  
  - **Tx Hash** = unique ID for the transaction