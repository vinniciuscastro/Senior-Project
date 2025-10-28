# report.py
from datetime import datetime

def generate_report(result, html=False):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if html:
        with open("report.html", "w") as f:
            f.write(f"""
            <html>
            <head><title>Mutest Report</title></head>
            <body>
                <h1>🧪 Mutest Report</h1>
                <p><strong>Date:</strong> {timestamp}</p>
                <pre>{result}</pre>
            </body>
            </html>
            """)
    else:
        with open("report.txt", "w") as f:
            f.write(f"=== Mutest Report ===\nDate: {timestamp}\n\n{result}\n")
