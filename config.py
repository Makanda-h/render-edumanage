import os
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = '123456' 
JWT_SECRET_KEY = '678999'  

# postgresql://school_database_render_user:5pzjWPbcPwCtU1YZGquPiukhCtw5xnGb@dpg-csb2k3ogph6c73a8lve0-a.oregon-postgres.render.com/school_database_render