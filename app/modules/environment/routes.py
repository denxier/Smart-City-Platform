import pandas as pd
from flask import Blueprint, render_template, send_file
from app.utils.report_export import generate_environment_pdf

env_bp = Blueprint('env_bp', __name__, template_folder='templates')

@env_bp.route('/environment')
def environment_dashboard():
    try:
        df = pd.read_csv('data/environment.csv')
        context = {
            "labels_js": df['timestamp'].tolist(),
            "air_js": df['air_quality'].tolist(),
            "water_js": df['water_quality'].tolist(),
            "noise_js": df['noise_level'].tolist()
        }
        return render_template('environment/dashboard.html', **context)
    except Exception as e:
        return f"Error loading CSV: {str(e)}"

@env_bp.route('/environment/export/pdf')
def export_environment_pdf():
    pdf_path = generate_environment_pdf('data/environment.csv')
    return send_file(pdf_path, as_attachment=True)

@env_bp.route('/environment/export/csv')
def export_environment_csv():
    return send_file('data/environment.csv', as_attachment=True)
