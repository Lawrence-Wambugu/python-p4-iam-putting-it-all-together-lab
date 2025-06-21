from app import app, db  # import db after it's been initialized with app in app.py
from models import User, Recipe

with app.app_context():
    db.drop_all()
    db.create_all()

    user1 = User(username='lawrence', image_url='https://example.com/image.jpg', bio='Fullstack Dev')
    user1.password_hash = 'password123'

    recipe1 = Recipe(
        title='Fried Rice',
        instructions='Boil rice until soft. In a pan, fry onions, add veggies, then mix in the rice. Cook for 5 mins.',
        minutes_to_complete=15,
        user=user1
    )

    db.session.add_all([user1, recipe1])
    db.session.commit()
