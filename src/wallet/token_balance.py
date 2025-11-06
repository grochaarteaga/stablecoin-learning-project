from web3 import Web3
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Connect to Alchemy
alchemy_url = os.getenv("ALCHEMY_URL")
w3 = Web3(Web3.HTTPProvider(alchemy_url))

if not w3.is_connected():
    print("❌ Connection failed.")

    exit()

# USDC Sepolia contract address
usdc_contract = "0x68194a729C2450ad26072b3D33ADaCbcef39D574"


# Minimal ABI to call ERC-20 functions: balanceOf, decimals, symbol
erc20_abi = [
    {"constant": True, "inputs": [], "name": "symbol", "outputs": [{"name": "", "type": "string"}], "type": "function"},
    {"constant": True, "inputs": [], "name": "decimals", "outputs": [{"name": "", "type": "uint8"}], "type": "function"},
    {"constant": True, "inputs": [{"name": "_owner", "type": "address"}], "name": "balanceOf", "outputs": [{"name": "balance", "type": "uint256"}], "type": "function"},
]

# Create contract instance
contract = w3.eth.contract(
    address=w3.to_checksum_address(usdc_contract),
    abi=erc20_abi
)


# Wallet address (your MetaMask)
wallet_address = os.getenv("SENDER_ADDRESS")

# Call contract functions
symbol = contract.functions.symbol().call()
decimals = contract.functions.decimals().call()
balance = contract.functions.balanceOf(wallet_address).call() / (10 ** decimals)

print(f"🪙 Token: {symbol}")
print(f"💰 Address: {wallet_address}")
print(f"Balance: {balance} {symbol}")