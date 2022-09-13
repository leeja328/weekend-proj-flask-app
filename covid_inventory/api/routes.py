from flask import Blueprint, request, jsonify
from covid_inventory.helpers import token_required
from covid_inventory.models import db, Location, location_schema, locations_schema


api = Blueprint('api', __name__, url_prefix = '/api')

@api.route('/getdata')
def getdata(current_user_token):
    return {'name': 'lando'}


# CREATE LOCATION ENDPOINT
@api.route('/locations', methods = ['POST'])
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

    location = Location(tested_positive, country, state, city, deaths, series, user_token, series, user_token = user_token)

    db.session.add(location)
    db.session.commit()

    response = location_schema.dump(location)

    return jsonify(response)


    # Retrieve ONE location endpoint
# @api.route('/locations/<id>', methods = ['GET'])
# @token_required
# def get_location(current_user_token, id):
#     owner = current_user_token.token
#     if owner == current_user_token.token:
#         location = Location.query.get(id)
#         response = location_schema.dump(location)
#         return jsonify(response)
#     else:
#         return jsonify({'message': 'Valid Token Required'}), 401



#  Retrieve All locations
@api.route('/locations', methods = ['GET']) 
@token_required
def get_location(current_user_token):
    owner = current_user_token.token
    locations = Location.query.filter_by(user_token = owner).all()
    response = locations_schema.dump(locations)
    return jsonify(response)




# Delete location Endpoint
# @api.route('/locations/<id>', methods = ["DELETE"])
# @token_required
# def delete_location(current_user_token, id):
#     location = Location.query.get(id)
#     db.session.delete(location)
#     db.session.commit()
#     response = location_schema.dump(location)
#     return jsonify(response)



