from web3 import Web3
import os
from dotenv import load_dotenv

load_dotenv()

alchemy_url = os.getenv("ALCHEMY_URL")
w3 = Web3(Web3.HTTPProvider(alchemy_url))

if not w3.is_connected():
    print("❌ Connection failed.")
    exit()

# ERC-20 DAI contract on Sepolia
token_address = "0x68194a729C2450ad26072b3D33ADaCbcef39D574"
token_address = w3.to_checksum_address(token_address)

# Minimal ABI with transfer function
erc20_abi = [
    {
        "constant": False,
        "inputs": [
            {"name": "_to", "type": "address"},
            {"name": "_value", "type": "uint256"}
        ],
        "name": "transfer",
        "outputs": [{"name": "success", "type": "bool"}],
        "type": "function"
    },
    {"constant": True, "inputs": [], "name": "decimals", "outputs": [{"name": "", "type": "uint8"}], "type": "function"},
]

contract = w3.eth.contract(address=token_address, abi=erc20_abi)

sender_private_key = os.getenv("SENDER_PRIVATE_KEY")
sender_address = os.getenv("SENDER_ADDRESS")
receiver_address = os.getenv("RECEIVER_ADDRESS")

# Convert amount to token units
decimals = contract.functions.decimals().call()
amount = int(0.1 * 10 ** decimals)  # send 0.1 DAI

# Build transaction
nonce = w3.eth.get_transaction_count(sender_address)
tx = contract.functions.transfer(receiver_address, amount).build_transaction({
    "chainId": 11155111,      # Sepolia
    "gas": 100000,
    "gasPrice": w3.eth.gas_price,
    "nonce": nonce,
})

# Sign and send
signed_tx = w3.eth.account.sign_transaction(tx, private_key=sender_private_key)
tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)

print(f"🚀 Token transfer submitted! Hash: {w3.to_hex(tx_hash)}")
print("🔍 View on Etherscan: https://sepolia.etherscan.io/tx/" + w3.to_hex(tx_hash))