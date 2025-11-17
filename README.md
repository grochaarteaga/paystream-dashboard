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

🔧 Environment variables

Create a .env file:

PRIVATE_KEY=0x...
SEPOLIA_RPC_URL=https://...
PAYSTREAM_ADDRESS=0x...
MOCKUSDC_ADDRESS=0x...


Never commit your .env file.

▶️ Run the dashboard
streamlit run app.py

📘 Smart Contract

The project uses two ABI files:

abi/PayStream.json

abi/MockUSDC.json

These ABIs define how Python interacts with the contracts.

🧩 Architecture
components/   → UI tabs
utils/         → All blockchain logic
abi/           → Contract ABIs
app.py         → Main Streamlit launcher

🏆 What I Learned

ERC-20 allowance mechanics

transferFrom pipeline

Event logs decoding

How on-chain payments work

EIP-1559 transaction fields

Streamlit UI development

Good smart contract UX practices

🛠 Future Improvements

Request history table

Real-time event log viewer

Support for other stablecoins (DAI/USDT)

Privy login instead of private key

Store requests in a database (Supabase)

🤝 Contributing

Pull requests are welcome!
This is a learning project — feel free to fork it and build your own version.

📬 Contact

If you're curious about stablecoin applications or B2B payments, feel free to reach out.


---

# ⭐ 5. **Push to GitHub — Step by Step**

### 1️⃣ Initialize repo

```bash
cd paystream-dashboard
git init

2️⃣ Add files
git add .


(Be sure .env is ignored.)

3️⃣ Commit
git commit -m "Initial commit: PayStream dashboard"

4️⃣ Create GitHub repo

Go to:

👉 https://github.com/new

Name it: paystream-dashboard

5️⃣ Add remote
git remote add origin https://github.com/YOUR_USERNAME/paystream-dashboard.git

6️⃣ Push
git push -u origin main