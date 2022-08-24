"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, People, FavPeople, Planets, FavPlanet
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def get_User():
    all_user = User.query.all()
    serializados = list(map(lambda user: user.serialize(),all_user))
    print(all_user)
    return jsonify({
        "mensaje": "Todos los Usuarios",
        "users": serializados
    }), 200



@app.route('/people', methods=['GET'])
def getPeople():
    all_people = People.query.all()
    serializados = list( map( lambda people: people.serialize(), all_people))
    print(all_people)

    return jsonify({
        "mensaje": "Todos los Personajes",
        "people": serializados
    }), 200

@app.route('/people/<int:idpeople>', methods=['GET'])
def dinamycPeople(idpeople):
    one = People.query.filter_by(uid=idpeople).first()
    if(one):
        return jsonify({
            "id": idpeople,
            "people": one.serialize()
        }), 200
        
    else:
        return jsonify({
                "id": idpeople,
                "people": "not found!"
        }), 404



@app.route('/planets', methods=['GET'])
def getPlanets():
    all_planets = Planets.query.all()
    serializados = list( map( lambda planets: planets.serialize(), all_planets))
    print(all_planets)

    return jsonify({
        "mensaje": "Todos los Planetas",
        "planets": serializados
    }), 200
@app.route('/planets/<int:idplanets>', methods=['GET'])
def dinamycPlanets(idplanets):
    one = Planets.query.filter_by(uid=idplanets).first()
    if(one):
        return jsonify({
            "id": idplanets,
            "planets": one.serialize()
        }), 200
        
    else:
        return jsonify({
                "id": idplanets,
                "planets": "not found!"
        }), 404





@app.route("/favorite/people/<int:people_id>", methods=['POST'])
def postPeopleFav(people_id):
    body = request.get_json() #recibir datos del usuario
    #people_id = 4
    #email = freddyloboq@gmail.com
    newFav = FavPeople(user=body['email'], people = people_id)
    db.session.add(newFav)
    db.session.commit()
    return "nuevo favorito agregado"

@app.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def postFavPlanet(planet_id):
    body = request.get_json() #recibir datos del usuario
    one = Planets.query.get(planet_id)
    oneSerializado = one.serialize()
    newFav = FavPeople(user=body['email'], planets=oneSerializado["name"])
    db.session.add(newFav)
    db.session.commit()
    return "nuevo favorito agregado"

@app.route("/favorite/people/<int:position>", methods=['DELETE'])
def deletePeopleFav(position):
    FavPeople.query.filter(FavPeople.id == position).delete()
    db.session.commit()
    return "favorito Eliminado"

@app.route("/favorite/planets/<int:position>", methods=['DELETE'])
def deletePlanetsFav(position):
    FavPlanet.query.filter(FavPlanet.id == position).delete()
    db.session.commit()
    return "favorito Eliminado"
    




# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
