from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            
            # do not serialize the password, its a security breach
        }

class People(db.Model):
    __tablename__ = 'people'

    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    gender = db.Column(db.String(120), unique=False, nullable=True)
    height = db.Column(db.Integer, unique=False, nullable=True)
    hair = db.Column(db.String(120), unique=False, nullable=True)

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

    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    population = db.Column(db.Integer, unique=False, nullable=False)
    climate = db.Column(db.String(120), unique=False, nullable=True)

    def serialize(self):
        return {
            "uid": self.uid,
            "name": self.name,
            "population": self.population,
            "climate": self.climate,
        }


class FavPeople(db.Model):
    __tablename__ = "favPeople"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(120), db.ForeignKey('user.email'))
    people_uid = db.Column(db.Integer, db.ForeignKey('people.uid'))
    user = db.relationship(User)
    people = db.relationship(People)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "people_uid": self.people_uid,
        }

class FavPlanet(db.Model):
    __tablename__ = "favPlanet"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(120), db.ForeignKey('user.email'))
    planet_uid = db.Column(db.Integer, db.ForeignKey('planets.uid'))
    user = db.relationship(User)
    planet = db.relationship(Planets)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_uid": self.planet_uid,
        }



