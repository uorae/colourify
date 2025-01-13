import requests
import auth

ACCESS_TOKEN = auth.get_access_token()

def fetch_recs():
  # Spotify Search API Endpoint
  url = 'https://api.spotify.com/v1/search'

  # Set headers with the access token
  headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}'
  }

  # Define the parameters for the recommendations
  params = {
    #'q': f'genre:{}',
    'type': 'track',
    'limit': 20, # Number of recommendations to fetch
  }

  # Send GET request to Spotify Recommendations API
  response = requests.get(url, headers=headers, params=params)

  # Check for successful request
  if response.status_code != 200:
    raise Exception("Error fetching recommendations")

  return response.json()['tracks']