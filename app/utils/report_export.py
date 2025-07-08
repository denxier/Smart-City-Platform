import pandas as pd
from weasyprint import HTML

def generate_environment_pdf(csv_path):
    df = pd.read_csv(csv_path)
    html = "<h1>Environmental Report</h1><table border='1' cellspacing='0' cellpadding='5'>"
    html += "<tr><th>Timestamp</th><th>Air</th><th>Water</th><th>Noise</th></tr>"

    for _, row in df.iterrows():
        html += f"<tr><td>{row['timestamp']}</td><td>{row['air_quality']}</td><td>{row['water_quality']}</td><td>{row['noise_level']}</td></tr>"

    html += "</table>"
    pdf_path = "data/environment_report.pdf"
    HTML(string=html).write_pdf(pdf_path)
    return pdf_path
