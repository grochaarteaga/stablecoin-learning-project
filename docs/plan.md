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

---

## Day 3 – Wallet Setup & Balance Reading
- Added Sepolia network in MetaMask
- Received 0.5 SepoliaETH from faucet
- Read wallet balance using Python + web3.py
- Verified on-chain connection works

---
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

---

## ✅ Day 5 – Interacting with ERC-20 Smart-Contract (DAI)
- Reviewed what **smart-contracts** are: self-executing programs on the blockchain.  
- Understood that stablecoins (like USDC) are smart-contracts that maintain internal ledgers of ownership.  
- Realized Circle has not deployed USDC on Sepolia (only on Mainnet / Goerli).  
- Connected to verified **DAI** contract on Sepolia (`0x68194a729C2450ad26072b3D33ADaCbcef39D574`).  
- Created `src/wallet/token_balance.py` to read:
  - `symbol()` → returns token symbol  
  - `decimals()` → returns decimal precision  
  - `balanceOf(address)` → returns token balance  
- Verified output and confirmed 0 DAI balance (no tokens yet).  
- Learned difference between:
  - **Native ETH** – balance lives on the account  
  - **Tokens (ERC-20)** – balance lives inside a smart-contract  
- Key takeaways:
  - Wrong contract/network ⇒ no code ⇒ `BadFunctionCallOutput`
  - Always check Etherscan → “Contract” tab = real code


## ✅ Day 6 – Sending ERC-20 Tokens
- Used `transfer()` to send 0.1 DAI between two wallets.
- Learned how token transfers differ from ETH transfers.
- Understood how `approve()` and `allowance()` enable DeFi apps.
- Observed that insufficient balance transactions still appear on-chain.
- Verified tx hash on Sepolia Etherscan.

## ✅ Day 7 – Approve & Allowance
- Learned that DeFi apps cannot move tokens without permission.
- Explored how ERC-20 `approve()` and `allowance()` work.
- Built `token_approve.py` to authorize a spender for 1 DAI.
- Verified on Etherscan that the approval transaction was confirmed.
- Learned that:
  - `approve` gives rights,
  - `allowance` checks limits,
  - `transferFrom` spends the approved tokens.

## ✅ Day 9 – Connect to Ethereum Mainnet
- Created new Alchemy Mainnet app.
- Connected to live Ethereum network.
- Read real ETH balance from MetaMask wallet.
- Fetched live ETH/USD price using CoinGecko.
- Verified that Python balance matches MetaMask.
- Learned mainnet = real ETH, Sepolia = test ETH.

## ✅ Day 10 – Gas & Simulation
- Learned what gas, gas price, and gas limit mean.
- Created script to estimate gas usage for ETH transfers.
- Calculated estimated gas fee in ETH and USD.
- Understood that estimate_gas simulates execution without broadcasting.
- Learned difference in cost between simple and complex transactions.
