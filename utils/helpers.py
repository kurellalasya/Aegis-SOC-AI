import os
from datetime import datetime

def save_report(report_content):
    # This line checks if the folder exists, and creates it if it doesn't
    if not os.path.exists("reports"):
        os.makedirs("reports")
        
    filename = f"reports/Incident_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    
    with open(filename, "w") as f:
        f.write(report_content)
    
    return filename