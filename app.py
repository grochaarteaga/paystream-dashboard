import streamlit as st

from components.create_request_ui import show_create_request_ui
from components.approve_request_ui import show_approve_request_ui
from components.approve_tokens_ui import show_approve_tokens_ui
from components.view_request_ui import show_view_request_ui
from components.cancel_request_ui import show_cancel_request_ui

st.set_page_config(
    page_title="PayStream Dashboard",
    page_icon="💸",
    layout="centered"
)

st.title("💸 PayStream – On-chain Payment Requests")
st.caption("Create, approve, cancel, and inspect MockUSDC payment requests on Sepolia.")

tabs = st.tabs([
    "Create Request",
    "Approve Request",
    "Approve Tokens",
    "View Request",
    "Cancel Request"
])

with tabs[0]:
    show_create_request_ui()

with tabs[1]:
    show_approve_request_ui()

with tabs[2]:
    show_approve_tokens_ui()

with tabs[3]:
    show_view_request_ui()

with tabs[4]:
    show_cancel_request_ui()
