import os


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_DIR = os.path.join(ROOT_DIR, "config")
DATA_DIR = os.path.join(ROOT_DIR, "Data")
SCHEMAS_DIR = os.path.join(DATA_DIR, "schemas")

SETTINGS = os.path.join(CONFIG_DIR, "settings.json")
PROJECT_CONFIG = os.path.join(CONFIG_DIR, "project.cfg")
DATA_TO_CLEAN = os.path.join(DATA_DIR, "data_to_clean.txt")
