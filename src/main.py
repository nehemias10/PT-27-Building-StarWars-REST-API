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
from models import db, User, People
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
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

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
    return jsonify({
        "mensaje": "Todos los Planets",
        "people": []
    })

@app.route('/planets/<int:idplanets>', methods=['GET'])
def dinamycPlanets(id):
    return jsonify({
        "id": id,
        "mensaje": "Planetas dinamico"
    })

@app.route('/users', methods=['GET'])
def getUsers():
    return jsonify({
        "mensaje": "Get a list of all the blog post users"
        
    })

@app.route('/users/favorites', methods=['GET'])
def getUsersFav():
    return jsonify({
        "mensaje": "Get all the favorites that belong to the current user"
    })

@app.route("/favorite/people/<int:people_id>", methods=['POST'])
def postPeopleFav(people_id):
    body = request.get_json() #recibir datos del usuario
    #people_id = 4
    #email = freddyloboq@gmail.com
    newFav = FavPeople(user=body['email'], people= people_id)
    db.session.add(newFav)
    db.session.commit()
    return "nuevo favorito agregado"
    

@app.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def postFavPlanet(planet_id):
    return jsonify({
        "mensaje": "Add a new favorite planet to the current user with the planet id = planet_id"
    })


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
