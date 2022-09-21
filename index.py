from app import app, db

# app.config['SQLALCHEMY_DATABASE_URI'] = ''

# db.init_app(app)

if __name__ == '__main__':
    db.create_all()
    app.run('0.0.0.0', 5000, debug=True)