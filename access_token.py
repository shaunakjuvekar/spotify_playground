import requests
import base64
from config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET

def get_token():
    # Import client id and secret
    CLIENT_ID = SPOTIFY_CLIENT_ID
    CLIENT_SECRET = SPOTIFY_CLIENT_SECRET

    # Base64 encode the client ID and client secret
    client_credentials = f"{CLIENT_ID}:{CLIENT_SECRET}"
    client_credentials_base64 = base64.b64encode(client_credentials.encode())

    # Request the access token
    token_url = 'https://accounts.spotify.com/api/token'
    headers = {
        'Authorization': f'Basic {client_credentials_base64.decode()}'
    }
    data = {
        'grant_type': 'client_credentials'
    }
    response = requests.post(token_url, data=data, headers=headers)

    if response.status_code == 200:
        access_token = response.json()['access_token']
        print("Access token obtained successfully.")
        return access_token
    else:
        print("Error obtaining access token.")
        exit()
