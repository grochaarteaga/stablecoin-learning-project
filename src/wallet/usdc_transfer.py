from web3 import Web3
import os
from dotenv import load_dotenv

load_dotenv()

# --- Connect to Ethereum Mainnet ---
alchemy_url = os.getenv("ALCHEMY_URL_MAINNET")
w3 = Web3(Web3.HTTPProvider(alchemy_url))

sender = os.getenv("SENDER_ADDRESS")
receiver = os.getenv("RECEIVER_ADDRESS")
private_key = os.getenv("SENDER_PRIVATE_KEY")

# --- USDC contract on Ethereum Mainnet ---
usdc_contract = w3.to_checksum_address("0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48")

erc20_abi = [
    {"constant": True, "inputs": [], "name": "decimals",
     "outputs": [{"name": "", "type": "uint8"}], "type": "function"},
    {"constant": False, "inputs": [
        {"name": "_to", "type": "address"},
        {"name": "_value", "type": "uint256"}],
     "name": "transfer",
     "outputs": [{"name": "success", "type": "bool"}],
     "type": "function"},
]

contract = w3.eth.contract(address=usdc_contract, abi=erc20_abi)
decimals = contract.functions.decimals().call()

# --- Amount: 0.5 USDC ---
amount = int(0.5 * (10 ** decimals))

# --- Build the transaction ---
nonce = w3.eth.get_transaction_count(sender)
tx = contract.functions.transfer(receiver, amount).build_transaction({
    "chainId": 1,  # Ethereum Mainnet
    "gas": 100000,  # gas limit
    "gasPrice": w3.eth.gas_price,
    "nonce": nonce,
})

# --- Sign transaction locally ---
signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)

# --- Send transaction ---
tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
print(f"🚀 USDC transfer submitted! Hash: {tx_hash.hex()}")
print(f"🔍 View on Etherscan: https://etherscan.io/tx/{tx_hash.hex()}")