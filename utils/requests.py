from utils.chains import w3, paystream_contract
from utils.wallet import get_wallet_address, build_tx, sign_and_send

STATUS_MAP = {
    0: "Pending",
    1: "Approved",
    2: "Cancelled"
}

def create_payment_request(payee: str, amount: int):
    """Creates a new payment request and returns (request_id, tx_hash)."""

    addr = get_wallet_address()

    # Build tx
    tx = paystream_contract.functions.createRequest(payee, amount).build_transaction(
        build_tx(w3, addr)
    )

    # Send tx
    tx_hash = sign_and_send(w3, tx)

    # Wait for receipt
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    # Parse RequestCreated event
    event_signature = w3.keccak(
        text="RequestCreated(uint256,address,address,uint256,uint8)"
    ).hex()

    request_id = None

    for log in receipt.logs:
        if log["topics"][0].hex() == event_signature:
            # topics = [sig, id, payer, payee]
            request_id = int(log["topics"][1].hex(), 16)

    return request_id, tx_hash


def approve_payment_request(request_id: int):
    addr = get_wallet_address()
    tx = paystream_contract.functions.approveRequest(request_id).build_transaction(
        build_tx(w3, addr)
    )
    return sign_and_send(w3, tx)


def cancel_payment_request(request_id: int):
    addr = get_wallet_address()
    tx = paystream_contract.functions.cancelRequest(request_id).build_transaction(
        build_tx(w3, addr)
    )
    return sign_and_send(w3, tx)


def get_request(request_id: int):
    try:
        raw = paystream_contract.functions.requests(request_id).call()

        # Check if request exists
        if raw[1] == "0x0000000000000000000000000000000000000000":
            return None

        amount_human = raw[3] / 1_000_000

        return {
            "id": raw[0],
            "payer": raw[1],
            "payee": raw[2],
            "amount_raw": raw[3],
            "amount_human": amount_human,
            "status": STATUS_MAP.get(raw[4], "Unknown")
        }
    except Exception as e:
        print("Error in get_request:", e)
        return None
