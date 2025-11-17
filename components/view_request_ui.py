# components/view_request_ui.py
import streamlit as st
from utils.requests import get_request

def show_view_request_ui():
    st.subheader("View a Payment Request")

    request_id_str = st.text_input(
        "Request ID",
        placeholder="e.g. 1",
    )

    if st.button("View Request"):
        if not request_id_str.isdigit():
            st.error("Request ID must be a number.")
            return

        request_id = int(request_id_str)
        req = get_request(request_id)

        if not req:
            st.error("No request found with this ID.")
            return

        st.markdown("### Request Details")
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**ID**: `{req['id']}`")
            st.write(f"**Payer**: `{req['payer']}`")
            st.write(f"**Payee**: `{req['payee']}`")
        with col2:
            st.write(f"**Amount**: `{req['amount_human']}` USDC")
            st.write(f"**Status**: `{req['status']}`")
