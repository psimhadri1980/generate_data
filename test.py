import providers.amount as AmountProvider
from faker import Faker

try:
    fake = Faker()
    fake.add_provider (AmountProvider)
except:
    print("Exception while adding provider")
    
print(fake.amount())