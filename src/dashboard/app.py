import streamlit as st
from web3 import Web3
import os
import requests
from dotenv import load_dotenv

# --- Load environment variables ---
load_dotenv()

# --- Connect to Ethereum Mainnet ---
alchemy_url = os.getenv("ALCHEMY_URL_MAINNET")
w3 = Web3(Web3.HTTPProvider(alchemy_url))
address = os.getenv("SENDER_ADDRESS")

# --- Title ---
st.set_page_config(page_title="Crypto Portfolio", page_icon="💰")
st.title("💰 My Crypto Portfolio Dashboard")
st.caption("Live balances fetched from Ethereum Mainnet")

if not w3.is_connected():
    st.error("❌ Connection to Ethereum failed.")
    st.stop()

# --- Fetch ETH Balance ---
eth_balance = w3.eth.get_balance(address) / 10**18

# --- Fetch Token Balance (DAI example) ---
token_address = "0x6B175474E89094C44Da98b954EedeAC495271d0F"  # mainnet DAI
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

# --- Fetch live prices (CoinGecko) ---
prices = requests.get(
    "https://api.coingecko.com/api/v3/simple/price",
    params={"ids": "ethereum,dai", "vs_currencies": "usd"}
).json()
eth_price = prices["ethereum"]["usd"]
dai_price = prices["dai"]["usd"]

# --- Calculate values ---
eth_usd = eth_balance * eth_price
dai_usd = token_balance * dai_price
total_usd = eth_usd + dai_usd

# --- Display ---
st.subheader("📊 Portfolio Summary")
st.write(f"**Wallet:** `{address}`")
st.metric("ETH Balance", f"{eth_balance:.5f} ETH", f"${eth_usd:,.2f}")
st.metric("DAI Balance", f"{token_balance:.2f} {symbol}", f"${dai_usd:,.2f}")
st.divider()
st.metric("💵 Total Portfolio Value", f"${total_usd:,.2f}")

st.caption("Prices from CoinGecko • Data via Alchemy RPC")