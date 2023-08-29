from generate.datasets.generator import ColumnGenerator
import pandas as pd

class DatasetConfig:
    """Dataset Config Object per config in YAML"""
    def __init__(self, config):
        self.__dict__.update(config)
        

class Dataset:
    """Dataset Object """
    def __init__(self, faker, config):
        self.faker = faker
        self.config = config
        self.dataset_name = self.config.name
        self.attribute_names = []
        for attribute in self.config.attributes:
            self.attribute_names.append(attribute.name)
        self.data = []
        self.generator = ColumnGenerator(self.faker)
        
        
    def generate(self, target_path, datasets):
        
        self.file_name = target_path + "/" + self.dataset_name  + ".csv"
        
        for attribute in self.config.attributes:
            self.data.append(self.generator.column_values(self, attribute, datasets))

        data_frame = pd.DataFrame(dict(zip(self.attribute_names, self.data)))
        data_frame.to_csv(self.file_name)