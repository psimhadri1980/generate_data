from generate.utils import *
from generate.datasets import DatasetConfig
from generate.datasets import Dataset
from os import mkdir

import datetime
from importlib import import_module
from faker import Faker
from faker.utils.loading import find_available_locales, find_available_providers

class DatasetGenerator:
    
    def __init__(self, config_path, target_path):
        self.config_path = config_path
        self.target_path = target_path
        self.my_fake = Faker()
        self.custom_providers = find_available_providers([import_module("providers")])
        for provider in self.custom_providers:
             self.my_fake.add_provider(import_module(provider).Provider)

    def generate(self):
        configs = load_config(self.config_path, DatasetConfig)
        target_gen_path = self.target_path + "/" + datetime.datetime.now().strftime("%y_%m_%d_%H_%M_%S")
        mkdir(target_gen_path)
        
        self.datasets = {}
        for config in configs:
            dataset = Dataset(self.my_fake, config)
            dataset.generate(target_gen_path, self.datasets)
            self.datasets[config.name] = dataset
