# ❌ This is insecure and violates multiple rules
import sqlite3

user_input = "1 OR 1=1"  
query = "SELECT * FROM users WHERE id = " + user_input  # SQL injection risk

# Hardcoded secret
API_KEY = "12345-SECRET-HARDCODED"

# Dangerous eval
result = eval("2 + 2")  

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute(query)  # Vulnerable to SQL injection
