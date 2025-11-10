from web3 import Web3
import os
from dotenv import load_dotenv
import requests

load_dotenv()

# --- Choose the mainnet connection ---
alchemy_url = os.getenv("ALCHEMY_URL_MAINNET")
w3 = Web3(Web3.HTTPProvider(alchemy_url))

if not w3.is_connected():
    print("❌ Connection to mainnet failed.")
    exit()

address = os.getenv("SENDER_ADDRESS")
print(f"✅ Connected to Ethereum Mainnet")
print(f"👛 Wallet: {address}")

# --- 1️⃣  Get ETH balance ---
eth_balance = w3.eth.get_balance(address) / 10**18  # in ETH

# --- 2️⃣  Get ETH price from CoinGecko ---
response = requests.get("https://api.coingecko.com/api/v3/simple/price",
                        params={"ids": "ethereum", "vs_currencies": "usd"},
                        timeout=10)
eth_price = response.json()["ethereum"]["usd"]

# --- 3️⃣  Calculate USD value ---
eth_usd_value = eth_balance * eth_price

# --- 4️⃣  Display ---
print("\n=== Real ETH Balance ===")
print(f"💰 {eth_balance:.6f} ETH")
print(f"💵 ≈ ${eth_usd_value:,.2f} USD (based on CoinGecko)")