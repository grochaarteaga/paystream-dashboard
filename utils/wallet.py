from eth_account import Account
from dotenv import load_dotenv
import os

load_dotenv()

# ---- Load private key ----
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
if not PRIVATE_KEY:
    raise ValueError("PRIVATE_KEY missing in .env")


def get_wallet_address():
    """Returns the address derived from the private key."""
    return Account.from_key(PRIVATE_KEY).address


def build_tx(w3, from_addr, gas=300000):
    """
    Build a correct EIP-1559 transaction dictionary for Sepolia.
    """
    try:
        nonce = w3.eth.get_transaction_count(from_addr)

        # EIP-1559 gas fields
        current_gas = w3.eth.gas_price
        max_fee = current_gas * 2
        max_priority = int(current_gas * 0.1)

        return {
            "from": from_addr,
            "nonce": nonce,
            "gas": gas,
            "maxFeePerGas": max_fee,
            "maxPriorityFeePerGas": max_priority,
            "chainId": 11155111,  # Sepolia chain ID
        }

    except Exception as e:
        print("Error in build_tx:", e)
        raise


def sign_and_send(w3, tx):
    """
    Signs and broadcasts a transaction, returns a valid 0x-prefixed hash.
    """
    try:
        signed = w3.eth.account.sign_transaction(tx, PRIVATE_KEY)
        tx_hash = w3.eth.send_raw_transaction(signed.raw_transaction)

        # FIX: Add missing "0x" prefix for etherscan compatibility
        return "0x" + tx_hash.hex()

    except Exception as e:
        print("Error in sign_and_send:", e)
        raise
