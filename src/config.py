"""Configuration Constants"""

from pathlib import Path

REPO_ROOT: Path = Path(__file__).resolve().parent

# Data URL Path
RAW_DATA_PATH: str = "https://docs.google.com/spreadsheets/d/1-oE6cmsbq8TFLB7tVy6uIJnyM1Ab3fIaJ7_wLImESb4/export?format=csv"

# Directory Paths
ETL_GOOGLESHEET_DIR: Path = REPO_ROOT / "etl_googlesheet"
FEATURE_ENGINEERING_DIR: Path = REPO_ROOT / "feature_engineering"
FASTAPI_DIR: Path = REPO_ROOT / "fastapi_app"

# Bucket Directory
BUCKET_MODELS_DIR: str = "models"
BUCKET_IMG_DIR: str = "img"

# Feature Registry Path
FEATURE_REGISTRY_INPUT_PATH: Path = FEATURE_ENGINEERING_DIR / "feature_registry.yaml"

# Data Table Names
APPT_NAME: str = "Appointment"
CATEGORY_NAME: str = "Category"
FEATURES_NAME: str = "Features"
FEATURE_REGISTRY_NAME: str = "FeatureRegistry"
MODEL_REGISTRY_NAME: str = "ModelRegistry"
FEEDBACK_NAME: str = "Feedback"

# Data Table Column Names
APPT_ID_COL: str = "appt_id"
CATEGORY_ID_COL: str = "category_id"
FEATURES_ID_COL: str = "feature_id"
FEATURE_REGISTRY_ID_COL: str = "f_reg_id"
FEATURE_REGISTRY_CONFIG_COL: str = "config"
MODEL_REGISTRY_ID_COL: str = "model_id"
MODEL_REGISTRY_TOP_MODELS_COL: str = "top_models"

# Model Artifact Names
TRAINED_MODELS_NAME: str = "trained_models.pkl"
ONEHOT_ENCODE_COLS_NAME: str = "onehot_columns.pkl"

# Configuration Parameters
#TODO Find Feature or Model Registry cannot be found, revert back to the last created versions
FEATURE_REGISTRY_ID_VAL: str = "e3dd644e-a400-485a-8084-e154c3c247c4"
MODEL_REGISTRY_ID_VAL: str = "1f9b814e-5b13-4bdf-9dbc-6dfff0798ba0"
ENSEMBLE_NUM: int = 2
ENSEMBLE_RANKING_METRIC: str = "mse"
ENSEMBLE_STRATEGY: str = "mean"
