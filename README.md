# 💸 PayStream – On-chain Payment Request Dashboard

This project is a Streamlit dashboard that interacts with a custom smart contract called **PayStream** deployed on **Ethereum Sepolia**.

It allows users to:

- Create payment requests (Payee + USDC amount)
- Approve USDC spending (ERC-20 `approve`)
- Approve a payment request on-chain (pulls USDC)
- View payment request details
- Cancel requests

The goal is to learn:

✔ Smart contract interaction  
✔ ERC-20 allowances  
✔ Signing & sending transactions  
✔ Event parsing (`RequestCreated`)  
✔ Using Python + Web3 + Streamlit  
✔ Building small B2B stablecoin prototypes  

---

## 🚀 Features

- Request creation with automatic extraction of the Request ID
- Real-time Etherscan links
- Allowance validation (prevents failing transactions)
- Safe EIP-1559 transaction signing (Sepolia)
- Clean UX with Streamlit tabs
- Session state to remember last created request

---

## 📦 Installation

```bash
git clone https://github.com/YOUR_USERNAME/paystream-dashboard.git
cd paystream-dashboard
pip install -r requirements.txt
