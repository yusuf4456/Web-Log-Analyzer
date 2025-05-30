import re
from collections import defaultdict
from datetime import timedelta

SQLI_PATTERNS = [r"(\bUNION\b|\bSELECT\b|\bINSERT\b|\bUPDATE\b|\bDELETE\b)", r"('|--|%27|%3D)", r"\bOR\b.*\b=\b"]
XSS_PATTERNS = [r"<script.*?>", r"onerror=", r"alert\("]

def detect_sqli(path):
    return any(re.search(p, path, re.IGNORECASE) for p in SQLI_PATTERNS)

def detect_xss(path):
    return any(re.search(p, path, re.IGNORECASE) for p in XSS_PATTERNS)

def detect_brute_force(logs, threshold=10, time_window=timedelta(minutes=1)):
    brute_ips = set()
    failed_attempts = defaultdict(list)
    for log in logs:
        if log["status"] in (401, 403):
            failed_attempts[log["ip"]].append(log["datetime"])
    for ip, times in failed_attempts.items():
        times.sort()
        for i in range(len(times) - threshold + 1):
            if times[i + threshold - 1] - times[i] <= time_window:
                brute_ips.add(ip)
                break
    return brute_ips

def detect_abnormal_rate(logs, rate_threshold=100):
    ip_counter = defaultdict(int)
    for log in logs:
        ip_counter[log['ip']] += 1
    return {ip for ip, count in ip_counter.items() if count > rate_threshold}

def analyze_logs(logs):
    findings = []
    brute_force_ips = detect_brute_force(logs)
    high_rate_ips = detect_abnormal_rate(logs)
    for log in logs:
        tags = []
        if detect_sqli(log['path']):
            tags.append("SQLi")
        if detect_xss(log['path']):
            tags.append("XSS")
        if log['ip'] in brute_force_ips:
            tags.append("Brute Force")
        if log['ip'] in high_rate_ips:
            tags.append("Abnormal Traffic")
        if tags:
            findings.append({**log, "alerts": tags})
    return findings
