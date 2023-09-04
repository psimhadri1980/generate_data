import yaml
import json
from typing import Any

def load_yaml_from_file(fileName):
    """helper to load a YAML mock-config from file"""
    with open(fileName, 'r') as file:
        config =  yaml.load(file, Loader=yaml.FullLoader)
        return config

def convert_dict_to_object(dictionary, config_class):
    """helper to convert dictionary to an python object of Any Config type """
    return json.loads(json.dumps(dictionary), object_hook=config_class)

def load_config(fileName, config_class):
    return convert_dict_to_object(load_yaml_from_file(fileName), config_class)