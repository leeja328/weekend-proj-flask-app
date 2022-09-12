from flask import Blueprint
from marvel_inventory.helpers import token_required
from marvel_inventory.models import db, Drone, drone_schema, drones_schema


api = Blueprint('api', __name__, url_prefix = '/api')

@api.route('/getdata')
def getdata(current_user_token):
    return {'name': 'lando'}


# CREATE LOCATION ENDPOINT
@api.route('/drones', methods = ['POST'])
@token_required
def create_location(current_user_token):
    tested_positive = request.json['tested_positive']
    country = request.json['country']
    state = request.json['state']
    city = request.json['city']
    deaths = request.json['deaths']
    series = request.json['series']
    user_token = current_user_token.token

    print(f"User Token: {current_user_token.token}")

    drone = Drone(tested_positive, country, state, city, deaths, series, user_token, series, user_token = user_token)

    db.session.add(drone)
    db.session.commit()

    response = drone_schema.dump(drone)

    return jsonify(response)


    # Retrieve ONE location endpoint
@api.route('/drones/<id>', methods = ['GET'])
@token_required
def get_location(current_user_token, id):
    owner = current_user_token.token
    if owner == current_user_token.token:
        drone = Drone.query.get(id)
        response = drone_schema.dump(drone)
        return jsonify(response)
    else:
        return jsonify({'message': 'Valid Token Required'}), 401



#  Retrieve All locations
@api.route('/drones', methods = ['GET']) 
@token_required
def get_location(current_user_token):
    owner = current_user_token.token
    drones = Drone.query.filter_by(user_token = owner).all()
    response = drones_schema.dump(drones)
    return jsonify(response)







# Delete location Endpoint
@api.route('/drones/<id>', methods = ["DELETE"])
@token_required
def delete_location(current_user_token, id):
    drone = Drone.query.get(id)
    db.session.delete(drone)
    db.session.commit()
    response = drone_schema.dump(drone)
    return jsonify(response)



