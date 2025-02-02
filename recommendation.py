import requests
from datetime import datetime
import auth

ACCESS_TOKEN = auth.get_access_token()

def fetch_recs(genres):
  # Spotify Search API Endpoint
  url = 'https://api.spotify.com/v1/search'

  # Set headers with the access token
  headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}'
  }

  query = f"genre:{' genre:'.join(genres)}"

  # Define the parameters for the recommendations 
  params = {
    'q': query,
    'type': 'track',
    'limit': 50, # Number of recommendations to fetch
  }

  # Send GET request to Spotify Recommendations API
  response = requests.get(url, headers=headers, params=params)

  # Check for successful request
  if response.status_code != 200:
    raise Exception("Error fetching recommendations")

  return response.json()['tracks']

# # sort by popularity and release date
def sort_recs(recommmended_tracks):
  # prioritising latest releases:
  for track in recommmended_tracks.values():

    # accounting for missing date values
    release_date = (track['Release Date'])
    if len(release_date) == 4:  # It's only a year (e.g., "2020")
      release_date = datetime.strptime(release_date, "%Y")
    elif len(release_date) == 7:  # It's only a year and month (e.g., "2020-01")
      release_date = datetime.strptime(release_date, "%Y-%m")
    else:
      # Otherwise, the date is in full (e.g., "2023-06-15")
      release_date = datetime.strptime(release_date, "%Y-%m-%d")

    # Calculate the time span between release date and today's date
    since_release = datetime.today() - release_date

    # Calculate the weighted popularity score based on time span (e.g., more recent releases have higher weight)
    track['Popularity'] = track['Popularity'] * (1 / (since_release.days + 1))

  return dict(sorted(recommmended_tracks.items(), key=lambda item: item[1]['Popularity'], reverse=True))