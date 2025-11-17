import streamlit as st
from utils.wallet import get_wallet_address
from utils.requests import create_payment_request

def show_create_request_ui():
    st.subheader("Create a new payment request")

    payer = get_wallet_address()
    st.text_input(
        "Your wallet address",
        value=payer,
        disabled=True,
        key="create_req_wallet"
    )

    payee = st.text_input(
        "Payee address",
        placeholder="0x...",
        key="create_req_payee"
    )

    amount = st.text_input(
        "Amount (USDC)",
        placeholder="e.g. 50",
        key="create_req_amount"
    )

    if st.button("Create Request", key="create_req_btn"):

        if not payee:
            st.error("Payee is required.")
            return

        if not amount.isdigit():
            st.error("Amount must be a number.")
            return

        onchain_amount = int(amount) * 10**6  # USDC uses 6 decimals

        try:
            with st.spinner("Submitting transaction..."):
                request_id, tx_hash = create_payment_request(payee, onchain_amount)

            if request_id is None:
                st.error("Request created but could not read event logs.")
                st.info(f"Transaction hash: {tx_hash}")
                return

            # Store request ID for auto-fill in the Approve tab
            st.session_state["last_request_id"] = request_id

            st.success(f"✅ Request Created Successfully!")
            st.write(f"**Request ID:** `{request_id}`")

            st.markdown(f"[View on Etherscan](https://sepolia.etherscan.io/tx/{tx_hash})")

            st.info("You can now approve this request in the next tab.")

        except Exception as e:
            st.error(f"Error: {e}")
