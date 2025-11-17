import streamlit as st
from utils.wallet import get_wallet_address
from utils.usdc import approve_spender

def show_approve_tokens_ui():
    st.subheader("Approve PayStream to spend your USDC")

    addr = get_wallet_address()
    st.text_input("Your wallet", value=addr, disabled=True, key="approve_tokens_wallet")

    amount = st.text_input("Allowance amount (USDC)", key="approve_tokens_amount")

    if st.button("Approve USDC Spending", key="approve_tokens_btn"):
        if not amount.isdigit():
            st.error("Amount must be number.")
            return
        onchain = int(amount) * 1_000_000
        try:
            tx_hash = approve_spender(onchain)
            st.success(f"Approved! {tx_hash}")
            st.markdown(f"https://sepolia.etherscan.io/tx/{tx_hash}")
        except Exception as e:
            st.error(e)
