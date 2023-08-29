from faker import Faker

class ColumnGenerator:
    
    def __init__(self, faker):
        self.faker = faker

    def __simple_value(self, type):
        if hasattr(self.faker, '%s' % type ):
            return getattr(self.faker, '%s' % type)()
        else:
            return None
        
    def __depends_on_values(self, dataset, attribute, datasets):
        attribute_type = attribute.type.split(".")[1]
        attribute_source = attribute.type.split(".")[0]
        if(attribute_source == "self"):
            depends_on_values = dataset.data[dataset.attribute_names.index(attribute_type)]
            column_values = self.faker.random_elements(depends_on_values, dataset.config.row_count, unique=False, use_weighting=True)
            return column_values
        elif attribute_source in datasets:
            foreign_dataset = datasets.get(attribute_source)
            depends_on_values = foreign_dataset.data[foreign_dataset.attribute_names.index(attribute_type)]
            column_values = self.faker.random_elements(depends_on_values, dataset.config.row_count, unique=False, use_weighting=True)
            return column_values
        else:
            print("Unknown Source Attribute configured.. Please correct it")

 
    def __depends_on_hierarchy(self, dataset, attribute):
        pass
            
    def column_values(self, dataset, attribute, datasets):
        column_values = []
        if (attribute.category == "SIMPLE"):
            for index in range(dataset.config.row_count):
                column_values.append(self.__simple_value(attribute.type))
        elif (attribute.category == "DEPENDS_ON"):
            column_values = self.__depends_on_values(dataset, attribute, datasets)
        return column_values

