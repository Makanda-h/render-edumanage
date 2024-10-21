from app import app
from models import db, User, Student, Teacher, Course, Enrollment

def seed_database():
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()

        # Create users
        admin = User(username='admin', email='admin@example.com', role='admin')
        admin.set_password('adminpass')

        teacher1 = User(username='teacher1', email='teacher1@example.com', role='teacher')
        teacher1.set_password('teacher1pass')

        student1 = User(username='student1', email='student1@example.com', role='student')
        student1.set_password('student1pass')

        student2 = User(username='student2', email='student2@example.com', role='student')
        student2.set_password('student2pass')

        db.session.add_all([admin, teacher1, student1, student2])
        db.session.commit()

        # Create teacher and students
        teacher = Teacher(user_id=teacher1.id, teacher_id='T001', name='Teacher One', email=teacher1.email)
        student_1 = Student(user_id=student1.id, student_id='S001', name='Student One', email=student1.email)
        student_2 = Student(user_id=student2.id, student_id='S002', name='Student Two', email=student2.email)

        db.session.add_all([teacher, student_1, student_2])
        db.session.commit()

        # Create courses
        course1 = Course(course_name='Introduction to Python', course_code='PY101')
        course2 = Course(course_name='Web Development Basics', course_code='WD101')

        # Assign teacher to courses
        course1.teachers.append(teacher)
        course2.teachers.append(teacher)

        db.session.add_all([course1, course2])
        db.session.commit()

        # Create enrollments
        enrollment1 = Enrollment(student_id=student_1.id, course_id=course1.id)
        enrollment2 = Enrollment(student_id=student_1.id, course_id=course2.id)
        enrollment3 = Enrollment(student_id=student_2.id, course_id=course1.id)

        db.session.add_all([enrollment1, enrollment2, enrollment3])
        db.session.commit()

        print("Database seeded successfully!")