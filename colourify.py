import inquirer
import recommendation

def colour_to_music(colour):
	colour_map = {
		'red': {'genres': ['rock', 'pop', 'dance']},
		'orange': {'genres': ['reggae', 'soul', 'acoustic']},
		'yellow': {'genres': ['indie', 'folk', 'pop']},
		'green': {'genres': ['country', 'folk', 'ambient']},
		'blue': {'genres': ['blues', 'jazz', 'classical']},
		'purple': {'genres': ['lo-fi', 'dream pop', 'shoegaze']},
		'black': {'genres': ['metal', 'alternative emo', 'visual kei']},
		'white': {'genres': ['ambient', 'classical', 'acoustic']},
	}
	
	# Default to a neutral value if color not found
	return colour_map.get(colour.lower(), colour_map['white'])


# welcome
print("Welcome to Colourify!")
questions = [
	inquirer.List(
		"colour",
		message="What colour do you feel today?",
		choices=["Red", "Orange", "Yellow", "Green", "Blue", "Purple"],
	),
]

answer = inquirer.prompt(questions)
genres = colour_to_music(answer['colour'])

track_json = recommendation.fetch_recs(genres['genres'])
for track_info in track_json['items']:
	title = track_info['name']
	artist = track_info['artists'][0]['name']

	print(title + ' by ' + artist)
# match answer["colour"]:
#     case "Red":
#         action-1
#     case "Orange":
#         action-2
#     case "Yellow":
#         action-3
#     case _:
#         action-default