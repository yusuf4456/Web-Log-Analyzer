from log_parser import parse_log_line
from detector import analyze_logs
from reporter import write_json, write_csv

logs = []
with open("access.log", "r", encoding="utf-8") as f:
    for line in f:
        parsed = parse_log_line(line)
        if parsed:
            logs.append(parsed)

findings = analyze_logs(logs)

write_json(findings)
write_csv(findings)

for i in findings:
    print(i)
