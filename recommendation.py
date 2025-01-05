import requests
import auth

ACCESS_TOKEN = auth.get_access_token()

# Spotify Recommendations API Endpoint
url = 'https://api.spotify.com/v1/recommendations'

# Set headers with the access token
headers = {
  'Authorization': f'Bearer {ACCESS_TOKEN}'
}

# Define the parameters for the recommendations
params = {
  # 'seed_artists': # artist ID
  # 'seed_tracks': # track ID
  # 'seed_genres': # genre
  # 'limit': # Number of recommendations to fetch
  # 'min_energy': # decimal e.g 0.4
  # 'max_energy': 
}

# Send GET request to Spotify Recommendations API
response = requests.get(url, headers=headers, params=params)

# Check for successful request
if response.status_code == 200:
    recommendations = response.json()['tracks']
    print(recommendations)
else:
    print("Error fetching recommendations:", response.status_code)
    print(response.json())