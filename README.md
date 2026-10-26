# Blockchain-Enabled Public Finance Management System

An educational web application that simulates public fund requests, review decisions, approved fund allocation, utilization tracking, and an append-only hash-linked audit ledger.

## Features
- Department fund requests
- Approve/reject workflow demonstration
- Hash-linked blockchain-style ledger
- Approved fund allocation and utilization dashboard
- Audit trail and basic chain integrity check

## Technology
- Python
- Flask
- HTML5 / CSS3
- SHA-256 hashing (Python `hashlib`)

## Run locally
1. Install Python 3.10 or later.
2. Open a terminal in this folder.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the app:
   ```bash
   python app.py
   ```
5. Open `http://127.0.0.1:5000` in your browser.

## Important limitations
This is a classroom prototype, not a production finance platform. It stores data in memory, so data resets when the server restarts. It has no real authentication, role-based authorization, database, digital signatures, distributed consensus, or production security. Approval controls are demonstration-only. Do not use real financial or personal data.
