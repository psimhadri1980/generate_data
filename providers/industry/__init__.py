from faker.providers import BaseProvider
from typing import Any

localized = False

class Provider(BaseProvider):
    """Implement custom Industries provider for Faker."""
    
    INDUSTRIES: list[dict[str:Any]] = [
            {'id': 100, 'name': 'Services & Export', 'naic_code' : '', 'iso_code' : '', 
                'level-1':[
                    {'id': 1001, 'name': 'IT Services', 'naic_code' : '', 'iso_code' : ''},
                    {'id': 1002, 'name': 'Exports', 'naic_code' : '', 'iso_code' : ''},
                    {'id': 1003, 'name': 'Hospitality', 'naic_code' : '', 'iso_code' : ''},
                    {'id': 1004, 'name': 'Imports', 'naic_code' : '', 'iso_code' : ''},
                ]
            },
            {'id': 200, 'name': 'Global Commercial Banks', 'naic_code' : '', 'iso_code' : '', 
                'level-1':[
                    {'id': 1001, 'name': 'Asset Management', 'naic_code' : '', 'iso_code' : ''},
                    {'id': 1002, 'name': 'Investment Banking', 'naic_code' : '', 'iso_code' : ''},
                    {'id': 1003, 'name': 'Private Banking', 'naic_code' : '', 'iso_code' : ''},
                    {'id': 1004, 'name': 'Structured Products', 'naic_code' : '', 'iso_code' : ''},
                ]
            },
        ]

    def industry(self):
        return self.random_element(self.INDUSTRIES)