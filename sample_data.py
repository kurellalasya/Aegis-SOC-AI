ATTACK_SAMPLES = {
    "Brute Force & PrivEsc": """
2026-05-14 22:10:01 Admin login failed from IP 192.168.1.50
2026-05-14 22:10:03 Admin login failed from IP 192.168.1.50
2026-05-14 22:10:08 Admin login successful from IP 192.168.1.50
2026-05-14 22:11:00 user 'admin' modified /etc/shadow
""",
    "SQL Injection Attempt": """
2026-05-14 14:05:22 GET /login.php?user=admin' OR '1'='1
2026-05-14 14:05:25 404 Error: Table 'users_db' not found
2026-05-14 14:06:01 POST /api/v1/query data="UNION SELECT password FROM admins"
""",
    "Suspicious Data Exfiltration": """
2026-05-14 09:00:15 Internal user 'dev_01' accessing /secure_vault/keys.zip
2026-05-14 09:05:44 Outbound connection to 45.33.12.9 (RU) - 4.5GB transferred
2026-05-14 09:10:00 Task Scheduler modified: 'run_backup.exe'
"""
}