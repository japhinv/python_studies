from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)
app.secret_key = "attendance_secret_key"   # 🔐 Required for login session

# ── Database Configuration ──
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///attendance.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ── Database Models ─────────────────────────────
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    roll_no = db.Column(db.String(50), unique=True, nullable=False)

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    date = db.Column(db.Date)
    status = db.Column(db.String(10))

# ── LOGIN ──────────────────────────────────────
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # 🔐 Hardcoded admin credentials
        if username == 'admin' and password == 'admin123':
            session['logged_in'] = True
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="Invalid username or password")

    return render_template('login.html')

# ── LOGOUT ─────────────────────────────────────
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# ── DASHBOARD ──────────────────────────────────
@app.route('/')
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    today = date.today()

    total_students = Student.query.count()

    present_today = Attendance.query.filter_by(
        date=today, status='Present'
    ).count()

    absent_today = Attendance.query.filter_by(
        date=today, status='Absent'
    ).count()

    return render_template(
        'dashboard.html',
        total_students=total_students,
        present_today=present_today,
        absent_today=absent_today
    )

# ── ADD STUDENT ────────────────────────────────
@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    if request.method == 'POST':
        name = request.form['name']
        roll = request.form['roll']

        student = Student(name=name, roll_no=roll)
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('dashboard'))

    return render_template('add_student.html')

# ── MARK ATTENDANCE ────────────────────────────
@app.route('/mark_attendance', methods=['GET', 'POST'])
def mark_attendance():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    students = Student.query.all()
    today = date.today()

    if request.method == 'POST':
        for s in students:
            status = request.form.get(str(s.id))

            # 🔒 Prevent duplicate attendance for same day
            existing = Attendance.query.filter_by(
                student_id=s.id,
                date=today
            ).first()

            if not existing:
                record = Attendance(
                    student_id=s.id,
                    date=today,
                    status=status
                )
                db.session.add(record)

        db.session.commit()
        return redirect(url_for('dashboard'))

    return render_template('mark_attendance.html', students=students)

# ── REPORT ─────────────────────────────────────
@app.route('/report')
def report():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    records = Attendance.query.all()
    return render_template('report.html', records=records)

# ── RUN APP ────────────────────────────────────
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)