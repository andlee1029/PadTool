import os
import json

FILE_NAME = 'player_api.json'

def load_player_data(directory = './raw-data', file_name = FILE_NAME):
    file_path = os.path.join(directory, file_name)
    with open(file_path, 'r') as f:
        data = json.load(f)
    cards = data['card']
    return [card[5] for card in cards]
    
