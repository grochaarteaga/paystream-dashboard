import os
import json
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

SEPOLIA_RPC_URL = os.getenv("SEPOLIA_RPC_URL")
if not SEPOLIA_RPC_URL:
    raise ValueError("SEPOLIA_RPC_URL is not set in .env")

w3 = Web3(Web3.HTTPProvider(SEPOLIA_RPC_URL))
if not w3.is_connected():
    raise ConnectionError("Web3 is NOT connected. Check RPC URL.")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ABI_DIR = os.path.join(BASE_DIR, "abi")

def _load_abi(filename: str):
    path = os.path.join(ABI_DIR, filename)
    with open(path) as f:
        data = json.load(f)
    return data["abi"]

PAYSTREAM_ADDRESS = os.getenv("PAYSTREAM_ADDRESS")
MOCKUSDC_ADDRESS = os.getenv("MOCKUSDC_ADDRESS")

paystream_abi = _load_abi("PayStream.json")
usdc_abi = _load_abi("MockUSDC.json")

paystream_contract = w3.eth.contract(
    address=PAYSTREAM_ADDRESS,
    abi=paystream_abi
)

usdc_contract = w3.eth.contract(
    address=MOCKUSDC_ADDRESS,
    abi=usdc_abi
)
