import streamlit as st
from web3 import Web3
import os
import requests
from dotenv import load_dotenv
from datetime import datetime

# --- Load environment variables ---
load_dotenv()

# --- Connect to Ethereum Mainnet ---
alchemy_url = os.getenv("ALCHEMY_URL_MAINNET")
w3 = Web3(Web3.HTTPProvider(alchemy_url))
address = os.getenv("SENDER_ADDRESS")

st.set_page_config(page_title="Crypto Portfolio", page_icon="💰")
st.title("💰 My Crypto Portfolio Dashboard")
st.caption("Live balances fetched from Ethereum Mainnet (Alchemy + CoinGecko)")

if not w3.is_connected():
    st.error("❌ Connection to Ethereum failed.")
    st.stop()

# --- Wallet Info ---
st.write(f"**Wallet:** `{address}`")

# --- Fetch ETH Balance ---
eth_balance = w3.eth.get_balance(address) / 10**18

# --- Fetch Token Balance (DAI example) ---
token_address = "0x6B175474E89094C44Da98b954EedeAC495271d0F"  # Mainnet DAI
token_abi = [
    {"constant": True, "inputs": [{"name": "_owner", "type": "address"}],
     "name": "balanceOf", "outputs": [{"name": "balance", "type": "uint256"}],
     "type": "function"},
    {"constant": True, "inputs": [], "name": "decimals",
     "outputs": [{"name": "", "type": "uint8"}], "type": "function"},
    {"constant": True, "inputs": [], "name": "symbol",
     "outputs": [{"name": "", "type": "string"}], "type": "function"},
]
token = w3.eth.contract(address=w3.to_checksum_address(token_address), abi=token_abi)
decimals = token.functions.decimals().call()
symbol = token.functions.symbol().call()
token_balance = token.functions.balanceOf(address).call() / (10 ** decimals)

# --- Fetch Live Prices ---
prices = requests.get(
    "https://api.coingecko.com/api/v3/simple/price",
    params={"ids": "ethereum,dai", "vs_currencies": "usd"}
).json()
eth_price = prices["ethereum"]["usd"]
dai_price = prices["dai"]["usd"]

# --- Calculate Values ---
eth_usd = eth_balance * eth_price
dai_usd = token_balance * dai_price
total_usd = eth_usd + dai_usd

# --- Display Portfolio Summary ---
st.subheader("📊 Portfolio Summary")
col1, col2, col3 = st.columns(3)
col1.metric("ETH Balance", f"{eth_balance:.5f} ETH", f"${eth_usd:,.2f}")
col2.metric("DAI Balance", f"{token_balance:.2f} {symbol}", f"${dai_usd:,.2f}")
col3.metric("💵 Total Value", f"${total_usd:,.2f}")

st.divider()
st.subheader("🧾 Recent Transactions")

# --- Fetch Transaction History (Etherscan V2 API) ---
api_key = os.getenv("ETHERSCAN_API_KEY")
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

res = requests.get(url, params=params)
data = res.json()

txs = data.get("result") or data.get("data", {}).get("result") or []

if txs:
    table_data = []
    for tx in txs:
        table_data.append({
            "Date": datetime.fromtimestamp(int(tx["timeStamp"])).strftime("%Y-%m-%d %H:%M"),
            "Value (ETH)": round(int(tx["value"]) / 10**18, 6),
            "Status": "✅ Success" if tx["isError"] == "0" else "❌ Failed",
            "Hash": f"[{tx['hash'][:12]}…](https://etherscan.io/tx/{tx['hash']})"
        })
    st.table(table_data)
else:
    st.info("No recent transactions found or Etherscan API error.")

st.caption("💾 Data sources : Alchemy • CoinGecko • Etherscan V2 API")
