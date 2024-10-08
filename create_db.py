from taskmanager import app, db

# Create an application context and create all the tables
with app.app_context():
    db.create_all()
    print("Database tables created successfully!")
