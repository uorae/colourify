import inquirer

def colour_to_music(characteristics):
	colour_map = {
		'red': {'energy': 0.8, 'valence': 0.8, 'tempo': 120, 'genres': ['pop', 'rock', 'dance']},
		'blue': {'energy': 0.3, 'valence': 0.4, 'tempo': 60, 'genres': ['jazz', 'acoustic', 'classical']},
		'yellow': {'energy': 0.7, 'valence': 0.9, 'tempo': 110, 'genres': ['indie', 'dance', 'electronic']},
		'green': {'energy': 0.5, 'valence': 0.6, 'tempo': 80, 'genres': ['ambient', 'folk', 'nature']},
		'purple': {'energy': 0.6, 'valence': 0.5, 'tempo': 100, 'genres': ['alternative', 'electronic']},
		'black': {'energy': 0.2, 'valence': 0.3, 'tempo': 70, 'genres': ['ambient', 'classical', 'indie']},
		'white': {'energy': 0.3, 'valence': 0.5, 'tempo': 80, 'genres': ['ambient', 'classical', 'acoustic']},
	}
	
	# Default to a neutral value if color not found
	return colour_map.get(characteristics.lower(), colour_map['black'])


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

# match answer["colour"]:
#     case "Red":
#         action-1
#     case "Orange":
#         action-2
#     case "Yellow":
#         action-3
#     case _:
#         action-default