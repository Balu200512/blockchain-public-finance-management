# Blockchain-Enabled Public Finance Management System

## 1. Project Overview

The Blockchain-Enabled Public Finance Management System is a web-based application designed to demonstrate transparency, accountability, and integrity in the management of public funds.

The system simulates the process of submitting departmental fund requests, reviewing requests, approving or rejecting allocations, recording fund utilization, and maintaining a blockchain-style audit ledger.

Developed using Python, Flask, HTML, CSS, and SHA-256 hashing, the project demonstrates how linked records can help identify unauthorized modifications to transaction history.

**Project Type:** Academic / Educational Prototype

## 2. Problem Statement

Traditional public finance workflows can face challenges related to record transparency, tracking fund allocation, maintaining audit trails, and identifying changes to transaction records.

This project demonstrates a digital workflow for managing sample fund requests and recording important actions in a hash-linked ledger. It provides a dashboard for viewing requests and an audit page for inspecting recorded blocks.

## 3. Project Objectives

- Develop a web interface for departmental fund requests.
- Demonstrate approval and rejection workflows.
- Record request, decision, and utilization events in a linked ledger.
- Calculate block hashes using SHA-256.
- Verify links between blocks to detect changes to recorded data.
- Display fund allocation and utilization summaries.
- Provide an audit page for reviewing ledger records.

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Flask | Web framework and routing |
| HTML5 | Web page structure |
| CSS3 | Dashboard styling and responsive layout |
| SHA-256 | Block hash calculation |
| JSON | Consistent serialization of block data |
| Jinja2 | Rendering dynamic HTML templates |

## 5. Main Features

### 5.1 Fund Request Management

Departments can submit sample fund requests by specifying:
- Department name
- Purpose of the request
- Requested amount

The system validates the submitted information and adds valid requests to the request register.

### 5.2 Verification and Approval

A submitted request initially receives a **Pending** status. The demonstration interface allows a request to be approved or rejected.

The decision is recorded as a new entry in the blockchain-style ledger.

**Note:** This prototype does not implement real user authentication or enforce official authorization.

### 5.3 Blockchain-Style Record Keeping

Each block contains:
- Block index
- Timestamp
- Transaction or event data
- Previous block hash
- Current block hash

The current hash is calculated using SHA-256 over the serialized block data. Each new block references the hash of the preceding block.

### 5.4 Fund Allocation Tracking

The dashboard calculates the total amount requested by approved departments and the amount of utilization recorded against those allocations.

Utilization entries are accepted only for approved requests and cannot exceed the approved allocation.

### 5.5 Audit Ledger

The audit page displays block details, including:
- Recorded event
- Timestamp
- Previous hash
- Current hash

The application checks whether stored block hashes match their contents and whether previous-hash links match the preceding blocks.

## 6. System Architecture

The application uses a simple layered structure:

1. **Presentation Layer:** HTML templates and CSS provide the dashboard and audit interface.
2. **Application Layer:** Flask handles HTTP requests, form submissions, and page rendering.
3. **Business Logic Layer:** Python classes manage requests, decisions, utilization, and block creation.
4. **Ledger Layer:** SHA-256 hashes and previous-block references provide basic integrity checks.

### Workflow

```text
Department submits fund request
              |
              v
      Request validation
              |
              v
      Pending request
              |
              v
    Approve or reject
              |
              v
     Record event in ledger
              |
              v
 Approved allocation tracking
              |
              v
    Utilization and audit
```

## 7. Project Structure

```text
blockchain-public-finance-management/
│
├── app.py
├── finance_chain.py
├── requirements.txt
├── README.md
│
├── templates/
│   ├── index.html
│   └── audit.html
│
└── static/
    └── style.css
```

### File Descriptions

- `app.py` — Flask application, dashboard routes, request submission, decisions, and utilization.
- `finance_chain.py` — Block structure, SHA-256 hashing, ledger management, and chain integrity checks.
- `requirements.txt` — Python package dependencies.
- `templates/index.html` — Dashboard, fund request form, and request register.
- `templates/audit.html` — Blockchain ledger and audit information.
- `static/style.css` — Styling, responsive layouts, cards, tables, and status indicators.
- `README.md` — Project documentation and setup instructions.

## 8. Installation Requirements

- Python 3.10 or later
- Visual Studio Code or another Python editor
- A modern web browser
- Internet connection for installing Flask, if it is not already installed

## 9. Installation and Setup

### Step 1: Clone the repository

Replace the repository URL below with your actual GitHub repository URL if necessary.

```bash
git clone https://github.com/Balu200512/blockchain-public-finance-management.git
```

### Step 2: Open the project directory

```bash
cd blockchain-public-finance-management
```

### Step 3: Create a virtual environment (recommended)

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

If PowerShell activation is unavailable, use Command Prompt:

```bat
.venv\Scripts\activate.bat
```

### Step 4: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Run the application

```bash
python app.py
```

### Step 6: Open the website

Visit the following address in your browser:

`http://127.0.0.1:5000`

Keep the terminal open while using the application.

## 10. How to Use the Application

1. Open the dashboard in your browser.
2. Select a department.
3. Enter the purpose and requested amount.
4. Submit the fund request.
5. Use the demonstration controls to approve or reject the pending request.
6. For an approved request, record a utilization amount.
7. Review the dashboard totals.
8. Open the Audit Ledger page to inspect recorded blocks and the chain integrity status.

Use only sample information when testing the project.

## 11. Validation and Integrity Checks

The ledger performs two main checks:

- **Content integrity:** Recalculates each block hash and compares it with the stored hash.
- **Chain linkage:** Checks that each block references the previous block's stored hash.

These checks can identify many accidental or unauthorized changes to existing block data. However, they do not provide complete security against an attacker who can modify the entire ledger and recalculate its hashes.

## 12. Advantages

- Demonstrates a blockchain-inspired record-keeping workflow.
- Provides a clear interface for tracking sample requests.
- Records important actions in a linked ledger.
- Includes basic record integrity checks.
- Demonstrates Python, Flask, HTML, and CSS integration.
- Provides an audit view for inspecting transaction history.

## 13. Limitations

This implementation is an educational prototype and has important limitations:

- Data is stored in memory and resets when the application restarts.
- No database is configured for persistent records.
- No login system or role-based authorization is implemented.
- The blockchain is not distributed across multiple computers.
- It does not implement real distributed consensus.
- Hash linking does not guarantee immutability against all forms of tampering.
- The interface does not connect to real government finance systems or payment services.
- No real financial or personal information should be entered.

## 14. Future Enhancements

Possible improvements include:

- Integrating SQLite or PostgreSQL for persistent storage.
- Adding secure authentication and role-based permissions.
- Implementing digital signatures for approval records.
- Building a multi-node ledger with a defined consensus protocol.
- Adding CSV or PDF audit report exports.
- Providing detailed fund utilization charts.
- Adding automated tests and stronger input validation.
- Deploying the application in a properly secured environment.

## 15. Learning Outcomes

This project demonstrates practical experience with:
- Python object-oriented programming
- Flask routes and form handling
- HTML and CSS frontend development
- Hash functions and linked records
- Transaction validation and audit workflows
- Basic integrity verification
- Organizing a multi-file software project

## 16. Author

**Balu200512**

GitHub: https://github.com/Balu200512

## 17. Conclusion

The Blockchain-Enabled Public Finance Management System demonstrates how a web application can combine fund request workflows, approval tracking, utilization records, and hash-linked audit history.

The project provides a foundation for learning about blockchain-inspired record integrity and public finance transparency. Additional database, security, authentication, and distributed-consensus components would be required before it could be considered for real-world use.
