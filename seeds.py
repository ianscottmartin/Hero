from sqlalchemy.orm import sessionmaker
from models import Base, User, Hero
from sqlalchemy import create_engine



engine = create_engine('sqlite:///comic_app.db')
Session = sessionmaker(bind=engine)

def create_sample_data():
    session = Session()

    users = [
        User(username='Silent Bob'),
        User(username='Jay'),
        User(username='Dante'),
        User(username='Randal'),
        User(username='Olaf'),
        User(username='Brodie')
    ]
    session.add_all(users)

    heroes = [
        Hero(name='Spider-Man'),
        Hero(name='Iron Man'),
        Hero(name='Wonder Woman'),
        Hero(name='Dr Strange'),
        Hero(name='Black Panther'),
        Hero(name='Moon Knight'),
        Hero(name='Thor'),
        Hero(name='Prof X'),
        Hero(name='Cyclops'),
        Hero(name='Mageto'),
        Hero(name='Batman'),
        Hero(name='Superman')
    ]
    session.add_all(heroes)