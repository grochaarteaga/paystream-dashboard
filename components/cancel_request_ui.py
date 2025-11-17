import streamlit as st
from utils.wallet import get_wallet_address
from utils.requests import get_request, cancel_payment_request

def show_cancel_request_ui():
    st.subheader("Cancel an existing request")

    payer = get_wallet_address()
    st.text_input("Your wallet", value=payer, disabled=True, key="cancel_req_wallet")

    req_id = st.text_input("Request ID", key="cancel_req_id")

    if st.button("Load Request", key="cancel_req_load"):
        if not req_id.isdigit():
            st.error("Enter a valid ID.")
            return
        req = get_request(int(req_id))
        if not req:
            st.error("Request not found.")
        else:
            st.session_state["cancel_request"] = req

    req = st.session_state.get("cancel_request")
    if req:
        st.write(req)
        if st.button("Cancel request", key="cancel_req_btn"):
            try:
                tx_hash = cancel_payment_request(req["id"])
                st.success(f"Cancelled! {tx_hash}")
                st.markdown(f"https://sepolia.etherscan.io/tx/{tx_hash}")
            except Exception as e:
                st.error(e)
