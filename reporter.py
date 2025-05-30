import json
import csv

def write_json(findings, filename="output.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(findings, f, ensure_ascii=False, indent=2, default=str)

def write_csv(findings, filename="output.csv"):
    if not findings:
        return
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=findings[0].keys())
        writer.writeheader()
        writer.writerows(findings)
