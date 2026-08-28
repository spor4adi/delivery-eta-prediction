from pathlib import Path

location = Path(__file__).resolve()
BASE_DIR = location.parent
DATA_DIR = BASE_DIR/"data"
MODELS_DIR = BASE_DIR/"models"

DATA_PATH = DATA_DIR/"data_set.csv"