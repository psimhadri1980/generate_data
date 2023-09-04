from providers.industry import Provider as IndustryProvider
from faker import Faker

try:
    fake = Faker()
    fake.add_provider (IndustryProvider)
except:
    print("Exception while adding provider")
    
def simple_value(type):
    if hasattr(fake, '%s' % type ):
        return getattr(fake, '%s' % type)()
    else:
        return None

def _complex_value (type):
    sub_types = type.split(":")
    value = simple_value(sub_types.pop(0))
    for index, sub_type in enumerate(sub_types):
        if(sub_type == "<RANDOM>"):
            sub_type = fake.random_int(min=0, max=(len(value)-1))
        print (sub_type)
        value = value[sub_type]
    return value

          
print(_complex_value("industry:level-1:<RANDOM>:name"))
#print(simple_value("industry")['level-1'][1]['name'])
