from utils.chains import w3, usdc_contract, PAYSTREAM_ADDRESS
from utils.wallet import get_wallet_address, build_tx, sign_and_send


DECIMALS = 1_000_000  # USDC decimals = 6


def get_usdc_balance(address: str):
    """Returns human USDC balance."""
    try:
        raw = usdc_contract.functions.balanceOf(address).call()
        return raw / DECIMALS
    except Exception as e:
        print("Error in get_usdc_balance:", e)
        return 0


def get_allowance(owner: str, spender: str):
    """Returns human readable allowance amount."""
    try:
        raw = usdc_contract.functions.allowance(owner, spender).call()
        return raw / DECIMALS
    except Exception as e:
        print("Error in get_allowance:", e)
        return 0


def approve_spender(amount: int, spender: str = PAYSTREAM_ADDRESS):
    """
    Approve a spender to use your USDC.
    Input amount must be raw (e.g., 5 USDC = 5_000_000).
    """
    addr = get_wallet_address()

    try:
        tx = usdc_contract.functions.approve(
            spender,
            amount
        ).build_transaction(
            build_tx(w3, addr)
        )

        tx_hash = sign_and_send(w3, tx)
        return tx_hash

    except Exception as e:
        print("Error in approve_spender:", e)
        raise
