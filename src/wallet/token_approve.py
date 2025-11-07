from web3 import Web3
import os
from dotenv import load_dotenv

load_dotenv()

alchemy_url = os.getenv("ALCHEMY_URL")
w3 = Web3(Web3.HTTPProvider(alchemy_url))

if not w3.is_connected():
    print("❌ Connection failed.")
    exit()

# ERC-20 DAI on Sepolia
token_address = "0x68194a729C2450ad26072b3D33ADaCbcef39D574"
token_address = w3.to_checksum_address(token_address)

# ABI with approve and allowance
erc20_abi = [
    {
        "constant": False,
        "inputs": [
            {"name": "_spender", "type": "address"},
            {"name": "_value", "type": "uint256"}
        ],
        "name": "approve",
        "outputs": [{"name": "success", "type": "bool"}],
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {"name": "_owner", "type": "address"},
            {"name": "_spender", "type": "address"}
        ],
        "name": "allowance",
        "outputs": [{"name": "remaining", "type": "uint256"}],
        "type": "function"
    },
    {"constant": True, "inputs": [], "name": "decimals", "outputs": [{"name": "", "type": "uint8"}], "type": "function"},
]

contract = w3.eth.contract(address=token_address, abi=erc20_abi)

# Load your wallet details
sender_private_key = os.getenv("SENDER_PRIVATE_KEY")
sender_address = os.getenv("SENDER_ADDRESS")

# Let's pick a random "spender" to approve (imagine this is Uniswap)
spender_address = "0x0000000000000000000000000000000000000001"

# Get decimals
decimals = contract.functions.decimals().call()
amount = int(1 * 10 ** decimals)  # approve 1 DAI

# STEP 1: Build the approve transaction
nonce = w3.eth.get_transaction_count(sender_address)
tx = contract.functions.approve(spender_address, amount).build_transaction({
    "chainId": 11155111,
    "gas": 100000,
    "gasPrice": w3.eth.gas_price,
    "nonce": nonce,
})

# STEP 2: Sign and send
signed_tx = w3.eth.account.sign_transaction(tx, private_key=sender_private_key)
tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)

print(f"✅ Approve transaction sent! Hash: {w3.to_hex(tx_hash)}")
print("🔍 View it on: https://sepolia.etherscan.io/tx/" + w3.to_hex(tx_hash))

# STEP 3: Check allowance (optional)
allowance = contract.functions.allowance(sender_address, spender_address).call() / (10 ** decimals)
print(f"📊 Allowance for spender: {allowance} DAI")