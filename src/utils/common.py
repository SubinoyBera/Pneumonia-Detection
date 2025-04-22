import os
import sys
import yaml
import joblib
from src.logger import logging
from src.exception import CustomException
from box import ConfigBox
from ensure import ensure_annotations
from pathlib import Path

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"yaml file: {path_to_yaml} loaded successfully.")
            
            return ConfigBox(content)
        
    except Exception as e:
        raise CustomException(f"Failed to read yaml file from {path_to_yaml}: {e}", sys)

@ensure_annotations
def create_directories(path_to_directories: list, verbose = True):
    try:
        for path in path_to_directories:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logging.info(f"Created directory: {path}")

    except Exception as e:
        raise CustomException(f"Failed to create directory at {path}: {e}", sys)

@ensure_annotations
def save_binary(data: any, path: Path):
    try:
        joblib.dump(value = data, filename = path)
        logging.info(f"Successfully save binary file at {path}")

    except Exception as e:
        raise CustomException(f"Failed to save binary file at {path}: {e}", sys)

@ensure_annotations    
def load_binary(path: Path) -> any:
    try:
        data = joblib.load(path)
        logging.info(f"Loaded binary file successfully from {path}")

    except Exception as e:
        raise CustomException(f"Failed to load binary file from {path}: {e}", sys)

@ensure_annotations
def get_size(path: Path) -> str:
    size_in_kb = round(os.path.getsize(path)/1024)
    
    return f"- {size_in_kb} KB"
