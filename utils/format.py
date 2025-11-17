def format_usdc(amount_wei: int, decimals: int = 6) -> str:
    human = amount_wei / (10 ** decimals)
    return f"{human:,.2f} USDC"


def short_address(addr: str, chars: int = 4) -> str:
    if not addr or len(addr) < 2 * chars + 2:
        return addr
    return f"{addr[:2 + chars]}…{addr[-chars:]}"


def etherscan_tx(tx_hash: str, network: str = "sepolia") -> str:
    """
    Returns a markdown link to Etherscan, making sure the 0x prefix is preserved.
    """
    if not tx_hash.startswith("0x"):
        tx_hash = "0x" + tx_hash

    if network == "sepolia":
        base = "https://sepolia.etherscan.io/tx/"
    else:
        base = "https://etherscan.io/tx/"

    return f"[View on Etherscan]({base}{tx_hash})"
