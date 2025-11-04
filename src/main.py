from web3 import Web3
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Connect to Alchemy Sepolia node
alchemy_url = os.getenv("ALCHEMY_URL")
w3 = Web3(Web3.HTTPProvider(alchemy_url))

# Check connection
if w3.is_connected():
    print("✅ Connected to Ethereum Sepolia testnet!")
    latest_block = w3.eth.block_number
    print(f"Current block number: {latest_block}")
else:
    print("❌ Connection failed. Check your API key or network.")
