import os
from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from app import db
from app.models.models import CivicIssue

civic_bp = Blueprint('civic', __name__, template_folder='templates')

UPLOAD_FOLDER = 'app/static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@civic_bp.route('/', methods=['GET', 'POST'])
def civic_home():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        photo = request.files.get('photo')

        filename = None
        if photo:
            filename = secure_filename(photo.filename)
            photo.save(os.path.join(UPLOAD_FOLDER, filename))

        issue = CivicIssue(title=title, description=description, photo=filename)
        db.session.add(issue)
        db.session.commit()
        flash('Issue submitted successfully!', 'success')
        return redirect(url_for('civic.civic_home'))

    issues = CivicIssue.query.order_by(CivicIssue.created_at.desc()).all()
    return render_template('civic_issue/civic_home.html', issues=issues)
