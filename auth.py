import requests
import base64

def get_access_token():
    # Spotify for develepors Client ID and Client Secret
    CLIENT_ID = 'fa2a96fc5373446c96f6e98808569eb3'
    CLIENT_SECRET = 'e661f2687bbc433faf10e333163f3b03'

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

    if response.status_code != 200:
        raise Exception("Failed to retrieve Spotify access token")

    return response.json()['access_token']