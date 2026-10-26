from flask import Flask, request, redirect, url_for, render_template, flash
from finance_chain import FinanceBlockchain

app = Flask(__name__)
app.secret_key = "change-this-development-secret"
ledger = FinanceBlockchain()

DEPARTMENTS = ["Health", "Education", "Transport", "Water Supply", "Public Works"]

@app.route("/")
def index():
    requests_list = ledger.requests
    approved = [r for r in requests_list if r["status"] == "Approved"]
    pending = [r for r in requests_list if r["status"] == "Pending"]
    allocated = sum(float(r["amount"]) for r in approved)
    spent = sum(float(r["utilized"]) for r in approved)
    return render_template(
        "index.html",
        requests=requests_list,
        pending_count=len(pending),
        approved_count=len(approved),
        allocated=allocated,
        spent=spent,
        departments=DEPARTMENTS,
        chain_valid=ledger.is_chain_valid(),
        blocks=ledger.chain
    )

@app.route("/request", methods=["POST"])
def create_request():
    department = request.form.get("department", "").strip()
    purpose = request.form.get("purpose", "").strip()
    try:
        amount = float(request.form.get("amount", "0"))
    except ValueError:
        amount = 0

    if department not in DEPARTMENTS or not purpose or amount <= 0:
        flash("Enter a valid department, purpose, and positive amount.", "error")
        return redirect(url_for("index"))

    ledger.submit_request(department, purpose, amount)
    flash("Fund request submitted for review.", "success")
    return redirect(url_for("index"))

@app.route("/request/<int:request_id>/decision", methods=["POST"])
def decide_request(request_id):
    decision = request.form.get("decision", "")
    if decision not in ("Approved", "Rejected"):
        flash("Invalid decision.", "error")
    elif ledger.decide_request(request_id, decision):
        flash(f"Request #{request_id} {decision.lower()}.", "success")
    else:
        flash("Request not found or already reviewed.", "error")
    return redirect(url_for("index"))

@app.route("/request/<int:request_id>/utilization", methods=["POST"])
def update_utilization(request_id):
    try:
        amount = float(request.form.get("amount", "0"))
    except ValueError:
        amount = -1

    result = ledger.record_utilization(request_id, amount)
    if result:
        flash("Utilization recorded on the ledger.", "success")
    else:
        flash("Utilization must be positive and cannot exceed the approved allocation.", "error")
    return redirect(url_for("index"))

@app.route("/audit")
def audit():
    return render_template(
        "audit.html",
        blocks=ledger.chain,
        valid=ledger.is_chain_valid()
    )

if __name__ == "__main__":
    app.run(debug=True)
