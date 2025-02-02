import inquirer
import recommendation

def colour_to_music(colour):
	colour_map = {
		'red': {'genres': ['rock']},
		'orange': {'genres': ['reggae']},
		'yellow': {'genres': ['indie']},
		'green': {'genres': ['folk']},
		'blue': {'genres': ['blues']},
		'purple': {'genres': ['shoegaze']},
		'black': {'genres': ['visual kei']},
		'white': {'genres': ['classical']},
	}
	
	# Default to a neutral value if color not found
	return colour_map.get(colour.lower(), colour_map['white'])


# welcome - prompt colour choice
print("Welcome to Colourify!")
questions = [
	inquirer.List(
		"colour",
		message = "What colour do you feel today?",
		choices = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Black", "White"],
	),
]

# map colour choice to music genres
answer = inquirer.prompt(questions)
print("Today I'm feeling " + answer['colour'] + "!\n")
genres = colour_to_music(answer['colour'])

# fetch unfiltered recommendations
track_json = recommendation.fetch_recs(genres['genres'])
track_info = {}

for track in track_json['items']:
	id = track['id']
	if id not in track_info:
		track_info[id] = {
			"Track Title": track['name'],
			"Artist(s)": ', '.join([artist['name'] for artist in track['artists']]),
			"Album Name": track['album']['name'],
			"Release Date": track['album']['release_date'],
			"Explicit?": track['explicit'],
			"Popularity": track["popularity"]
		}

sorted_recs = recommendation.sort_recs(track_info)

for rec in sorted_recs.values():
	print(f"'{rec['Track Title']}' by {rec['Artist(s)']} [{rec['Release Date']}]")

# match answer["colour"]:
#     case "Red":
#         action-1
#     case "Orange":
#         action-2
#     case "Yellow":
#         action-3
#     case _:
#         action-default