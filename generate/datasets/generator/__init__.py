from faker import Faker

class ColumnGenerator:
    
    def __init__(self, faker):
        self.faker = faker

    def __simple_value(self, type):
        if hasattr(self.faker, '%s' % type ):
            return getattr(self.faker, '%s' % type)()
        else:
            return None
    
    def __complex_value (self, type):
        sub_types = type.split(":")
        value = self.__simple_value(sub_types.pop(0))
        for sub_type in sub_types:
            if(sub_type == "<RANDOM>"):
                sub_type = self.faker.random_int(min=0, max=(len(value)-1))
            print (sub_type)
            value = value[sub_type]
        return value
       
    def __depends_on_values(self, dataset, attribute, datasets):
        attribute_type = attribute.type.split(".")[1]
        attribute_source = attribute.type.split(".")[0]
        generate_rows_count = dataset.config.row_count
        from_dataset = dataset
        if(attribute_source != "self"):
            from_dataset = datasets.get(attribute_source)
        return self.__get_columns_values_from_generated_dataset(from_dataset, attribute_type, generate_rows_count)


    def __get_columns_values_from_generated_dataset(self, dataset, attribute_type, generate_rows_count):
        depends_on_values = dataset.data[dataset.attribute_names.index(attribute_type)]
        column_values = self.faker.random_elements(depends_on_values, generate_rows_count, unique=False, use_weighting=True)
        return column_values

 
    def __depends_on_hierarchy(self, dataset, attribute):
        pass
            
    def column_values(self, dataset, attribute, datasets):
        column_values = []
        if (attribute.category == "SIMPLE"):
            for index in range(dataset.config.row_count):
                column_values.append(self.__simple_value(attribute.type))
        elif(attribute.category == "COMPLEX"):
            for index in range(dataset.config.row_count):
                column_values.append(self.__complex_value(attribute.type))
        elif (attribute.category == "DEPENDS_ON"):
            column_values = self.__depends_on_values(dataset, attribute, datasets)
        return column_values

