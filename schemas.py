from marshmallow import Schema, fields, validate, ValidationError, EXCLUDE

class UserSchema(Schema):
    class Meta:
        unknown = EXCLUDE
    id = fields.Integer(dump_only=True)
    username = fields.String(required=True, validate=validate.Length(min=3, max=80))
    email = fields.Email(required=True)
    role = fields.String(required=True, validate=validate.OneOf(['admin', 'teacher', 'student']))
    password = fields.String(load_only=True, validate=validate.Length(min=6))

class StudentSchema(Schema):
    id = fields.Integer(dump_only=True)
    user_id = fields.Integer(allow_none=True)
    student_id = fields.String()
    name = fields.String()
    email = fields.Email()

class TeacherSchema(Schema):
    id = fields.Integer(dump_only=True)
    user_id = fields.Integer(required=True)
    teacher_id = fields.String(required=False, validate=validate.Length(min=3, max=20))
    name = fields.String(required=True, validate=validate.Length(min=1, max=100))
    email = fields.Email(required=True)


class CourseSchema(Schema):
    class Meta:
        unknown = EXCLUDE
    id = fields.Integer(dump_only=True)
    course_name = fields.String(required=True, validate=validate.Length(min=1, max=100))
    course_code = fields.String(required=True, validate=validate.Length(min=2, max=20))
    teacher_id = fields.Integer(required=False, allow_none=True)
  



class EnrollmentSchema(Schema):
    id = fields.Integer(dump_only=True)
    student_id = fields.Integer()
    course_id = fields.Integer()
    grade = fields.Float()
    student = fields.Nested(lambda: StudentSchema(exclude=('enrollments',)))
    course = fields.Nested(lambda: CourseSchema(exclude=('enrollments',)))

# Create instances of schemas
user_schema = UserSchema()
student_schema = StudentSchema()
teacher_schema = TeacherSchema()
course_schema = CourseSchema()
enrollment_schema = EnrollmentSchema()

def validate_user_data(data):
    errors = user_schema.validate(data)
    if errors:
        raise ValidationError(errors)

def validate_student_data(data):
    errors = student_schema.validate(data)
    if errors:
        raise ValidationError(errors)

def validate_teacher_data(data, partial=False):
    try:
        teacher_schema.load(data, partial=partial)
    except ValidationError as err:
        raise err

def validate_course_data(data):
    try:
        validated_data = course_schema.load(data)
        return validated_data
    except ValidationError as err:
        raise err

def validate_enrollment_data(data):
    try:
        return enrollment_schema.load(data)
    except ValidationError as err:
        raise err