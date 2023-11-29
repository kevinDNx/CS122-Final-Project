import geocoder

def get_current_location():
    # Get current location based on IP address
    location = geocoder.ip('me')

    # Extract latitude and longitude
    latitude = location.latlng[0]
    longitude = location.latlng[1]

    return latitude, longitude

if __name__ == "__main__":
    try:
        latitude, longitude = get_current_location()
        print(f"Your current location is: Latitude {latitude}, Longitude {longitude}")
    except Exception as e:
        print(f"Error: {e}")
