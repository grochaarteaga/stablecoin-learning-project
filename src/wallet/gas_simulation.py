from web3 import Web3
import os
from dotenv import load_dotenv

load_dotenv()

# --- Connect to mainnet ---
alchemy_url = os.getenv("ALCHEMY_URL_MAINNET")
w3 = Web3(Web3.HTTPProvider(alchemy_url))

if not w3.is_connected():
    print("❌ Connection to mainnet failed.")
    exit()

sender = os.getenv("SENDER_ADDRESS")
receiver = os.getenv("RECEIVER_ADDRESS")

print("✅ Connected to Ethereum Mainnet")
print(f"👛 Sender: {sender}")
print(f"🎯 Receiver: {receiver}")

# --- 1️⃣  Build a fake ETH transaction ---
tx = {
    "from": sender,
    "to": receiver,
    "value": w3.to_wei(0.001, "ether"),
}

# --- 2️⃣  Estimate gas ---
estimated_gas = w3.eth.estimate_gas(tx)
gas_price = w3.eth.gas_price
fee_eth = (estimated_gas * gas_price) / 10**18

print("\n=== Gas Simulation ===")
print(f"🧮 Estimated Gas: {estimated_gas} units")
print(f"💸 Gas Price: {gas_price / 10**9:.2f} gwei")
print(f"⚙️ Estimated Fee: {fee_eth:.6f} ETH")

# --- 3️⃣  Estimate fee in USD ---
import requests
price = requests.get(
    "https://api.coingecko.com/api/v3/simple/price",
    params={"ids": "ethereum", "vs_currencies": "usd"}
).json()["ethereum"]["usd"]

fee_usd = fee_eth * price
print(f"💵 Estimated Fee: ${fee_usd:.4f} USD")