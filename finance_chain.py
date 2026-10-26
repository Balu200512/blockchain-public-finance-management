import hashlib
import json
import time


class Block:
    def __init__(self, index, record, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.record = record
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = {
            "index": self.index,
            "timestamp": self.timestamp,
            "record": self.record,
            "previous_hash": self.previous_hash
        }
        payload = json.dumps(data, sort_keys=True, separators=(",", ":"))
        return hashlib.sha256(payload.encode("utf-8")).hexdigest()


class FinanceBlockchain:
    """In-memory teaching demo; data resets when the app restarts."""

    def __init__(self):
        self.chain = []
        self.requests = []
        self.next_id = 1
        self._add_block({"type": "GENESIS", "message": "Public finance ledger created"})

    def _add_block(self, record):
        previous_hash = self.chain[-1].hash if self.chain else "0"
        block = Block(len(self.chain), record, previous_hash)
        self.chain.append(block)
        return block

    def submit_request(self, department, purpose, amount):
        item = {
            "id": self.next_id,
            "department": department,
            "purpose": purpose,
            "amount": round(float(amount), 2),
            "status": "Pending",
            "utilized": 0.0
        }
        self.next_id += 1
        self.requests.append(item)
        self._add_block({"type": "FUND_REQUEST_SUBMITTED", **item})
        return item

    def decide_request(self, request_id, decision):
        item = next((r for r in self.requests if r["id"] == request_id), None)
        if not item or item["status"] != "Pending":
            return False
        item["status"] = decision
        self._add_block({
            "type": "FUND_REQUEST_DECISION",
            "request_id": item["id"],
            "department": item["department"],
            "amount": item["amount"],
            "decision": decision
        })
        return True

    def record_utilization(self, request_id, amount):
        item = next((r for r in self.requests if r["id"] == request_id), None)
        if not item or item["status"] != "Approved" or amount <= 0:
            return False
        new_total = round(item["utilized"] + amount, 2)
        if new_total > item["amount"]:
            return False
        item["utilized"] = new_total
        self._add_block({
            "type": "FUND_UTILIZATION",
            "request_id": item["id"],
            "department": item["department"],
            "amount_recorded": round(amount, 2),
            "total_utilized": new_total
        })
        return True

    def is_chain_valid(self):
        for i, block in enumerate(self.chain):
            if block.hash != block.calculate_hash():
                return False
            if i > 0 and block.previous_hash != self.chain[i - 1].hash:
                return False
        return True
