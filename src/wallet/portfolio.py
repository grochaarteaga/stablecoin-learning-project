from web3 import Web3
import requests
import os
from dotenv import load_dotenv

load_dotenv()

# --- Connect to Ethereum ---
alchemy_url = os.getenv("ALCHEMY_URL")
w3 = Web3(Web3.HTTPProvider(alchemy_url))
address = os.getenv("SENDER_ADDRESS")

if not w3.is_connected():
    print("❌ Connection failed.")
    exit()
print("✅ Connected to blockchain")

# --- 1️⃣  Get ETH balance ---
eth_balance = w3.eth.get_balance(address) / 10**18  # in ETH

# --- 2️⃣  Get DAI balance (ERC-20 on Sepolia) ---
dai_contract = w3.eth.contract(
    address=w3.to_checksum_address("0x68194a729C2450ad26072b3D33ADaCbcef39D574"),
    abi=[
        {"constant": True, "inputs": [{"name": "_owner", "type": "address"}],
         "name": "balanceOf", "outputs": [{"name": "balance", "type": "uint256"}],
         "type": "function"},
        {"constant": True, "inputs": [], "name": "decimals",
         "outputs": [{"name": "", "type": "uint8"}], "type": "function"},
        {"constant": True, "inputs": [], "name": "symbol",
         "outputs": [{"name": "", "type": "string"}], "type": "function"},
    ]
)

dai_decimals = dai_contract.functions.decimals().call()
dai_balance = dai_contract.functions.balanceOf(address).call() / 10**dai_decimals

# --- 3️⃣  Get real-world prices from CoinGecko ---
try:
    response = requests.get(
        "https://api.coingecko.com/api/v3/simple/price",
        params={"ids": "ethereum,dai", "vs_currencies": "usd"},
        timeout=10
    )
    prices = response.json()
    eth_price = prices["ethereum"]["usd"]
    dai_price = prices["dai"]["usd"]
except Exception as e:
    print("❌ Error fetching prices:", e)
    eth_price = dai_price = 0

# --- 4️⃣  Calculate USD values ---
eth_usd = eth_balance * eth_price
dai_usd = dai_balance * dai_price
total_usd = eth_usd + dai_usd

# --- 5️⃣  Display summary ---
print("\n=== Portfolio Summary ===")
print(f"💰 ETH Balance: {eth_balance:.5f}  (~${eth_usd:,.2f})")
print(f"🪙 DAI Balance: {dai_balance:.2f}  (~${dai_usd:,.2f})")
print(f"📊 Total Portfolio: ${total_usd:,.2f}")