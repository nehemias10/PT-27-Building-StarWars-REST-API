from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class People(db.Model):
    __tablename__ = 'people'

    uid = db.Column(db.integer, primary_key=True)
    name = db.Column(db.string(120), unique=False, nullable=False)
    gender = db.Column(db.string(120), unique=False, nullable=True)
    height = db.Column(db.integer, unique=False, nullable=True)
    hair = db.Column(db.string(120), unique=False, nullable=True)

    def __repr__(self):
        return '<People %r>' %self.name

    def serialize(self):
        return {
            "uid": self.uid,
            "name": self.name,
            "gender": self.gender,
            "height": self.height,
            "hair": self.hair,
        }

class Planets(db.Model):
    __tablename__ = "planets"

    uid = db.Column(db.integer, primary_key=True)
    name = db.Column(db.string(120), unique=False, nullable=False)
    population = db.Column(db.integer, unique=False, nullable=False)
    climate = db.Column(db.string(120), unique=False, nullable=True)

    def serialize(self):
        return {
            "uid": self.uid,
            "name": self.name,
            "population": self.population,
            "climate": self.climate,
        }


class FavPeople(db.Model):
    __tablename__ = "favPeople"
    id = db.Column(db.integer, primary_key=True)
    user_id = db.Column(db.integer, db.ForeingKey('user.id'))
    people_id = db.integer(db.integer, db.ForeingKey('people.id'))
    user = db.relationship(User)
    people = db.relationship(People)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "people_id": self.people_id,
        }

        class FavPlanets(db.Model):
    __tablename__ = "favPlanets"
    id = db.Column(db.integer, primary_key=True)
    user_id = db.Column(db.integer, db.ForeingKey('user.id'))
    planet_id = db.integer(db.integer, db.ForeingKey('planets.id'))
    user = db.relationship(User)
    planets = db.relationship(Planets)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id,
        }




