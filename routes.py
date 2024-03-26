from flask import  Blueprint,render_template,request,jsonify
from models.student import Student
import uuid
from app import mongo

routes_bp = Blueprint('routes', __name__)




@routes_bp.route('/login')
def login():
    return render_template('login.html')

@routes_bp.route('/signup')
def signup():
    return render_template('signup.html')

@routes_bp.route('/student/profile')
def student():
    return render_template('student-profile.html')

@routes_bp.route('/faculty/profile')
def faculty():
    return render_template('faculty-profile.html')

@routes_bp.route('/contact')
def contact():
    return render_template('contact.html')

@routes_bp.route('/student/payment')
def payment():
    return render_template('payment.html')

@routes_bp.route('/student/TT')
def time_table():
    return render_template('time_table.html')

@routes_bp.route('/student/result')
def result():
    return render_template('result.html')

@routes_bp.route('/faculty/check')
def faculty_check():
    return render_template('faculty-check.html')

@routes_bp.route('/student/attendance')
def attend():
    return render_template('attendance.html')

@routes_bp.route('/student/subject')
def subject():
    return render_template('student-subject.html')

@routes_bp.route('/student/subject/overview')
def overview():
    return render_template('overview.html')

@routes_bp.route('/home')
def homepage():
    return render_template('university_homepage.html')



@routes_bp.route('/student/create', methods=['POST'])
def create_student():
    try:
        # Get student data from the request
        data = request.json
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        password = data.get('password')
        class_id = data.get('class_id')

        # Validate required fields
        if not all([first_name, email, password]):
            return jsonify({'error': 'First name, email, and password are required'}), 400

        # Generate a UUID for the student
        student_id = str(uuid.uuid4())

        # Create a new student instance
        new_student = Student(student_id=student_id, first_name=first_name, last_name=last_name, email=email, password=password, class_id=class_id)

        # Save the student to the database
        student_id = Student.save(mongo, new_student.__dict__)

        return jsonify({'message': 'Student created successfully', 'student_id': student_id}), 201
    except Exception as e:
        return jsonify({'error': 'Internal Server Error','message': e}), 500
