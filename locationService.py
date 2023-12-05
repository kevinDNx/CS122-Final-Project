import geocoder
import requests

def get_current_location():
    # Get current location based on IP address
    location = geocoder.ip('me')

    # Extract latitude and longitude
    latitude = location.latlng[0]
    longitude = location.latlng[1]
    return latitude, longitude
