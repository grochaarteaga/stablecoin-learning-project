from web3 import Web3
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Connect to the blockchain via Alchemy
alchemy_url = os.getenv("ALCHEMY_URL")
w3 = Web3(Web3.HTTPProvider(alchemy_url))

if not w3.is_connected():
    print("❌ Connection failed.")
    exit()

# Get wallet details from .env
sender_private_key = os.getenv("SENDER_PRIVATE_KEY")
sender_address = os.getenv("SENDER_ADDRESS")
receiver_address = os.getenv("RECEIVER_ADDRESS")

# Transaction parameters
amount_in_ether = 0.01
gas_price = w3.eth.gas_price  # Current gas price
nonce = w3.eth.get_transaction_count(sender_address)

# Build transaction
tx = {
    "nonce": nonce,
    "to": receiver_address,
    "value": w3.to_wei(amount_in_ether, "ether"),
    "gas": 21000,
    "gasPrice": gas_price,
    "chainId": 11155111  # Sepolia chain ID
}

# Sign transaction
signed_tx = w3.eth.account.sign_transaction(tx, private_key=sender_private_key)

# Send transaction
tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)


print(f"🚀 Transaction sent! Hash: {w3.to_hex(tx_hash)}")
print("🔍 View it on: https://sepolia.etherscan.io/tx/" + w3.to_hex(tx_hash))
