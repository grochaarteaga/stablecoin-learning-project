import requests
import os
from dotenv import load_dotenv
from datetime import datetime
from web3 import Web3

load_dotenv()

address = Web3.to_checksum_address(os.getenv("SENDER_ADDRESS"))
api_key = os.getenv("ETHERSCAN_API_KEY")

# Use new V2 API
url = "https://api.etherscan.io/v2/api"

params = {
    "chainid": 1,  # Ethereum Mainnet
    "module": "account",
    "action": "txlist",
    "address": address,
    "startblock": 0,
    "endblock": 99999999,
    "page": 1,
    "offset": 5,
    "sort": "desc",
    "apikey": api_key
}

response = requests.get(url, params=params)
data = response.json()

print("URL:", response.url)
print("Status:", data.get("status"))

# V2 now nests results under data.result
txs = data.get("data", {}).get("result", [])

if data.get("status") == "1" and data.get("result"):
    txs = data["result"]
elif data.get("status") == "1" and data.get("data", {}).get("result"):
    txs = data["data"]["result"]
else:
    txs = []

if txs:
    print(f"\n=== Last {len(txs)} Transactions for {address} ===")
    for tx in txs:
        time = datetime.fromtimestamp(int(tx["timeStamp"])).strftime("%Y-%m-%d %H:%M")
        value_eth = int(tx["value"]) / 10**18
        status = "✅ Success" if tx["isError"] == "0" else "❌ Failed"
        print(f"{time} | {value_eth:.4f} ETH | {status}")
        print(f"→ {tx['hash']}\n")
else:
    print("❌ No transactions found or error.")
