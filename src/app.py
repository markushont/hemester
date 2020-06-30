from flask import Flask, escape, request
import requests

app = Flask(__name__)

G_BASE_URL = 'https://maps.googleapis.com/maps/api'
G_API_KEY = 'asdasdqwewtwe'

@app.route('/api/route', methods=['GET'])
def get_route():
    origin = request.args.get('origin')
    destination = request.args.get('destination')

    route_response = requests.get(
        f'{G_BASE_URL}/directions/json?origin={origin}&destination={destination}&key={G_API_KEY}'
    )

    if not route_response.ok:
        return { 'error_code': route_response.status_code, 'message': route_response.text }
    
    location = route_response.json().get('routes')[0].get('legs')[0].get('end_location')
    print(route_response.json().get('routes')[0].get('legs')[0])
    location_str = ','.join([str(location.get('lat')), str(location.get('lng'))])
    print(location_str)

    places_response = requests.get(
        f'{G_BASE_URL}/place/nearbysearch/json?location={location_str}&radius=5000&key={G_API_KEY}&type=roofing_contractor'
    )

    if not places_response.ok:
        return { 'error_code': route_response.status_code, 'message': route_response.text }
    
    return places_response.json()

