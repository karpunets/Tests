import os


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PROPERTIES_DIR = os.path.join(ROOT_DIR, "settings.json")
DATA_DIR = os.path.join(ROOT_DIR, "Data")
DATA_TO_CLEAN = os.path.join(DATA_DIR, "data_to_clean.txt")
