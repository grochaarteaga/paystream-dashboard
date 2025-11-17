import streamlit as st
from utils.wallet import get_wallet_address
from utils.requests import get_request, approve_payment_request
from utils.usdc import get_allowance
from utils.chains import PAYSTREAM_ADDRESS
from utils.usdc import approve_spender


def show_approve_request_ui():
    st.subheader("Approve a payment request")

    payer = get_wallet_address()
    st.text_input("Your wallet (payer)", value=payer, disabled=True)

    req_id = st.text_input("Request ID", placeholder="Enter request ID")

    # Load request
    if st.button("Load Request"):
        if not req_id.isdigit():
            st.error("Invalid ID.")
            return

        req = get_request(int(req_id))

        if not req:
            st.error("Request not found.")
            return

        st.session_state["approve_request"] = req

    req = st.session_state.get("approve_request")

    if not req:
        return

    # ---- Show request details ----
    st.markdown("### Request Details")
    st.write(f"**ID:** {req['id']}")
    st.write(f"**Payer:** {req['payer']}")
    st.write(f"**Payee:** {req['payee']}")
    st.write(f"**Amount:** {req['amount_human']} USDC")
    st.write(f"**Status:** {req['status']}")

    # ---- Check allowance ----
    st.markdown("---")
    st.markdown("### Token Allowance Check")

    allowance = get_allowance(req["payer"], PAYSTREAM_ADDRESS)

    st.info(f"Current Allowance: **{allowance} USDC**")

    # Does not have enough allowance
    if allowance < req["amount_human"]:
        st.error(
            f"❌ Not enough USDC allowance.\n\n"
            f"Required: **{req['amount_human']} USDC**\n"
            f"Approved: **{allowance} USDC**"
        )

        # Help user fix it directly
        if st.button("Approve Tokens First (USDC → PayStream)"):
            amount_raw = int(req["amount_raw"])
            with st.spinner("Submitting approval transaction..."):
                tx_hash = approve_spender(amount_raw)
            st.success(f"Allowance approved! TX: {tx_hash}")
            st.markdown(f"[View on Etherscan](https://sepolia.etherscan.io/tx/{tx_hash})")

        return  # stop here, don't show Approve Request button

    # ---- Approve Request button (only shown if allowance OK) ----
    st.success("You have enough allowance to approve this request.")

    if st.button("Approve this Request"):
        try:
            with st.spinner("Processing approval..."):
                tx_hash = approve_payment_request(req["id"])

            st.success(f"Request approved! TX: {tx_hash}")
            st.markdown(f"[View on Etherscan](https://sepolia.etherscan.io/tx/{tx_hash})")

        except Exception as e:
            st.error(f"❌ Transaction failed: {e}")
