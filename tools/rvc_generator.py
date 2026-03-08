#!/usr/bin/env python3
"""
Requirement vs. Capability (RvC) Generator
------------------------------------------
Parses embedded C firmware test execution logs and cross-references them against
the technical baseline REQUIREMENTS.md to generate a DO-254 compliant compliance matrix.
"""

import re
import json
import sys
from pathlib import Path

def parse_requirements(req_path: str) -> dict:
    """Parses markdown tables to extract Requirement IDs and text."""
    reqs = {}
    if not Path(req_path).exists():
        return reqs
        
    with open(req_path, 'r') as f:
        for line in f:
            # Match markdown table rows containing REQ-
            match = re.search(r'\|\s*`(REQ-[A-Z]+-\d+)`\s*\|\s*(.*?)\s*\|', line)
            if match:
                req_id = match.group(1)
                req_text = match.group(2).strip()
                reqs[req_id] = {"text": req_text, "status": "UNTESTED", "log_evidence": None}
    return reqs

def ingest_test_logs(log_path: str, req_db: dict):
    """Scans hardware-in-the-loop (HIL) test logs for requirement verification markers."""
    if not Path(log_path).exists():
        return
        
    with open(log_path, 'r') as f:
        for line in f:
            # Look for lines like: [PASS] Verification of REQ-GYRO-001 completed in 2ms.
            match = re.search(r'\[(PASS|FAIL)\] Verification of (REQ-[A-Z]+-\d+)(.*)', line)
            if match:
                status = match.group(1)
                req_id = match.group(2)
                evidence = match.group(3).strip()
                
                if req_id in req_db:
                    req_db[req_id]["status"] = status
                    req_db[req_id]["log_evidence"] = evidence

def generate_rvc_report(req_db: dict, output_path: str):
    """Generates the final JSON compliance matrix."""
    tested = sum(1 for r in req_db.values() if r["status"] != "UNTESTED")
    passed = sum(1 for r in req_db.values() if r["status"] == "PASS")
    total = len(req_db)
    
    report = {
        "metadata": {
            "total_requirements": total,
            "coverage_percent": (tested / total * 100) if total > 0 else 0,
            "pass_rate": (passed / total * 100) if total > 0 else 0
        },
        "compliance_matrix": req_db
    }
    
    with open(output_path, 'w') as f:
        json.dump(report, f, indent=2)
    print(f"RvC Matrix generated: {output_path} (Coverage: {report['metadata']['coverage_percent']:.1f}%)")

if __name__ == "__main__":
    REQ_FILE = "docs/REQUIREMENTS.md"
    LOG_FILE = "logs/hil_test_execution.log"
    OUT_FILE = "rvc_compliance_matrix.json"
    
    print("Initializing DO-254 RvC Generator...")
    db = parse_requirements(REQ_FILE)
    ingest_test_logs(LOG_FILE, db)
    generate_rvc_report(db, OUT_FILE)
