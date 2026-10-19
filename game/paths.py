from pathlib import Path

BASE_DIR = Path(__file__).parent.parent   # the dungeon-rpg folder
DATA_DIR = BASE_DIR / "data"
RACES_PATH = DATA_DIR / "races.json"
CLASSES_PATH = DATA_DIR / "classes.json"