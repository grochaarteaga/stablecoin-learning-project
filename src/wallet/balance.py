from web3 import Web3
import os
from dotenv import load_dotenv

# Load environment variables (.env file)
load_dotenv()

# Connect to Alchemy Sepolia node
alchemy_url = os.getenv("ALCHEMY_URL")
w3 = Web3(Web3.HTTPProvider(alchemy_url))

# Check connection
if not w3.is_connected():
    print("❌ Connection failed.")
    exit()

# Paste your wallet address from MetaMask
wallet_address = "0xB7C4Eb5F98Fad995E940476711fe0785b66D5851"

# Get balance in Wei
balance_wei = w3.eth.get_balance(wallet_address)

# Convert Wei → Ether
balance_eth = w3.from_wei(balance_wei, "ether")

print(f"💰 Wallet: {wallet_address}")
print(f"Balance: {balance_eth} SepoliaETH")
