import os
import json

from common.pad_types import Monster

FILE_NAME = 'monster_api.json'

    
def load_monster_data(dir: str = 'raw-data/', fileLocation: str = FILE_NAME) -> list[Monster]:
    """Loads monsters from raw data file"""

    file_path = os.path.join(dir, fileLocation)
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    monsters = [Monster(m) for m in data['card']]
    return monsters