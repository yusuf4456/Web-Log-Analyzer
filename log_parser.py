import re
from datetime import datetime

log_pattern = re.compile(
    r'(?P<ip>\S+) \S+ \S+ \[(?P<datetime>[^\]]+)\] "(?P<method>\S+)? (?P<path>\S+)? \S+" (?P<status>\d{3}) \S+ "(?P<referrer>[^"]*)" "(?P<user_agent>[^"]*)"'
)

def parse_log_line(line):
    match = log_pattern.match(line)
    if match:
        return {
            'ip': match.group('ip'),
            'datetime': datetime.strptime(match.group('datetime'), "%d/%b/%Y:%H:%M:%S %z"),
            'method': match.group('method'),
            'path': match.group('path'),
            'status': int(match.group('status')),
            'user_agent': match.group('user_agent'),
        }
    return None
